import json, requests
import random
from pprint import pprint
#ob = Object()
class Sensor:
	#sensors_list=[]
	def __init__(self,sensorName, sensorValueFunction):
		#Sensor.sensors_list.append(self)
		self.name = sensorName
		self.value= sensorValueFunction
"""
SENSORS = [Sensor("CalcLoadValue", "36.1"),
           Sensor("CoolantTemp", "29"),
		   Sensor("IntakeManifoldPressure", 30),
		   Sensor("EngineRPM", "680"),
		   Sensor("VehicleSpeed", "70"),
		   Sensor("TimingAdvance", "2.5"),
		   Sensor("IntakeAirTemp", "26.3"),
		   Sensor("AirFlowRateMAF", "17"),
		   Sensor("ThrottlePosition", "15.29"),
		   Sensor("TimeSinceEngineStart", "57"),
		   Sensor("EngineRunwithMILon", "10")]


#ok=random.uniform(0.1, 10)
"""
#clv=["36.1","36.2","36.3","36.4","36.7","36.8","37.1","32.5","33.9"]
#CLV=random.choice(clv)

def clv():
	CLV=["29.8","33.6","30.7","36.1","67.1"]
	c=random.choice(CLV)
	return c

#print (clv())
def ct():
	CT=["203","201"]
	a=random.choice(CT)
	return a
def rpm():
	RPM=["610","605"]
	b=random.choice(RPM)
	return b
def maf():
	MAF=["0.17","0.18"]
	d=random.choice(MAF)
	return d

SENSORS = [Sensor("CLV", clv()),
           Sensor("CT", ct()),
		   Sensor("IMP", "30"),		   Sensor("ERPM", rpm()),
		   Sensor("VS", "70"),
		   Sensor("TA", "2.5"),
		   Sensor("IAT", "26.3"),
		   Sensor("MAF", maf()),
		   Sensor("TP", "15.29"),
		   Sensor("TSES", "57"),
		   Sensor("ERMON", "10")]

#print vars(SENSORS)
#print json.loads((SENSORS),sort_keys=True, indent=4)
def obj_dict(obj):
    return obj.__dict__

json_string = json.dumps(SENSORS, default=obj_dict)
#print (json_string)
#print (json_string)
#p=json.loads(json_string)
#pprint (p)
#print(SENSORS)
#print(p[0]["name"])
