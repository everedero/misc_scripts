# SPI CC2500 remote control protocol

## Overview
The Tiani 2 remote includes a TI MSP430G2452 as a microcontroller and the TI CC2500 as a 2.4 GHz proprietary RF transceiver and its CC2591 range extender.

According to datasheet, it is also compatible with Oden 2 and Lyla 2 devices.

This describes the SPI control between microcontroller and transceiver.

SPI clock is around 140 kHz (maximum) with irregular clock.

## TX data
TX data packages has 9 bytes:

```
|7F  01  00  A5 | 08  08 | 00  00 | 01 | 05 |
| HEADER        | ACC    | zeros  | M  | S  |
```

With:

* M: mode (0x00 to 0x07, 0x00 is deactivate, or wait for instruction?)
* S: strength (0x01 to 0x0F)
* ACC: accelerometer data

#### Control mode 1
In mode 1, acceleremoter data controls the motor through device tilting.
0 degrees tilting is minimum, 90 degrees is maximum.

* 0 point is:

    28 28

* Max ACC value is:

    64 64

For some reason it is a doubled byte.

#### Control mode 2
In mode 2, accelerometer controls the motor though acceleration and movement.

It seems like S = 10

#### Control mode 3
In mode 3, standard button mode is activated.
* Modes go from 1 to 7, middle button allow to circle between modes.
* Strength is controlled by buttons + and -.

### TX data sending
We send a short packet without M and S, and then a long packet with M and S.

We wait 54 ms between each TX.

For each send:
```
// 54 ms
36 [0F]: Idle mode
80 00 [00 5C]
7F 01 00 A5 28 28 00 00
06 07: set TX pack len to 7
35: activate STX
80 00 [40 5C]
// 1ms
80 00 [20 5C]
3B: SFTX, flush TX fifo buffer
36: Idle
34 [0F]: SRX (perform calibration first?)
36 [4F]: Idle (with status 4F: recalibration)
```
Showing only MOSI commands. When useful, we put MISO between brackets [].

## Initialisation
Most MISO bytes are status bytes, 0x0F means:
* STATE[7] = 0: chip ready
* STATE[6:4] = 0x0: IDLE state
* STATE[3:0] = 0xF: 16 bytes free in TX FIFO

0x10 is:
* STATE[6:4] = 0x1: RX Receive mode
* STATE[3:0] = 0x0: 0 bytes available in RX FIFO

```
30 // SRES Reset chip
0B 0A
0C 00
0D 5D
0E 13
0F B1
10 2D
11 3B
12 73
13 22
14 F8
0A 00
15 00
21 B6
22 10
18 18 // FS_AUTOCAL=1, automatically recalibrate from IDLE to TX/RX
19 1D
1A 1C
1B C7
1C 00
1D B0
23 EA
24 0A
25 00
26 11
29 59
2C 88
2D 31
2E 0B
00 5C
02 5B
07 0A
08 04
09 01
06 09 // Set pkt len for burst write
7E FF FF FF FF FF FF FF FF // Burst write PATABLE
8F FF [00 B1] // Read CHANNR (1-byte)
3A
3B
36 // IDLE
00 5C [0F 0F]
02 5B [0F 0F]
36 // IDLE
36 // IDLE
80 00 [00 5C] // IOCFG
0A 01 [0F 0F] // CHANNR
3A // SFRX Flush RX FIFO
3B // SFTX Flush TX FIFO
36 // IDLE
34 // SRX: switch to RX, calibration first
// 20 ms
A5 FF [10 1C] // Single byte read FSCAL1
F4 00 [10 CB] // Burst read RSSI?
F4 00 [10 CD]
[...]
```

We stay about 1 second in RX init mode, reading RSSI with:

    F4 00

## Behaviour

* The remote acts the same if device is connected or not connected.

```
80 00 [00 5C]
```

## Pinout

| MSP430 pin | Pin name | Use     | CC2500 pin | Note                  |
|------------|----------|---------|------------|-----------------------|
| 1          | DVCC     |         |            |                       |
| 2          | P1.0     |         |            |                       |
| 3          | P1.1     |         |            |                       |
| 4          | P1.2     |         |            |                       |
| 5          | P1.3     | SW1     |            | Active low            |
| 6          | P1.4     | SW3     |            | Active low            |
| 7          | P1.5     | SW2     |            | Active low            |
| 8          | P2.0     | SCLK    | 1          |                       |
| 9          | P2.1     | MOSI    | 20         |                       |
| 10         | P2.2     | MISO    | 2          |                       |
| 11         | P2.3     | R14     |            |                       |
| 12         | P2.4     | R13     |            |                       |
| 13         | P2.5     | CSn     | 7          | Active low            |
| 14         | P1.6     |         |            |                       |
| 15         | P1.7     |         |            |                       |
| 16         | RST      | TDI/TDO |            | Debug testpoint TDI/O |
| 17         | TEST     |         |            |                       |
| 18         | XOUT     |         |            |                       |
| 19         | XIN      |         |            |                       |
| 20         | DVSS     |         |            |                       |

No testpoints are available on the SPI bus, our best option here is to solder wires directly to the MSP430 TSSOP-20 pads.

SPI bus on P2 pins is strange. The datasheet states that SPI pins are:

| SPI | Pin  |
|-----|------|
| CLK | P1.5 |
| DO  | P1.6 |
| DI  | P1.7 |

My take on this: SPI is done via bitbanging instead of HW peripherals, explaining why the clock is irregular.
