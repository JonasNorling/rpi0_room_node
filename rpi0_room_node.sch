EESchema Schematic File Version 4
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "RPi0 room node"
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector_Generic:Conn_02x20_Odd_Even J?
U 1 1 5C2E2ED2
P 2250 3450
F 0 "J?" H 2300 4567 50  0000 C CNN
F 1 "Conn_02x20_Odd_Even" H 2300 4476 50  0000 C CNN
F 2 "" H 2250 3450 50  0001 C CNN
F 3 "~" H 2250 3450 50  0001 C CNN
	1    2250 3450
	1    0    0    -1  
$EndComp
$Comp
L RF_AM_FM:RFM69HCW U?
U 1 1 5C2E2FAC
P 9500 1850
F 0 "U?" H 9500 2528 50  0000 C CNN
F 1 "RFM69HCW" H 9500 2437 50  0000 C CNN
F 2 "" H 6200 3500 50  0001 C CNN
F 3 "http://www.hoperf.com/upload/rf/RFM69HCW-V1.1.pdf" H 6200 3500 50  0001 C CNN
	1    9500 1850
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Linear:AP2204K-3.3 U?
U 1 1 5C2E3418
P 8200 1600
F 0 "U?" H 8200 1942 50  0000 C CNN
F 1 "AP2210K-3.3" H 8200 1851 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23-5" H 8200 1925 50  0001 C CNN
F 3 "https://www.diodes.com/assets/Datasheets/AP2204.pdf" H 8200 1700 50  0001 C CNN
	1    8200 1600
	1    0    0    -1  
$EndComp
$Comp
L LED:CQY99 D?
U 1 1 5C2E374A
P 8400 4450
F 0 "D?" H 8350 4740 50  0000 C CNN
F 1 "CQY99" H 8350 4649 50  0000 C CNN
F 2 "LED_THT:LED_D5.0mm_IRGrey" H 8400 4625 50  0001 C CNN
F 3 "https://www.prtice.info/IMG/pdf/CQY99.pdf" H 8350 4450 50  0001 C CNN
	1    8400 4450
	1    0    0    -1  
$EndComp
$Comp
L Interface_Optical:TSOP323xx U?
U 1 1 5C2E38EB
P 8400 5600
F 0 "U?" H 8387 6025 50  0000 C CNN
F 1 "TSOP323xx" H 8387 5934 50  0000 C CNN
F 2 "OptoDevice:Vishay_MOLD-3Pin" H 8350 5225 50  0001 C CNN
F 3 "http://www.vishay.com/docs/82490/tsop321.pdf" H 9050 5900 50  0001 C CNN
	1    8400 5600
	1    0    0    -1  
$EndComp
$Comp
L LED:ASMB-MTB0-0A3A2 D?
U 1 1 5C2E3CE1
P 4850 5850
F 0 "D?" H 4850 6367 50  0000 C CNN
F 1 "ASMB-MTB0-0A3A2" H 4850 6276 50  0000 C CNN
F 2 "LED_SMD:LED_Avago_PLCC4_3.2x2.8mm_CW" H 4850 6350 50  0001 C CNN
F 3 "https://docs.broadcom.com/docs/AV02-4186EN" H 4850 5400 50  0001 C CNN
	1    4850 5850
	1    0    0    -1  
$EndComp
$Comp
L Device:Antenna AE?
U 1 1 5C2E3F7A
P 10550 1600
F 0 "AE?" H 10630 1591 50  0000 L CNN
F 1 "Antenna" H 10630 1500 50  0000 L CNN
F 2 "" H 10550 1600 50  0001 C CNN
F 3 "~" H 10550 1600 50  0001 C CNN
	1    10550 1600
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J?
U 1 1 5C2E426E
P 4800 2450
F 0 "J?" H 4880 2492 50  0000 L CNN
F 1 "Conn_01x03" H 4880 2401 50  0000 L CNN
F 2 "" H 4800 2450 50  0001 C CNN
F 3 "~" H 4800 2450 50  0001 C CNN
	1    4800 2450
	1    0    0    -1  
$EndComp
Text Notes 4600 2250 0    50   ~ 0
one-wire
$Comp
L Transistor_BJT:DTA123E Q?
U 1 1 5C2E45B7
P 8550 4750
F 0 "Q?" H 8737 4796 50  0000 L CNN
F 1 "PDTC123Y" H 8737 4705 50  0000 L CNN
F 2 "" H 8550 4750 50  0001 L CNN
F 3 "" H 8550 4750 50  0001 L CNN
	1    8550 4750
	1    0    0    -1  
$EndComp
$EndSCHEMATC
