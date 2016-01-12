import Adafruit_GPIO.FT232H as FT232H

# Temporarily disable FTDI serial drivers.
FT232H.use_FT232H()

# Find the first FT232H device.
ft232h = FT232H.FT232H()

#gyro defines - ST L3G2
L3G_CTRL_REG1 = 0x20
L3G_CTRL_REG2 = 0x21
L3G_CTRL_REG3 = 0x22
L3G_CTRL_REG4 = 0x23
L3G_CTRL_REG5 = 0x24
L3G_OUT_X_L = 0x28
L3G_WHO_AM_I = 0x0F
L3G_I2C_ADDR = 0x69
 
print 'Scanning all I2C bus addresses...'
# Enumerate all I2C addresses.
for address in range(127):
    # Skip I2C addresses which are reserved.
    if address <= 7 or address >= 120:
        continue
    # Create I2C object.
    i2c = FT232H.I2CDevice(ft232h, address)
    # Check if a device responds to this address.
    if i2c.ping():
        print 'Found I2C device at address 0x{0:02X}'.format(address)
        
 
print 'Done!'

gyro = FT232H.I2CDevice(ft232h,L3G_I2C_ADDR)

whoAmI = gyro.readU8(L3G_WHO_AM_I)

print format(whoAmI,'02x')
