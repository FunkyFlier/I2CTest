import Adafruit_GPIO.FT232H as FT232H
import struct
import time

from datetime import datetime
from datetime import timedelta
from math import floor

print (timedelta.resolution)
# Temporarily disable FTDI serial drivers.
FT232H.use_FT232H()

# Find the first FT232H device.
ft232h = FT232H.FT232H()

startTime = datetime.now()
#print time.get_clock_info('clock')

def millis():
   return floor(time.clock() * 1000)
def micros():
    return floor(time.clock() * 1000000)
def nanos():
    return floor(time.clock() * 1000000000)
X_ = 0
Y_ = 1
Z_ = 2

#gyro defines - ST L3G2
READ = 0x80
for x in range(10000):
    #print time.clock()
    #print floor(time.clock() * 1000000)
    print time.clock()
    print nanos()
    print millis()
    print micros()
    
    
L3G_CTRL_REG1 = 0x20
L3G_CTRL_REG2 = 0x21
L3G_CTRL_REG3 = 0x22
L3G_CTRL_REG4 = 0x23
L3G_CTRL_REG5 = 0x24
L3G_OUT_X_L = 0x28
L3G_WHO_AM_I = 0x0F
L3G_I2C_ADDR = 0x69
 
# print 'Scanning all I2C bus addresses...'
# # Enumerate all I2C addresses.
# for address in range(127):
#     # Skip I2C addresses which are reserved.
#     if address <= 7 or address >= 120:
#         continue
#     # Create I2C object.
#     i2c = FT232H.I2CDevice(ft232h, address)
#     # Check if a device responds to this address.
#     if i2c.ping():
#         print 'Found I2C device at address 0x{0:02X}'.format(address)
#          
#   
# print 'Done!'
gyro = FT232H.I2CDevice(ft232h,L3G_I2C_ADDR)

whoAmI = gyro.readU8(L3G_WHO_AM_I)
format(whoAmI,'02x')
print (bin(whoAmI))

gyro.write8(L3G_CTRL_REG2, 0x00)
gyro.write8(L3G_CTRL_REG3, 0x00)
gyro.write8(L3G_CTRL_REG4, 0x20)
gyro.write8(L3G_CTRL_REG5, 0x02)
gyro.write8(L3G_CTRL_REG1, 0x8F)

# xVal1 = gyro.readU8(L3G_OUT_X_L | READ)
# xVal2 = gyro.readU8(L3G_OUT_X_L+1 | READ)
#                      
# print bin(xVal1),",",bin(xVal2)

# print format(L3G_OUT_X_L | READ,'02x')

xVal3 = gyro.readS16(L3G_OUT_X_L | READ, True)
# print xVal3
#  
# print bin(xVal3)
# 
gyroByteList = gyro.readList(L3G_OUT_X_L | READ, 6)

print (format(gyroByteList[0],'02x'))
print (format(gyroByteList[1],'02x'))
print (format(gyroByteList[2],'02x'))

gyroIntList = struct.unpack('hhh',gyroByteList[0:6])
print (gyroIntList)


xGyro = gyroIntList[0]
yGyro = gyroIntList[1]
zGyro = gyroIntList[2]

print (xGyro,",",yGyro,",",zGyro)





























