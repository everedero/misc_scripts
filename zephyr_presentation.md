# HW Bring up

## Setup folder
(Takes > 2 minutes, pre-download)

* Start from a clean sample directory

Do all the setup gizmo in Readme
```
west init -m https://github.com/zephyrproject-rtos/example-application --mr main my-workspace
```
(Don’t git clone, it creates a weird path)

* update Zephyr modules
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
Board folder:
```
tree -L 3 boards/
```

* Find a similar board dts to copy
Copy a board, to have presets and example configs

SoC: STM32F405
But we can take an exemple from the same SoC series, and change SoC, for the demo
```
cd $Z/boards
grep -rnw ./ -e "name: stm32f40.*"
```
* stm32f4 disco (not the right SoC, we’ll change it)
```
cp -r $Z/boards/st/stm32f4_disco/ ./boards/st
```

## Rename stuff
```
rename "s/stm32f4_disco/totoboard/g" ./*
grep -rnw ./ -i -e ".*stm32f4_disco"
sed -i 's/stm32f4_disco/totoboard/' totoboard.yaml
sed -i 's/stm32f4_disco/totoboard/' board.yml
sed -i 's/STM32F4_DISCO/TOTOBOARD/' Kconfig.totoboard
```
* Remove docs folder, for later

Not mandatory but nice: compatible = "st,totoboard", model description

## Try new board
```
BOARD="totoboard"
west build -p always -b $BOARD app
```

* It looks for examplesensor0, not here in our dts

## Import blinky
```
cp -r $Z/samples/basic/blinky ./

west build -p always -b $BOARD blinky
```

* While it builds -> some explanations about device tree "zephyr,led0", open the blinky.c source
```
vim $Z/samples/basic/blinky/src/main.c
```

## Find correct chip
Now time to actually modify the DTS file.
First, SoC selection.
```
find ./ -name "stm32f407Xg.dtsi"
```
It is in : $Z/dts/arm/st/f4/stm32f4
```
stm32f405Xg.dtsi
```

```
find ../ -name "stm32f407v(e-g)tx-pinctrl.dtsi"
./modules/hal/stm32/dts/st/f4/stm32f407v(e-g)tx-pinctrl.dtsi
```

* Pincontrol file: check your board chip name (me: stm32f405vgtx-pinctrl because I have STM32F405VGT6)
+ wildcards for component name

* Also, board.yaml
```
grep -rnw ./ -e ".*stm32f407.*"
```

## Clock frequency
Check the main clock
* OSC\_IN -> NX3225GD-8MHZ
* HSE is 8 MHz in DTS
* Look, a nice macro to avoid writing lots of zeros (in $Z/dts/common)

## Open schematics and find a LED + UART
* Orange LED: PC13 Active HIGH
* Blue button: PC14 Active LOW
* Rapid pull-up / pull-down check on schematics

* Usart -> Usart 6
* PC6/USART6\_TX
* PC7/USART6\_RX

* Remove can busses, disable OTG
* Change zephyr,shell to usart6

```
west build -p always -b $BOARD blinky
```

## Results

* Build and flash: see blinky and blinky msg.

## Config shell gpio
```
tree -L 2 blinky
```
prj.conf: selects what will be build

In blinky prj.conf, add:
```
CONFIG_SHELL=y
CONFIG_GPIO_SHELL=y
```

Unsure about the name? gpio shell or shell gpio?
```
west build -t menuconfig
```

* Log level for LED
Either put the logs on UART2 (zephyr,console=&usart2), or disable logs by modifying blinky sample.

* PA2/USART2\_TX, PA3/USART2\_RX (already set as default)
Works with the uart-usb adapter.
Pinout:
* Yellow = GND
* Green TXD = pin 3
* Blue RXD = pin 4

## Use shell GPIO
```
gpio help
gpio info
```

* Yellow: PC4
```
gpio conf
```

Gpio referenced by addresses, not nice names! So, tip:

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
* Misc config with devmem

Devmem: read and write register values by hand instead of using software abstraction!
But why?

* What if you need an option that is not in the shell GPIO i/o/h/l toggles
* Try some pull-up strength, speed settings, for signal integrity or EMC

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

#### Exemple setting not in shell
TODO: Remove or not?
For instance, slew-rate, in bindings
```
/dts/bindings/pinctrl/st,stm32-pinctrl.yaml
```
```
GPIOx_OSPEEDR
GPIOC: 40020800
```
Page 285: Address offset: 0x08 for OSPEEDR
0 by default
0x2000 0000 for high speed offset 14

## I2C shell
* Output connector I2C:
```
PB10/I2C2_SCL
PB11/I2C2_SDA
```
* From boards/st/nucleo_f411re/nucleo_f411re.dts:
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

TODO Talk about what when it builds: menuconfig again, i2c driver setup in dts, Linux/RPi i2cget/i2cset equivalents?

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
About spi shell: someone named Benner has an opened PR
It will look like this:

```
uart:~$ spi transceive spi@40013000 49 0
```

## Clock tree config
Start crying?

SoC clock tree schem page 154.

    vim $Z/dts/bindings/clock/st,stm32f4-pll-clock.yaml

Maybe an RFC?

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
