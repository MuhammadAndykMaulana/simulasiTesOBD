import json, requests
from pprint import pprint
import random

class Mil:
    def __init__(self,codes, items):
		self.code = codes
		self.item = items
		#self.area  = areas

MILS =[
    Mil("41", "Sirkuit Tekanan Absolute Manifold/Tekanan Barometric"),    
    Mil("42", "Sirkuit Intake Air Temperature Malfungsi"),    
    Mil("43", "Sirkuit Temperature Cairan Pendingin Mesin"),    
    Mil("31", "Malfungsi Sirkuit Sensor Posisi Pedal (Throttle Position)/Switch A"),
    Mil("21", "Sirkuit Sensor Oksigen (Bank 1 Sensor 1)"),    
    Mil("23", "Sirkuit Heater Sensor O2 (Bank 1 Sensor 1)"),
    Mil("22", "Sirkuit Sensor Oksigen (Bank 1 Sensor 2)"),
    Mil("25", "Sistem Terlalu Kurus (Malfungsi A/F Kurus, Bank 1)"),
    Mil("26", "Sistem Terlalu Gemuk (Malfungsi A/F Kurus, Bank 1)"),
    Mil("18", "Sirkuit Sensor Knock 1"),
    Mil("13", "Malfungsi Sirkuit A Sensor Posisi Crankshaft"),
    Mil("14", "Sirkuit Sensor Posisi Charmshaft A (Bank 1 / Single Sensor)"),
    Mil("16", "Koil Pengapian A Utama / Sirkuit Sekunder"),
    Mil("76", "Malfungsi pada Sirkuit Purge Control Valve Sistem Evoparative Emission Control"),
    Mil("52", "Sensor Kecepatan Kendaraan"),
    Mil("71", "Sistem Kontrol Idle Malfungsi"),
    Mil("75", "Sensor VVT/Range Sirkuit sensor Posisi Camshaft/Problem Performance (Bank 1)"),
    Mil("73", "Malfungsi pada Sistem VVT (Bank 1)"),
    Mil("54", "Sirkuit Sinyal Starter"),
    Mil("51", "Sirkuit Switch A/C Malfungsi"),
    Mil("44", "Sistem Sinyal Sensor Temperature Evoparator Air Conditioner"),
    Mil("83", "Malfungsi pada Sirkuit Sinyal Immobiliser"),
    Mil("82", "Problem Komunikasi Serial antara ECU EFI dan ECU A/T"),
    Mil("74", "Malfungsi pada Sirkuit OCV(Bank 1)"),
    ]

def obj_dict(obj):
    return obj.__dict__
json_str = json.dumps((random.choice(MILS)), default=obj_dict)
#json_str = json.dumps(MILS, default=obj_dict)
#print json_str

#Alhamdulillah
#decoded=json.loads(json_str)
#pprint (decoded)
#print (decoded["item"][0])
#print (decoded[0]["code"])
#print (decoded["code"])
