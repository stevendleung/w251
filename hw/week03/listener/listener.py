import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT= 1883
LOCAL_MQTT_TOPIC="test_topic"

REMOTE_MQTT_HOST="ec2-13-57-5-80.us-west-1.compute.amazonaws.com"
REMOTE_MQTT_PORT= 1883
REMOTE_MQTT_TOPIC="test_topic"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC, qos =1)

	
def on_message(client,userdata, msg):
  try:
    print("message received: ",str(msg.payload))
    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=1, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
remote_mqttclient = mqtt.Client()
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)

local_mqttclient.on_message = on_message



# go into a loop
local_mqttclient.loop_forever()

