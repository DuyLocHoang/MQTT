
import paho.mqtt.client as mqtt
from Store_Data_to_Sqlite3 import sensor_Data_Handler

# MQTT Settings
MQTT_Broker = "192.168.100.23"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic1 = "Control_Nutrition"
MQTT_Topic2 = "Control_Water"

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code "+str(rc))
    client.subscribe(MQTT_Topic1)
    client.subscribe(MQTT_Topic2)

#Save Data 
def on_message(client, userdata, msg):
    print "MQTT Data Received..."
    print "MQTT Topic: " + msg.topic
    print "Data: " + msg.payload
    sensor_Data_Handler(msg.topic, msg.payload)

client = mqtt.Client()

client.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
client.on_message = on_message
client.on_connect = on_connect

client.loop_forever()
