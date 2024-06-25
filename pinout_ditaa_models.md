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

<!--
                                                                         CN7

                                                                       +-------+
                                                                   D16 | 1 | 2 | D15
                                                                       |   |   |
                                                                   D17 | 3 | 4 | D14
                                                                       |   |   |
                                                                   D18 | 5 | 6 | AREF
                    CN8                                                |   |   |
                                                                   D19 | 7 | 8 | GND
                  +-------+                                            |   |   |
               NC | 1 | 2 | D43                                    D20 | 9 | 10| D13
                  |   |   |                                            |   |   |
            IOREF | 3 | 4 | D44                                    D21 | 11| 12| D12
                  |   |   |                                            |   |   |
            RESET | 5 | 6 | D45                                    D22 | 13| 14| D11
                  |   |   |                                            |   |   |
              3V3 | 7 | 8 | D46                                    D23 | 15| 16| D10
                  |   |   |                                            |   |   |
               5V | 9 | 10| D47                                    D24 | 17| 18| D9
                  |   |   |                                            |   |   |
              GND | 11| 12| D48                                    D25 | 19| 20| D8
                  |   |   |                                            |   |   |
              GND | 13| 14| D49                                        +-------+
                  |   |   |
              VIN | 15| 16| D50                                        +-------+
                  |   |   |                                      AVDD  | 1 | 2 | D7
                  +-------+                                            |   |   |
                                                                 AGND  | 3 | 4 | D6
                  +-------+                                            |   |   |
              A0  | 1 | 2 | D51                                   GND  | 5 | 6 | D5
                  |   |   |                                            |   |   |
              A1  | 3 | 4 | D52                                    A6  | 7 | 8 | D4
                  |   |   |                                            |   |   |
              A2  | 5 | 6 | D53                                    A7  | 9 | 10| D3
                  |   |   |                                            |   |   |
              A3  | 7 | 8 | D54                                    A8  | 11| 12| D2
                  |   |   |                                            |   |   |
              A4  | 9 | 10| D55                                    D26 | 13| 14| D1
                  |   |   |                                            |   |   |
              A5  | 11| 12| GND                                    D27 | 15| 16| D0
                  |   |   |                                            |   |   |
              D72 | 13| 14| D56                                    GND | 17| 18| D42
                  |   |   |                                            |   |   |
              D71 | 15| 16| D57                                    D28 | 19| 20| D41
                  |   |   |                                            |   |   |
              D70 | 17| 18| D58                                    D29 | 21| 22| GND
                  |   |   |                                            |   |   |
              D69 | 19| 20| D59                                    D30 | 23| 24| D40
                  |   |   |                                            |   |   |
              D68 | 21| 22| D60                                    D31 | 25| 26| D39
                  |   |   |                                            |   |   |
              GND | 23| 24| D61                                    GND | 27| 28| D38
                  |   |   |                                            |   |   |
              D67 | 25| 26| D62                                    D32 | 29| 30| D37
                  |   |   |                                            |   |   |
              D66 | 27| 28| D63                                    D33 | 31| 32| D36
                  |   |   |                                            |   |   |
              D65 | 29| 30| D64                                    D34 | 33| 34| D35
                  |   |   |                                            |   |   |
                  +-------+                                            +-------+

                  CN9                                                  CN10
-->
![Kroki generated PlantUML](https://kroki.io/ditaa/svg/eNrNmEGOgzAMRfecIvtqpDiOk7BEIM2OZU_Tw49NW5pIncqtYmaQvCvm5ffHP-Bcp2te8zB06nX6ul6nHg0XSO7igCtwLUC9KC_36kOZuRlyxY0y_lPKws2IK_3ScF7LHxOO3Ey0LE8b7tbqQrjOtbUiqgiD5x8LJXj5p3F48cBeOlbWilFHKcsC4ApCGY6hvFmLKUlHKcIDckWhBGtKPOPDXkyZdJRyExBXEkpvriWda4vFrKMUe0DmKnzTaA35vS61w2LRQYpDYOQdJysrB0HeDRbHHhH2egvsPiHf9WHvybEPtWw-RD9Ptn2mJWvIyTeiECh6iXfqkUbWZp2gEYWCptmUXDPRzCFDK4oqM6fs6oFmHpkTNqKQKjKn4uqBZp6YU2xEIWVipiYxzSGpFmXbEhrIXA9C87xccnOMIFWq36Lhnpcx2FNCEw_KVC91YEawp_S1LKSMdbFxYJeEq0vMKdNYy0KqXF9QlhbYJmE7DNj7MpVKliV5HeUWU2yTIDbBgw5yuywJ9LsnsE2C2ASLvZa5liUFnZYyGALbBLfcyfaUqZYl6d4oUTIf2SYoNsFkT0m1LEn3RolyKkG2CYpNkI54o_zoEPg4Tg_PPnCM7u1rXsH_AN1nAPo=)
