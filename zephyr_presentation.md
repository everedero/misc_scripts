# HW Bring up
## Setup folder
* Start from a clean sample directory
Do all the setup gizmo in Readme

```
west init -m https://github.com/zephyrproject-rtos/example-application --mr main my-workspace
```
(Don’t git clone, it creates a weird path)

* update Zephyr modules
cd my-workspace
west update

* Try compilation
```
BOARD="custom_plank"
west build -b $BOARD app -- -DOVERLAY_CONFIG=debug.conf
```

* Find a similar board
```
grep -rnw ./ -e "stm32f40.*"
```

## Create our board
* Copy a board
```
cp -r ~/zephyrproject/zephyr/boards/st/stm32f4_disco/ ./boards/st
```

## Rename stuff
```
rename "s/stm32f4_disco/totoboard/g" ./*
grep -rnw ./ -i -e ".*stm32f4_disco"
sed -i 's/stm32f4_disco/totoboard/' totoboard.yaml
sed -i 's/stm32f4_disco/totoboard/' board.yml
```
Kconfig: BOARD_TOTOBOARD instead of BOARD_STM32F4_DISCO
(+ docs)

Not mandatory: compatible = "st,totoboard"

## Try new board
```
BOARD="totoboard"
west build -p always -b $BOARD app -- -DOVERLAY_CONFIG=debug.conf
```

* It looks for examplesensor, OK

## Import blinky
```
cp -r ~/zephyrproject/zephyr/samples/basic/blinky ./

west build -p always -b $BOARD blinky -- -DOVERLAY_CONFIG=prj.conf
```

Blinky OK

## Find correct chip
```
find ./ -name "stm32f407Xg.dtsi"
```
It is in : $Z/dts/arm/st/f4/stm32f4

```
:%s/f405/f407/g
```

```
find ./ -name "stm32f407v(e-g)tx-pinctrl.dtsi"
./modules/hal/stm32/dts/st/f4/stm32f407v(e-g)tx-pinctrl.dtsi
```

* Pincontrol file: check your board chip name (me: stm32f405vgtx-pinctrl because I have STM32F405VGT6)
+ wildcards for component name

* Also, board.yaml
```
grep -rnw ./ -e ".*stm32f407.*"
```

## Open schematics and find a LED
Orange LED: PC13

Usart -> Usart 6

Remove usart2, can busses, disable OTG

* In debug mode, we can read UART

## Config shell gpio
In blinky prj.conf:
```
CONFIG_SHELL=y
CONFIG_GPIO_SHELL=y
```

Unsure about the name? gpio shell or shell gpio?
```
west build -t menuconfig
```

* Log level for LED
Either put the logs on UART2 (zephyr,console=&usart2), or disable logs by modifying blinky sample
TODO UART2 read does not work

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

Or:
```
dtsh
tree --format NKYC
```

Or:

* Setup GPIOC 4 to active high output and set to 1
```
gpio conf gpio@40020800 4 oh0
gpio set gpio@40020800 4 1

gpio blink gpio@40020800 4 1
```

* Read GPIO
User button PC14
```
gpio conf gpio@40020800 14 i
gpio get gpio@40020800
```
1 if not pressed, 0 if pressed

```
gpio conf gpio@40020800 14 il
```
0 if not pressed: OK

* Misc config with devmem
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

Easy sample with input vs output
```
devmem 40020800 32
gpio conf gpio@40020800 4 oh0
devmem 40020800 32
```
-> See 00 (Input state) become 01 (Output mode)!

# I2C
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

```
CONFIG_I2C=y
CONFIG_I2C_SHELL=y
```

i2c scan i2c@40005800
2d 53 57

Page 64 / page 159: I2C adresses are 0x53 and 0x57 (7-bits)

Device identifier:
i2c read i2c@40005800 57 17 2

PE7
gpio get gpio@40021000 7

gpio conf gpio@40021000 7 o
gpio set gpio@40021000 7 1
-> Disables I2C device

Read I2C
```
i2c read i2c@40005800 53 0
```

## Bringup complex subsystem
### Display
Let’s say I made an advanced DTS
Switching back to

BOARD="st25dv_mb1283_disco"

For display, I added:
* SPI2 activation
* display driver using this SPI bus
* zephyr,display chosen to tell Zephyr where is the display
* header for some variables

Simple sample:
```
cp -r ~/zephyrproject/zephyr/samples/drivers/display/ ./
```

### USB
```
cp -r ~/zephyrproject/zephyr/samples/subsys/usb/testusb/ ./
west build -b $BOARD testusb -- -DOVERLAY_CONFIG=prj.conf
```

Observe:
NordicSemiconductor Zephyr testusb sample
