# Zephyr board bring-up walkthrough

Commands and notes for the 25/04/2024 Zephyr Tech Talk.

## Setup folder

* Start from a clean sample directory

Do all the setup steps in Readme, then clone a new example-application with west init:
```
west init -m https://github.com/zephyrproject-rtos/example-application --mr main my-workspace
```
Don’t git clone directly, it creates a weird path.

* Update Zephyr modules
```
cd my-workspace
west update
```
* Try compilation
```
cd example-application
BOARD="custom_plank"
west build -b $BOARD -p always app
```

## Create our board
* Find a similar board dts to copy
Copy a board, to have presets and example configs

* SoC: STM32F405, but we can take an exemple from the same SoC series, and change SoC, for the demo
```
cd $Z/boards
grep -rnw ./ -e "name: stm32f40.*"
```
* Choosing stm32f4\_disco as a ref design - not the right SoC but we’ll change it
```
cp -r $Z/boards/st/stm32f4_disco/ ./boards/st
```

### Rename board files
```
rename "s/stm32f4_disco/totoboard/g" ./*
grep -rnw ./ -i -e ".*stm32f4_disco"
sed -i 's/stm32f4_disco/totoboard/' totoboard.yaml
sed -i 's/stm32f4_disco/totoboard/' board.yml
sed -i 's/STM32F4_DISCO/TOTOBOARD/' Kconfig.totoboard
```
* Docs folder can be updated later, it is mandatory if you want to contribute your board to Zephyr main

* Not mandatory but nice: customize compatible = "st,totoboard" and model description in dts file

### Try the board
```
BOARD="totoboard"
west build -p always -b $BOARD app
```
* It looks for examplesensor0, which is not here in our dts

### Import blinky
```
cp -r $Z/samples/basic/blinky ./
west build -p always -b $BOARD blinky
```

Don’t flash this, it still needs customizations.

* "zephyr,led0" in dts allows to choose the led actually blinked by software
 * You can see the call to zephyr,led0 if you open the blinky.c source
```
vim $Z/samples/basic/blinky/src/main.c
```

## DTS customisation
* Now modify the DTS file to match the board.

### SoC selection
```
find ./ -name "stm32f407Xg.dtsi"
```
The SoC description file is:
```
$Z/dts/arm/st/f4/stm32f4/stm32f405Xg.dtsi
```

The pinctrl file is:
```
find ../ -name "stm32f407v(e-g)tx-pinctrl.dtsi"
./modules/hal/stm32/dts/st/f4/stm32f407v(e-g)tx-pinctrl.dtsi
```

* Pincontrol file: check your board chip name (me: stm32f405vgtx-pinctrl because I have STM32F405VGT6)
* X is a standard wildcard for component name

* Also, change the SoC in board.yaml
```
grep -rnw ./ -e ".*stm32f407.*"
```

### Open schematics and find a LED + UART
Open schematics for the board.

* Orange LED: PC13 Active HIGH
* Blue button: PC14 Active LOW
* Rapid pull-up / pull-down check on schematics

* Usart accessible on USB port through ST-Link: Usart 6
* PC6/USART6\_TX
* PC7/USART6\_RX

* Remove can busses, disable OTG
* Change zephyr,shell to usart6

### Clock frequency
Check the main clock
* OSC\_IN -> NX3225GD-8MHZ
* HSE is 8 MHz in DTS
* There is a nice macro to avoid writing lots of zeros in frequency fields (in $Z/dts/common)

### Build and flash and run
```
west build -p always -b $BOARD blinky
west flash
```
Results: LED should blink and UART messages should be displayed.

## Shells
### Enable GPIO shell
```
tree -L 2 blinky
```
prj.conf: selects what will be build

In blinky prj.conf, add:
```
CONFIG_SHELL=y
CONFIG_GPIO_SHELL=y
```

Now, are you unsure about the option name? Should it be gpio shell or shell gpio?
Open the option catalogue, menuconfig:
```
west build -t menuconfig
```

* Log level for LED
Either put the logs on UART2 (zephyr,console=&usart2), or disable logs by modifying blinky sample.

## Use shell GPIO
```
gpio help
gpio info
```

* Yellow LED is on PC4
```
gpio conf
```

Gpio referenced by addresses, not nice names! So, tips to find the register address for our GPIOC peripheral:

* Pre-built DTS
```
vim ./build/zephyr/zephyr.dts
gpioc: gpio@40020800
```

* DTS visualition tool
```
dtsh
tree --format NKYC
```

* Setup GPIOC 4 to active high output and set to 1
```
gpio conf gpio@40020800 4 oh0
gpio set gpio@40020800 4 1

gpio blink gpio@40020800 4 1
```

* GPIO blink: useful for measurements with oscillo trigger?

* Read GPIO
User button PC14
```
gpio conf gpio@40020800 14 i
gpio get gpio@40020800 14
```
1 if not pressed, 0 if pressed

```
gpio conf gpio@40020800 14 il
```
0 if not pressed: OK

### Devmem shell
Read and modify misc peripheral config with devmem.

```
CONFIG_DEVMEM_SHELL (enabled by default)
```

Easy sample with input vs output

Register offset page 284

GPIO 0 controlled by the 2 lower bits
```
gpio conf gpio@40020800 0 i
devmem 40020800 32
gpio conf gpio@40020800 0 o
devmem 40020800 32
```
-> See 00 (Input state) become 01 (Output mode)!

Can also write in devmem:

```
devmem 40020800 32 0x400a000
```

## I2C shell
* Output connector I2C:
```
PB10/I2C2_SCL
PB11/I2C2_SDA
```
* From boards/st/nucleo\_f411re/nucleo\_f411re.dts:
```
&i2c1 {
        pinctrl-0 = <&i2c1_scl_pb8 &i2c1_sda_pb9>;
        pinctrl-names = "default";
        status = "okay";
        clock-frequency = <I2C_BITRATE_FAST>;
};
```

Copy and modify

```
CONFIG_I2C=y
CONFIG_I2C_SHELL=y
```
Build

* Time to mention SPI shell exists and was just merged
* Similar to i2cset/get and spidev in Linux, don’t need my Pi anymore

* First, show scan without daughter board: nothing displayed.

### I2C shell but this time it works
Then, with daughter board plugged in:
* Scan
```
i2c scan i2c@40005800
2d 53 57
```

Page 64 / page 159: I2C adresses are 0x53 and 0x57 (7-bits)

* Read I2C
```
i2c read i2c@40005800 53 0
```

* PE7 device enable / disable
It’s called ST25DX SPARE, and can be selected onboard, but also controlled by SoC
```
gpio get gpio@40021000 7

gpio conf gpio@40021000 7 o
gpio set gpio@40021000 7 1
```
-> Disables I2C device

* Can be used for osc measurements

* End of part 3: shell!

## Bringup complex subsystem
Systems that cannot just be checked with GPIO / i2c / spi simple commands.

### Display
Let’s say I made an advanced DTS
Switching back to:
```
BOARD="st25dv_mb1283_disco"
```

Simple sample:
```
cp -r ~/zephyrproject/zephyr/samples/drivers/display/ ./
west build -p always -b $BOARD display
```

Open the dts in:
```
vim $Z/boards/st/st25dv_mb1283_disco/st25dv_mb1283_disco.dts
```

For display, I added:
* SPI2 activation
* display driver using this SPI bus
* zephyr,display chosen to tell Zephyr where is the display
* header for some variables

### USB
```
cp -r ~/zephyrproject/zephyr/samples/subsys/usb/testusb/ ./
west build -p always -b $BOARD testusb
```

* Open dts to check how usb is described

* lsusb: NordicSemiconductor Zephyr testusb sample

# FAQ preshots
## SPI shell
Just merged!
It will look like this:

```
uart:~$ spi transceive spi@40013000 49 0
```

## Clock tree config
Currently manufacturer dependant.
In case of ST, use STMCube configurator, or SoC clock tree schem page 154, and some magic.

    vim $Z/dts/bindings/clock/st,stm32f4-pll-clock.yaml

See RFC & talk by Daniel DeGrasse

## More explanations about device tree

I did a lot of arbitrary copy-pasting, explanation:

### DTS bindings
* Describe DTS options, also count as code, sort of codumentation

For UART:
```
vim $Z/dts/bindings/serial/uart-controller.yaml
vim $Z/dts/bindings/serial/st,stm32-uart-base.yaml
```

### Where are pinmuxes defined?
In the pinctrl file we chose earlier.

```
~/zephyrproject/modules/hal/stm32/dts/st/f4/stm32f405zgtx-pinctrl.dtsi
```
* manufacturer specific macro stuff, grep "define STM32_PINMUX" and "define PIN_NO" if questions.

## Why devmem?
Devmem: read and write register values by hand instead of using software abstraction!
But why?

* What if you need an option that is not in the shell GPIO i/o/h/l toggles
* Try some pull-up strength, speed settings, for signal integrity or EMC
For instance, slew-rate, in bindings
```
/dts/bindings/pinctrl/st,stm32-pinctrl.yaml
```
```
GPIOx_OSPEEDR
GPIOC: 40020800
```
* Register map page 285: Address offset: 0x08 for OSPEEDR
* 0 by default
* 0x2000 0000 for high speed offset 14
