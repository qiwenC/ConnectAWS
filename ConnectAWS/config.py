
# wifi configuration
WIFI_SSID = 'YOUR_WIFI'
WIFI_PASS = 'YOUR_WIFI_PASSWORD'

# AWS general configuration
AWS_PORT = 8883
AWS_HOST = 'YOUR_AWS_HOST_ADDRESS'
AWS_ROOT_CA = '/flash/cert/root-CA.crt'
AWS_CLIENT_CERT = '/flash/cert/xxxx.cert.pem'
AWS_PRIVATE_KEY = '/flash/cert/xxxx.private.key'
################## Subscribe / Publish client #################
#CLIENT_ID = 'PycomPublishClient'#?
TOPIC = 'myTestTopic'
#DEVICE_TOPIC = 'myTestTopic/deviceID'
OFFLINE_QUEUE_SIZE = -1
DRAINING_FREQ = 2
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5
LAST_WILL_TOPIC = 'PublishTopic' #？
LAST_WILL_MSG = 'To All: Last will message'#？

####################### Shadow updater ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "ShadowUpdater"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

####################### Delta Listener ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "DeltaListener"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

####################### Shadow Echo ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "ShadowEcho"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5
