import paho.mqtt.client as mqtt

mqtt_host = 'localhost'
action_queue = '$ACTION/#'


def on_connect(mqtt_client, user_date, flags, rc):
    mqtt_client.subscribe(action_queue)


def on_message(mqtt_client, user_data, message):
    print(f'msg.topic: {message.payload}')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_host, 1883, 60)

client.loop_forever()

