import subprocess
import sys, time, datetime
import json, requests
from utils import *
from utils import scanSerial
from utils import getId
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

from MIL import *
from MIL import MILS
import paho.mqtt.client as mqtt
from obd_sensors import SENSORS
from obd_sensors import *
from pprint import pprint

"""
def jdefault(o):
	return o.__dict__
OBD=json.dumps(SENSORS, default=jdefault)
"""	
def getTime():
    dateString = "%d/%m/%Y,%H:%M:%S"
    return datetime.datetime.now().strftime(dateString)

def getGPS():
	gpspipe= "timeout 10s gpspipe -w -n 10 |  grep -m 1 speed"
	p = subprocess.Popen(gpspipe, stdout = subprocess.PIPE, shell = True)
	return p.communicate()[0]

def on_connect(mqttc, userdata, rc):
    print("Connected with result code "+str(rc))
    if rc!=0 :
       mqttc.reconnect()

def on_publish(mqttc, userdata, mid):
    print "Published"

def on_disconnect(mqttc, userdata, rc):
    if rc != 0:
       print("Unexpected disconnection. Reconnecting...")
       mqttc.reconnect()
    else :
       print "Disconnected successfully"
# Setup MQTT
broker = '202.182.58.202'
broker_port=1883

# Create a client instance
mqttc=mqtt.Client(client_id="00000000439a2140")
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_disconnect = on_disconnect


mqttc.connect(broker, broker_port, 60)
print("Connected to the server 202.182.58.202")

while 1:
		OBD=json_string	
		iD=getId()
		waktu=getTime()
		gpsData=getGPS()
		mil=json_str

		class DATA:

			def __init__ (self, ID, time, OBDData, Mil, GPSpipe):
						self.id=ID
						self.Time=time
						self.OBDSupported=OBDData
						self.CheckEngine=Mil
						self.gps=GPSpipe

		Data=DATA(iD, waktu, OBD, mil, gpsData)
		msg=json.dumps(vars(Data), sort_keys=True, indent=4)
		#print(msg)
		"""
		decode=json.loads(msg)
		pprint (decode)
		print(decode["id"])
		print(decode["Time"])
		p=json.loads(decode["gps"])
		print p["lat"]
		OBD=json.loads(decode['OBDSupported'])
		print (OBD[0]["name"]+":"+OBD[0]["value"])
		m=json.loads(decode["CheckEngine"])
		print (m["code"]+":"+m["item"])
				
		
		decode=json.loads(msg)
		
		OBD=json.loads(decode['OBDSupported'])
		value=OBD[0]["value"]
		print(value)
		"""
		try:
				topic = "carmonitoring"
				payload = msg
				print "Publishing JSON Format on topic: " + topic + " with message " + payload
				mqttc.publish(topic, payload, 0)
				time.sleep(5)

		except Exception as e:
			print "exception"
			log_file=open("log.txt","w")
			log_file.write(str(time.time())+" "+e.__str__())
			log_file.close()

			mqttc.disconnect()
			print ""
			time.sleep(3)  
		

#mqttc.loop_forever()

