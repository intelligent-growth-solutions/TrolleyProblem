import paho.mqtt.client as mqtt

a = 0
b = 0
c = 0
values = []
pipe = None

class MqttController():


    def __init__(self):
        self.pipe = None
        return

    def initialise(self, main_pipe):
        global pipe
        pipe = main_pipe

        #client = mqtt.Client(client_id="marauders map", protocol=mqtt.MQTTv311)
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id="marauders map")

        client.on_disconnect = on_disconnect
        client.on_publish = on_publish
        client.on_message = on_message
        client.on_subscribe = on_subscribe
        client.on_connect = on_connect

        client.username_pw_set(username="a_username", password="a_password")
        client.connect(host="an_ip_address", port=1883)

        client.loop_forever()
        print("init")

def on_connect(client, userdata, flags, rc):
        print("Device connected with result code: " + str(rc))
        request_list=["marauders map/0000_Beacon_1",
                      "marauders map/0012_Beacon2",
                      "marauders map/7512_Beacon3"
                      ]
        for i in request_list:
            client.subscribe(i, qos=0)



def on_disconnect(client, userdata, rc):
    print("Device disconnected with result code: " + str(rc))


def on_publish(client, userdata, mid):
    return

def error_path():
    print("Error")

def on_message(client, userdata, message):
    # global point
    global values  # Add a global variable to store the frontendHelper instance
    global a
    global b

    print(str(message.topic) + " " + str(message.payload))

    if message.topic == 'marauders map/0000_Beacon_1':
        a = str(message.payload)[-3:-1]

        print(a)

    elif message.topic == 'marauders map/0012_Beacon2':
        b = str(message.payload)[-3:-1]

        print(a)
        #values.append([a, b])
        #TODO convert values from RSSI to cartesian points
        pipe.send([(int(a), int(b))])



def on_subscribe(client, userdata, mid, qos):
    print("subscribed")
