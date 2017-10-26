raw_temp_data = '04 00 ad 27 01 11 31'
raw_temp_bytes = raw_temp_data.split()
raw_ambient_temp = int( '0x'+ raw_temp_bytes[3]+ raw_temp_bytes[2], 16)
ambient_temp_int = raw_ambient_temp >> 2 & 0x3FFF
ambient_temp_celsius = float(ambient_temp_int) * 0.03125
print ambient_temp_celsius
