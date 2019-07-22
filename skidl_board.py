#!/usr/bin/env python3
#
# SKiDL definition of the board
#

from skidl import *

class RpiConnector(Part):
    def __init__(self, ref=None, value=None,
                 footprint='Connector_PinHeader_2.54mm:PinHeader_2x20_P2.54mm_Vertical'):
        Part.__init__(self, 'Connector_Generic', 'Conn_02x20_Odd_Even',
                      ref=ref, value=value, footprint=footprint)
        self[1].name = '+3.3V'; self[1].drive = POWER
        self[2].name = '+5V'; self[2].drive = POWER
        self[4].name = '+5V'
        self[6].name = 'GND'; self[6].drive = POWER
        self[9].name = 'GND'
        self[14].name = 'GND'
        self[20].name = 'GND'
        self[25].name = 'GND'
        self[30].name = 'GND'
        self[34].name = 'GND'
        self[39].name = 'GND'

t_led = Part('Device', 'LED', footprint='LED_SMD:LED_0805_2012Metric_Castellated', dest=TEMPLATE)
t_r = Part('Device', 'R', value='390', footprint='Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder', dest=TEMPLATE)
t_c = Part('Device', 'C', footprint='Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder', dest=TEMPLATE)
t_tp = Part('Connector', 'TestPoint', footprint='TestPoint:TestPoint_THTPad_1.0x1.0mm_Drill0.5mm', dest=TEMPLATE)

# Global nets
vcc_33 = Net('+3.3V')
vcc_5 = Net('+5V')
vcc_reg = Net('VCC_reg')
gnd = Net('GND')

# Raspberry Pi connector
rpi_con = RpiConnector(ref='J1', value='Raspberry Pi')
rpi_con['+3.3V'] += vcc_33
rpi_con['+5V'] += vcc_5
rpi_con['GND'] += gnd
rpi_con[17, 26, 27, 28, 33, 35, 36, 37, 38, 40] += NC

# Serial port header
uart_header = Part('Connector_Generic', 'Conn_01x03', ref='J3',
                   footprint='Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical')
uart_header[:] += gnd, rpi_con[10], rpi_con[8]

# LEDs
vcc_33 & t_led(ref='D3')['A', 'K'] & t_r(ref='R3') & rpi_con[3]
vcc_33 & t_led(ref='D4')['A', 'K'] & t_r(ref='R4') & rpi_con[5]
vcc_33 & t_led(ref='D5')['A', 'K'] & t_r(ref='R5') & rpi_con[13]
rgb_led = Part('LED', 'ASMB-MTB0-0A3A2', ref='D1', footprint='LED_SMD:LED_Avago_PLCC4_3.2x2.8mm_CW')
rgb_led[1] += vcc_33
rgb_led[2] & t_r(ref='R6', value='390') & rpi_con[32]
rgb_led[3] & t_r(ref='R7', value='390') & rpi_con[31]
rgb_led[4] & t_r(ref='R8', value='390') & rpi_con[29]

# One-wire headers
onewire = Net('onewire')
onewire += rpi_con[7]
vcc_33 & t_r(ref='R1', value='4k7') & onewire
j2 = Part('Connector_Generic', 'Conn_01x03', ref='J2',
          footprint='Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical')
j4 = j2(ref='J4')
j2[:] += vcc_33, onewire, gnd
j4[:] += vcc_33, onewire, gnd

# IR receiver
ir = Part('Interface_Optical', 'TSOP382xx', ref='U2',
          footprint='OptoDevice:Vishay_MINICAST-3Pin')
ir[:] += rpi_con[12], gnd, vcc_33
gnd & t_c(ref='C3', value='1u') & vcc_33

# IR transmitter
irled = Part('LED', 'CQY99', ref='D2', footprint='LED_THT:LED_D5.0mm_IRGrey')
# Note: I'm suspicious of this being the correct transistor
t = Part('Transistor_BJT', 'DTA123E', value='PDTC123Y', ref='Q1', footprint='Package_TO_SOT_SMD:SC-59_Handsoldering')
vcc_5 & irled['A', 'K'] & t_r(ref='R2', value=70) & t['C', 'E'] & gnd
t['B'] += rpi_con[11]

# LDO
ldo = Part('Regulator_Linear', 'AP2204K-3.3', ref='U1',
           footprint='Package_TO_SOT_SMD:SOT-23-5')
ldo['VIN', 'EN'] += vcc_5
ldo['GND'] += gnd
ldo['VOUT'] += vcc_reg
gnd & t_c(ref='C1', value='1u') & vcc_5
gnd & t_c(ref='C2', value='10u') & vcc_reg
vcc_reg += t_tp(ref='TP7')[1]

# RF module
rfm = Part('RF_Module', 'RFM69HCW', ref='U3', footprint='RF_Module:HOPERF_RFM69HW')
ant1 = Part('Device', 'Antenna_Shield', ref='AE1', value='SMA', footprint='Connector_Coaxial:SMA_Amphenol_132289_EdgeMount')
ant2 = Part('Device', 'Antenna_Shield', ref='AE2', value='U.Fl', footprint='Connector_Coaxial:U.FL_Hirose_U.FL-R-SMT-1_Vertical')
rfm['GND'] += gnd
rfm['3.3V'] += vcc_reg
rfm['SCK'] += rpi_con[23]
rfm['MOSI'] += rpi_con[19]
rfm['MISO'] += rpi_con[21]
rfm['NSS'] += rpi_con[24]
rfm['RESET'] += rpi_con[15]
rfm['DIO0'] += rpi_con[22] | t_tp(ref='TP6')
rfm['DIO1'] += rpi_con[18] | t_tp(ref='TP5')
rfm['DIO2'] += rpi_con[16] | t_tp(ref='TP4')
rfm['DIO3'] += t_tp(ref='TP3')[1]
rfm['DIO4'] += t_tp(ref='TP2')[1]
rfm['DIO5'] += t_tp(ref='TP1')[1]
rfm['ANT'] += Net('ant') | ant1[1] | ant2[1]
gnd += ant1['Shield'] | ant2['Shield']
gnd & t_c(ref='C4', value='10u') & vcc_reg

# Sundry
Part('Mechanical', 'MountingHole', ref='H1', footprint='holes:hole_2.75')
Part('Mechanical', 'MountingHole', ref='H2', footprint='holes:hole_2.75')
Part('Mechanical', 'MountingHole', ref='H3', footprint='holes:hole_2.75')
Part('Mechanical', 'MountingHole', ref='H4', footprint='holes:hole_2.75')

# Finalize
ERC()
generate_netlist()
