import configparser
from time import localtime, strftime
import json
import paho.mqtt.client as mqtt

#
# Global variables
#
config = configparser.ConfigParser()
config.read('/home/pi/py.conf')     # Broker connection config.

requestTopic  = 'services/timeservice/request/+'        # Request comes in here. Note wildcard.
responseTopic = 'services/timeservice/response/'        # Response goes here. Request ID will be appended later


#
# Callback that is executed when the client receives a CONNACK response from the server.
#
def onConnect(client, userdata, flags, rc):
   print("Connected with result code " + str(rc))

   # Subscribe on request topic with a single-level wildcard.
   # Subscribing in on_connect() means that if we lose the connection and
   # reconnect then subscriptions will be renewed.
   client.subscribe(requestTopic, 0)    # topic, QoS


#
# Callback that is executed when a message is received.
#
def onMessage(client, userdata, message):
   requestTopic = message.topic
   requestID = requestTopic.split('/')[3]       # obtain requestID as last field from the topic

   print("Received a time request on topic " + requestTopic + ".")


   # Get and format the local time
   lTime = strftime('%H:%M:%S', localtime())

   # Publish the time to the response topic
   client.publish((responseTopic + requestID), payload=lTime, qos=0, retain=False)


#
# Callback that is executed when we disconnect from the broker.
#
def onDisconnect(client, userdata, message):
    print("Disconnected from the broker.")


#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------


# Create MQTT client instance
mqttc = mqtt.Client(client_id='raspberrypi', clean_session=True)

mqttc.on_connect = onConnect
mqttc.on_message = onMessage
mqttc.on_disconnect = onDisconnect

# Connect to the broker
#mqttc.username_pw_set(config['MQTT']['userMQTT'], password=config['MQTT']['passwdMQTT'])
#mqttc.connect(config['MQTT']['hostMQTT'], port=int(config['MQTT']['portMQTT']), keepalive=60, bind_address="")

# Setup MQTT
broker = '202.182.58.202'
broker_port=1883

mqttc.connect(broker, broker_port, 60)




# This is a blocking form of the network loop and will not return until the client
# calls disconnect(). It automatically handles reconnecting.
mqttc.loop_forever()

# End
