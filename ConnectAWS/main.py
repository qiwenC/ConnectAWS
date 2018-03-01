from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from network import WLAN
from pytrack import Pytrack
from L76GNSS import L76GNSS
#from pysense import Pysense
#from SI7006A20 import SI7006A20
import binascii
import json
import machine
import time
import utime
import config
import gc
from machine import RTC

# Connect to wifi
wlan = WLAN(mode=WLAN.STA)
wlan.connect(config.WIFI_SSID, auth=(None, config.WIFI_PASS), timeout=5000)
while not wlan.isconnected():
    time.sleep(0.5)
print('WLAN connection succeeded!')

time.sleep(2)
gc.enable

# setup rtc
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
print(rtc.now())

# get MAC address as the device ID
deviceID = binascii.hexlify(wlan.mac())

# configure pysense
#py = Pysense()
#si = SI7006A20(py)
py = Pytrack()
l76 = L76GNSS(py, timeout=30)


# user specified callback function
def customCallback(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")


# configure the MQTT client
pycomAwsMQTTClient = AWSIoTMQTTClient(config.CLIENT_ID)
pycomAwsMQTTClient.configureEndpoint(config.AWS_HOST, config.AWS_PORT)
pycomAwsMQTTClient.configureCredentials(config.AWS_ROOT_CA, config.AWS_PRIVATE_KEY, config.AWS_CLIENT_CERT)

pycomAwsMQTTClient.configureOfflinePublishQueueing(config.OFFLINE_QUEUE_SIZE)
pycomAwsMQTTClient.configureDrainingFrequency(config.DRAINING_FREQ)
pycomAwsMQTTClient.configureConnectDisconnectTimeout(config.CONN_DISCONN_TIMEOUT)
pycomAwsMQTTClient.configureMQTTOperationTimeout(config.MQTT_OPER_TIMEOUT)
pycomAwsMQTTClient.configureLastWill(config.LAST_WILL_TOPIC, config.LAST_WILL_MSG, 1)

#Connect to MQTT Host
if pycomAwsMQTTClient.connect():
    print('AWS connection succeeded')

# Subscribe to topic
pycomAwsMQTTClient.subscribe(config.TOPIC, 1, customCallback)
time.sleep(2)

# Send message to host
loopCount = 0
while loopCount < 8:
    coord = l76.coordinates()
    message = {}
    message['deviceID'] = deviceID
    timestamp = utime.localtime()
    message['timestamp'] = "%d/%d/%d %d:%d:%d"%(timestamp[2],timestamp[1],timestamp[0],timestamp[3],timestamp[4],timestamp[5])
    message['gps'] = coord
    #message['temp'] = si.temperature()
    #message['humid'] = si.humidity()
    #message['message'] = "New Message" + str(loopCount)
    #message['sequence'] = loopCount
    messageJson = json.dumps(message)
    #deviceJson = json.dumps(deviceID)
    pycomAwsMQTTClient.publish(config.TOPIC, messageJson, 1)
    #pycomAwsMQTTClient.publish(config.DEVICE_TOPIC,deviceJson,1)
    #pycomAwsMQTTClient.publish(config.TOPIC, "New Message " + str(loopCount), 1)
    loopCount += 1
    time.sleep(5.0)
