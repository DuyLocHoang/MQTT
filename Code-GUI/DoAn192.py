import tkinter
from tkinter import *
import paho.mqtt.client as mqtt
import json
from datetime import datetime
MQTT_Broker = "192.168.100.21"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic_Control1 = "Control_Nutrition"
MQTT_Topic_Control3 = "Control_Water"

def on_connect(client, userdata, flags, rc):
    if rc == 0 :
        status_data.set("Connected")
    else :
        status_data.set("Not Connected")
    print("Connected With Result Code "+str(rc))
    print("Connecting to MQTT BROKER : {}".format(MQTT_Broker))

	

def on_message(client, userdata, message):
    print(message.topic + " Received: " + message.payload.decode())
    update_meters(message.topic, message.payload.decode())


def on_publish(client, userdata, rc):
    pass

def Pulish_To_Topic1(topic, message1,message2):
    message_dict = {}
    message_dict['Control_Pump1'] = message1
    message_dict['Control_Pump2'] = message2
    message_dict['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    message_json = json.dumps(message_dict)
    client.publish(topic,message_json)
    print("Published:" + str(message_json) + " " + "on MQTT Topic: " + str(topic))

def Pulish_To_Topic2(topic, message1):
    message_dict = {}
    message_dict['Control_Water'] = message1
    message_dict['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    message_json = json.dumps(message_dict)
    client.publish(topic,message_json)
    print("Published:" + str(message_json) + " " + "on MQTT Topic: " + str(topic))

def send_message2( en3):
    msg = en3.get()
    en3.delete(0,'end')
    Pulish_To_Topic2(MQTT_Topic_Control3,msg)

def send_message1( en1,en2):
    msg = en1.get()
    msg2 = en2.get()
    en2.delete(0,'end')
    en1.delete(0, 'end')
    Pulish_To_Topic1(MQTT_Topic_Control1,msg,msg2)

def quit_program(client):
    client.loop_stop()
    client.disconnect()
    print("Closed connection")
    exit()




def Controller_Data_Handler(jsonData):
    json_Dict = json.loads(jsonData)
    NutriA = json_Dict['NutriA']
    NutriB = json_Dict['NutriB']
    WaterIn = json_Dict['WaterIn']
    lab19_data.set(NutriA)
    lab20_data.set(NutriB)
    lab21_data.set(WaterIn)



def Sensor_Data_Handler(jsonData):

    json_Dict = json.loads(jsonData)
    PH = json_Dict['PH']
    Humidity = json_Dict['Humidity']
    EC = json_Dict['EC']
    CO2 = json_Dict['CO2']
    Light = json_Dict['Light']
    Temp = json_Dict['Temperature']
    Date_data1 = json_Dict['Date']
    Date_data.set(Date_data1)
    lab2_data.set(PH)
    lab5_data.set(EC)
    lab8_data.set(Temp)
    lab11_data.set(Humidity)
    lab14_data.set(CO2)
    lab17_data.set(Light)
 
def update_meters(topic, value):
    if topic == "Update_Data_Sensor":
        Sensor_Data_Handler(value)
    elif topic == "Updata_Data_Controller":
        Controller_Data_Handler(value)

    """Creates the Tkinter GUI and connects to the MQTT broker."""
iot=Tk()
iot.title("Do an 192")
iot.geometry("600x300")
#tạo label bên trái
lb1 = Label (iot, text = "Set", font =("consolas", 14, "bold"))
lb1.place (x = 130, y=10)

lb2 = Label (iot, text = "Pumped", font =("consolas", 14, "bold"))
lb2.place (x = 240, y=10)

lb3 = Label (iot, text = "Nutrition A", font =("consolas", 13, "bold"))
lb3.place (x = 6, y=40)

lb4 = Label (iot, text = "l", font =("consolas", 13, "bold"))
lb4.place (x = 180, y=40)

lb5 = Label (iot, text = "Nutrition B", font =("consolas", 13, "bold"))
lb5.place (x = 6, y=73)

lb6 = Label (iot, text = "l", font =("consolas", 13, "bold") )
lb6.place (x = 180, y=73)

lb7 = Label (iot, text = "Water In", font =("consolas", 13, "bold") )
lb7.place (x = 6, y=103)

lb8 = Label (iot, text = "l", font =("consolas", 13, "bold") )
lb8.place (x = 180, y=103)

lb9 = Label (iot, text = "l", font =("consolas", 13, "bold"))
lb9.place (x = 330, y=40)

lb10 = Label (iot, text = "l", font =("consolas", 13, "bold"))
lb10.place (x = 330, y=73)

lb11 = Label (iot, text = "l", font =("consolas", 13, "bold"))
lb11.place (x = 330, y=103)

    #tạo label bên phải:
lab1 = Label(iot, text = "PH", font =("consolas", 13, "bold"))
lab1.place (x=380, y=10)

lab2_data = DoubleVar()
lab2 = Label(iot,textvariable = lab2_data, relief = "solid", borderwidth = 0.5, font = "Times 13" )
lab2.place (x=430, y=10, width = 85)

lab3 = Label(iot, text = "pH", font =("consolas", 13, "bold"))
lab3.place (x=520, y=10)

lab4 = Label(iot, text = "EC", font =("consolas", 13, "bold"))
lab4.place (x=380, y=40)

lab5_data = DoubleVar()
lab5 = Label(iot,textvariable = lab5_data, relief = "solid", borderwidth = 0.5, font = "Times 13" )
lab5.place (x=430, y=40, width = 85)

lab6 = Label(iot, text = "mS/cm", font =("consolas", 13, "bold"))
lab6.place (x=520, y=40)

lab7 = Label(iot, text = "Temp", font =("consolas", 13, "bold"))
lab7.place (x=380, y=70)

lab8_data = DoubleVar()
lab8 = Label(iot,textvariable = lab8_data, relief = "solid", borderwidth = 0.5, font = "Times 13" )
lab8.place (x=430, y=70, width = 85)

lab9 = Label(iot, text = "Celcius", font =("consolas", 13, "bold"))
lab9.place (x=520, y=70)

lab10 = Label(iot, text = "Hud", font =("consolas", 13, "bold"))
lab10.place (x=380, y=100)

lab11_data = DoubleVar()
lab11 = Label(iot,textvariable = lab11_data, relief = "solid", borderwidth = 0.5, font = "Times 13" )
lab11.place (x=430, y=100, width = 85)

lab12 = Label(iot, text = "%", font =("consolas", 13, "bold"))
lab12.place (x=520, y=100)

lab13 = Label(iot, text = "CO2", font =("consolas", 13, "bold"))
lab13.place (x=380, y=130)

lab14_data = DoubleVar()
lab14 = Label(iot,textvariable = lab14_data, relief = "solid", borderwidth = 0.5, font = "Times 13" )
lab14.place (x=430, y=130, width = 85)

lab15 = Label(iot, text = "ppm", font =("consolas", 13, "bold"))
lab15.place (x=520, y=130)

lab16 = Label(iot, text = "Light", font =("consolas", 13, "bold"))
lab16.place (x=380, y=160)

lab17_data = DoubleVar()
lab17 = Label(iot,textvariable = lab17_data, relief = "solid", borderwidth = 0.5, font = "Times 13" )
lab17.place (x=430, y=160, width = 85)

lab18 = Label(iot, text = "Lux", font =("consolas", 13, "bold"))
lab18.place (x=520, y=160)

lab19_data = DoubleVar()
lab19 = Label(iot, textvariable = lab19_data , relief = "solid", borderwidth = 0.5, font = "Times 13" )
lab19.place (x = 240, y=40, width = 85 )

lab20_data = DoubleVar()
lab20 = Label(iot , textvariable = lab20_data, relief = "solid", borderwidth = 0.5, font = "Times 13" )
lab20.place (x = 240, y=73, width = 85 )

lab21_data = DoubleVar()
lab21 = Label(iot,textvariable = lab21_data, relief = "solid", borderwidth = 0.5, font = "Times 13" )
lab21.place (x = 240, y=103, width = 85 )

status_data = DoubleVar()
status = Label (iot, textvariable = status_data,  font =("consolas", 13, "bold") )
status.place(x= 490, y =250)
status_label = Label (iot, text = 'Status: ', font =("consolas", 13, "bold") )
status_label.place(x = 407 , y = 250)

Date_data =  DoubleVar()
Date = Label (iot, textvariable = Date_data,  font =("consolas", 11, "bold") )
Date.place(x= 20, y =250)
#tạo khung nhập liệu

en1 = Entry(iot, font = "Times 13")
en1.place (x = 120, y=40, width = 55 )

en2 = Entry(iot, font = "Times 13")
en2.place (x = 120, y=73, width = 55 )
    
en3 = Entry(iot, font = "Times 13")
en3.place (x = 120, y=103, width = 55 )



    #tạo nút nhấn
bt1 = Button(iot, text = "PUMB NUTRITION", font = ("consolas", 14, "bold"), bg = "cyan", fg = "white")
bt1.place(x = 20, y = 140, width = 170, height = 30)
bt1['command'] = lambda : send_message1( en1,en2) 
    
bt2 = Button(iot, text = "PUMP WATER", font = ("consolas", 14, "bold"), bg = "cyan", fg = "white")
bt2.place(x = 210, y = 140, width = 120, height = 30)
bt2['command'] = lambda : send_message2( en3)

q_button = Button(iot, text = "Exit", font = ("consolas",14,"bold"), bg = "cyan", fg = "white")
q_button.place(x = 20, y= 180 , width = 120 , height = 30)
q_button['command'] = lambda: quit_program(client)

client = mqtt.Client()
client.connect(MQTT_Broker, MQTT_Port,Keep_Alive_Interval)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.subscribe("Temperature", qos=1)
client.loop_start()
iot.mainloop()



