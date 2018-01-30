
# wifi configuration
WIFI_SSID = 'Croyance'
WIFI_PASS = 'Freya270'

# AWS general configuration
AWS_PORT = 8883
AWS_HOST = 'ap71nzxvi4ixf.iot.eu-west-2.amazonaws.com'
AWS_ROOT_CA = '/flash/cert/root-CA.crt'
AWS_CLIENT_CERT = '/flash/cert/ef37e84425.cert.pem'
AWS_PRIVATE_KEY = '/flash/cert/ef37e84425.private.key'
################## Subscribe / Publish client #################
CLIENT_ID = 'PycomPublishClient'
TOPIC = 'myTestTopic'
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
