import serial
import platform

def scanSerial():
    """scan for available ports. return a list of serial names"""
    available = []
 # Enable USB connection
    for i in range(256):
      try:
        s = serial.Serial("/dev/ttyUSB"+str(i)) #indeed /dev/ttyS, /dev/ttyACM, /dev/ttyd
        available.append(s.portstr)
        s.close()   # explicit close 'cause of delayed GC in java
      except serial.SerialException:
        pass
 # Enable Bluetooh connection (optional)
    for i in range(10):
      try:
		s = serial.Serial("/dev/rfcomm"+str(i))
		available.append( (str(s.port)))
		s.close()   # explicit close 'cause of delayed GC in java
      except serial.SerialException:
		pass
    return available
	
def getId():
    iD = "0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6]=='Serial':
                iD = line[10:26]
        f.close()
    except:
        iD = "ERROR00000000000"
        f.close()
    return iD