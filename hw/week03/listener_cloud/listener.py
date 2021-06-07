import paho.mqtt.client as mqtt
import boto3

s3client = boto3.client('s3',
    aws_access_key_id=YOUR_KEY,
    aws_secret_access_key=YOUR_SECRET_KEY)

LOCAL_MQTT_HOST="mqtt"
LOCAL_MQTT_PORT= 1883
LOCAL_MQTT_TOPIC="test_topic"

global count
count = 0

def save_img(img_bytes):
    global count    

    response = s3client.put_object(
    Bucket='stevendleung-w251-hw-wk3',
    Body=img_bytes,
    Key='face{:d}.png'.format(count),
    ACL='public-read',
    ContentType='image/png')
    
    
    count += 1

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
  try:
    print("message received: ",str(msg.payload))
    save_img(msg.payload)  

  except Exception:
    traceback.print_exc()


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message



# go into a loop
local_mqttclient.loop_forever()

