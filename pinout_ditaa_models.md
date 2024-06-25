# Models for pinout drawings in Ditaa format
* See raw text file for ASCII versions (in comments)
* See kroki.io to get the pretty printed image version

## NRF52DK
<!--

                                                            +----+
                                                    P0.27   | 10 |
                                                            |    |
                                                    P0.28   | 9  |
                                                            |    |
                                                    P0.02   | 8  |
        o                                                   |    |
     +---+                                          GND     | 7  |
     | 1 | VDD                                              |    |
     |   |                                          P0.25   | 6  |
     | 2 | VDD                                              |    |
     |   |                                          P0.24   | 5  |
     | 3 | RESET                                            |    |
     |   |                                          P0.23   | 4  |
     | 4 | VDD                                              |    |
     |   |                                          P0.22   | 3  |
     | 5 | 5V                                               |    |
     |   |                                          P0.20   | 2  |
     | 6 | GND                                              |    |
     |   |                                          P0.19   | 1  |
     | 7 | GND                                              |    |
     |   |                                                  +----+
     | 8 | NC                                                 o
     |   |                                                   P4
     +---+
      P1                                                    +----+
        o                                           P0.18   | 8  |
     +---+                                                  |    |
     | 1 | P0.03                                    P0.17   | 7  |
     |   |                                                  |    |
     | 2 | P0.04                                    P0.16   | 6  |
     |   |                                                  |    |
     | 3 | P0.28                                    P0.15   | 5  |
     |   |                                                  |    |
     | 4 | P0.29                                    P0.14   | 4  |
     |   |                                                  |    |
     | 5 | P0.30                                    P0.13   | 3  |
     |   |                                                  |    |
     | 6 | P0.31                                    P0.12   | 2  |
     |   |                                                  |    |
     +---+                                          P0.11   | 1  |
                                                            |    |
                                                            +----+
                                                              o
                                                             P3

                                                            +----+
                                                    P0.10   | 9  |
                                                            |    |
                                                    P0.09   | 8  |
                                                            |    |
                                                    P0.08   | 7  |
                                                            |    |
                                                    P0.07   | 6  |
                                                            |    |
                                                    P0.06   | 5  |
                                                            |    |
                                                    P0.05   | 4  |
                                                            |    |
                                                    P0.21   | 3  |
                                                            |    |
                                                    P0.01   | 2  |
                                                            |    |
                                                    P0.00   | 1  |
                                                            |    |
                                                            +----+
                                                              o
                                                             P6

-->

![Kroki generated PlantUML](https://kroki.io/ditaa/svg/eNrtl82OgyAURvc-BXszE_7RdW1m15iZSV_DF-DhC5RWBrpAINxZlASNi_vlyNUjDqhijB9mjENJ6Yo_qTJnjQhGeqih0O5QTDG5iBmBUmDqIqYwYquksN0Z80u_LouPUM8I0x0zr8tSTqEf1_kdEa5EBhEUgIK7EhFEMDO_zz_n344UzJXwIIIDrAX1979HCDuvqCsF9s_CHiHNfDy3nSjI7N-LPUJ1pnilX-sOjS6nwyFbFQJaeSAbr66VNPiYbMcESqZIoAft97ot1n7WziyXQiUCLVrWvxTUU_BcCpkItAEFu1O472UWhUgE2oCCe4o5l4InAm1AIe4UDOdSsESgDSikpyC5FDQRaDXFwdfMUpBIoP03XA32r4lAS8fKBqh7sM3A_2L3O6e7XwCKKZI3DIWK5A1DISN5w1CISN4wf4gkkjfMWpBI3jAU-C3vcEXkDZkJeKo=)

## ESP32-WROOM
<!--

            +-----+       +------------------+       +-----+
            | 3V3 |       |                  |       | GND |
            |     |       |                  |       |     |
            | EN  |       |                  |       | 23  |
            |     |       |                  |       |     |
            | VP  |       |    ESPRESSIF     |       | 22  |
            |     |       |                  |       |     |
            | VN  |       |    ESP32-WROOM   |       | TX  |
            |     |       |                  |       |     |
            | 34  |       |                  |       | RX  |
            |     |       |                  |       |     |
            | 35  |       |                  |       | 21  |
            |     |       |                  |       |     |
            | 32  |       |                  |       | GND |
            |     |       |                  |       |     |
            | 33  |       +------------------+       | 19  |
            |     |                                  |     |
            | 25  |                                  | 18  |
            |     |                                  |     |
            | 26  |                                  | 5   |
            |     |                                  |     |
            | 27  |                                  | 17  |
            |     |                                  |     |
            | 14  |                                  | 16  |
            |     |                                  |     |
            | 12  |                                  | 4   |
            |     |                                  |     |
            | GND |                                  | 0   |
            |     |                                  |     |
            | 13  |                                  | 2   |
            |     |                                  |     |
            | D2  |                                  | 15  |
            |     |                                  |     |
            | D3  |                                  | D1  |
            |     |                                  |     |
            | CMD |                                  | D0  |
            |     |                                  |     |
            | 5V  |                                  | CLK |
            |     |                                  |     |
            +-----+                                  +-----+
-->

![Kroki generated PlantUML](https://kroki.io/ditaa/svg/eNrFlssKgzAQRfd-xexFMDNG27WxpbQ-0GL7MX58W2mx0RJmcaF3EQgzh8MkBiRaEievxN7Oi1-Koy-WJpJRnutnt8lSOjaOpmhbU8HzuoKrRgmzENY8dquOauj6ahhOh7WZ0eZmaxZObn3b1h58vYPNkinhHm622ns2aDPTn75tkaUj8CQnMvvwzIH8NrNVwmaHNudK2BLaXGhnLsBmk2nNOdrMSjhDn_b8WDRwijYbUcKMNjvtaRuLNmtndgZsLmvlPbsUbLajEi4vZ6TZ_5UK5N34AGiqfao=)

## STM32 NUCLEO
144-pins female header connectors, such as in NUCLEO-F756ZG. [See manual](https://www.st.com/resource/en/user_manual/dm00244518-stm32-nucleo-144-boards-stmicroelectronics.pdf)

Be careful, eval kit pin names do not match logical pin names.
For instance, CN7-A0 header pin corresponds to PA3.

Logical pin names are indicated with parenthesis (PA3).

<!--
                                                                         CN7

                                                                       +-------+
                                                             (PC6) D16 | 1 | 2 | D15 (PB8)
                                                                       |   |   |
                                                            (PB15) D17 | 3 | 4 | D14 (PB9)
                                                                       |   |   |
                                                            (PB13) D18 | 5 | 6 | AREF
                    CN8                                                |   |   |
                                                            (PB12) D19 | 7 | 8 | GND
                  +-------+                                            |   |   |
               NC | 1 | 2 | D43 (PC8)                       (PA15) D20 | 9 | 10| D13 (PA5)
                  |   |   |                                            |   |   |
            IOREF | 3 | 4 | D44 (PC9)                        (PC7) D21 | 11| 12| D12 (PA6)
                  |   |   |                                            |   |   |
            RESET | 5 | 6 | D45 (PC10)                       (PB5) D22 | 13| 14| D11 (PA7)
                  |   |   |                                            |   |   |
              3V3 | 7 | 8 | D46 (PC11)                       (PB3) D23 | 15| 16| D10 (PD14)
                  |   |   |                                            |   |   |
               5V | 9 | 10| D47 (PC12)                       (PA4) D24 | 17| 18| D9 (PD15)
                  |   |   |                                            |   |   |
              GND | 11| 12| D48 (PD2)                        (PB4) D25 | 19| 20| D8 (PF12)
                  |   |   |                                            |   |   |
              GND | 13| 14| D49 (PG2)                                  +-------+
                  |   |   |
              VIN | 15| 16| D50 (PG3)                                  +-------+
                  |   |   |                                      AVDD  | 1 | 2 | D7 (PF13)
                  +-------+                                            |   |   |
                                                                 AGND  | 3 | 4 | D6 (PE9)
                  +-------+                                            |   |   |
       (PA3)  A0  | 1 | 2 | D51 (PD7)                             GND  | 5 | 6 | D5 (PE11)
                  |   |   |                                            |   |   |
       (PC0)  A1  | 3 | 4 | D52 (PD6)                        (PB1) A6  | 7 | 8 | D4 (PF14)
                  |   |   |                                            |   |   |
       (PC3)  A2  | 5 | 6 | D53 (PD5)                        (PC2) A7  | 9 | 10| D3 (PE13)
                  |   |   |                                            |   |   |
       (PF3)  A3  | 7 | 8 | D54 (PD4)                        (PF4) A8  | 11| 12| D2 (PF15)
                  |   |   |                                            |   |   |
       (PF5)  A4  | 9 | 10| D55 (PD3)                        (PB6) D26 | 13| 14| D1 (PG14)
                  |   |   |                                            |   |   |
       (PF10) A5  | 11| 12| GND                              (PB2) D27 | 15| 16| D0 (PG9)
                  |   |   |                                            |   |   |
              D72 | 13| 14| D56 (PE2)                              GND | 17| 18| D42 (PE8)
                  |   |   |                                            |   |   |
       (PA7)  D71 | 15| 16| D57 (PE4)                       (PD13) D28 | 19| 20| D41 (PE7)
                  |   |   |                                            |   |   |
       (PF2)  D70 | 17| 18| D58 (PE5)                       (PD12) D29 | 21| 22| GND
                  |   |   |                                            |   |   |
       (PF1)  D69 | 19| 20| D59 (PE6)                       (PD11) D30 | 23| 24| D40 (PE10)
                  |   |   |                                            |   |   |
       (PF0)  D68 | 21| 22| D60 (PE3)                        (PE2) D31 | 25| 26| D39 (PE12)
                  |   |   |                                            |   |   |
              GND | 23| 24| D61 (PF8)                              GND | 27| 28| D38 (PE14)
                  |   |   |                                            |   |   |
       (PD0)  D67 | 25| 26| D62 (PF7)                        (PA0) D32 | 29| 30| D37 (PE15)
                  |   |   |                                            |   |   |
       (PD1)  D66 | 27| 28| D63 (PF9)                        (PB2) D33 | 31| 32| D36 (PB10)
                  |   |   |                                            |   |   |
       (PG0)  D65 | 29| 30| D64 (PG1)                        (PE0) D34 | 33| 34| D35 (PB11)
                  |   |   |                                            |   |   |
                  +-------+                                            +-------+

                  CN9                                                  CN10
-->
![Kroki generated PlantUML](https://kroki.io/ditaa/svg/eNrNmM1u2zAQhO96Ch5rBAXEXf5IR9qUjFzcIi38NH747qzjlAIixq3FtAZ4sS1pNPx2diVjtvkcTrHrNjrX09fr5-mxE375fgg7k20wF2NlkaxsvXy_H3Zbab3cVveY1L310BrlZCzLqVaHH8b_UCtD6yAn87Lgb3qZ5u59LoZ_J5Mgc5STwVbIPZ5yV-FtE5WnQ8mbY3A47FZVJt146uXPUGp7bDwOSv69jb8U60Gtz99k00reHHg7jLtKQUVoxc1ZK4uglaA1NNb6Mv2Yfha8ZYc6Pth-3di9-opNsCzLQauF1thYqzF85gK67IJqtRWtKCjCQdbLCtDay_cSAc3FGn8u2XNRxVKFWAexIMZGWYMcNKpW31yr1G_JnhtwXaoAu1etoMaOUpG4QRwzy_19ktYbew4eHde13tf-1i52fj6V8HjAc-StLnafEemcsymzL6rTvGseuX_-SdidMvtQotPYTqqUDbYj9QuHPAIpx_o-vUp9iz4k3yRp0gxgqX_karILhzyCPodasUnCpWAW0acIuKZa1VdaWoQGmn2tk0klpmjK5GP1lVtqnVUrLyzy8Ci7itZZfkyDKZOP1FffVCvsS25hkQd7mWsMYOSmsOi6yKK2DMwYBJIvLdKq-WBAxHxIsQxOzc2xeW_IcTGXeE2fj3rDa0O59VwHBqahpa0JyZSjXbQWpPrk1seDrE8HNJQ914GBKTZFgFRrX1rk0esnX9OqCIBvEm6I1h4RtgMVKsNYmuMxGUyhplKOyoxbI0GGdJzoNa36ppb2KnYo3MlBr1tLAHCcWVucMENghvUOP23mejMpALt5uKuuSKAhQMMKTdu8yldnY2lS0EyPFWdTD2eRHCTssPYsrca2jSBfmQ2lSQHNcq49Kmq4MqYHFnYY7HDQIaEps8ers740KTjtQDVm1VmMOSzsMNhhfVHUcsx6dMb8Pbp37713Gf_mJZ7tu-4XR5NCcA==)
