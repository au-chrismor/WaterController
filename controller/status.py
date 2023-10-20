from flask import Blueprint, render_template
from controller.db import get_db
from controller.auth import login_required
from paho.mqtt import client as mqtt
import random

bp = Blueprint('status', __name__)


@bp.route('/')
def index():
    power = 'OK'
    return render_template('status/index.html',
                           power=power,
                           tanklevel=80,
                           controllers=controller_count(),
                           ports=port_count(),
                           enabled_ports=enabled_port_count(),
                           msg_queue=test_message_broker())


def controller_count():
    db = get_db()
    count = db.execute('SELECT COUNT(controller_name) FROM controller').fetchone()
    return count


def port_count():
    db = get_db()
    count = db.execute('SELECT COUNT(port_name) FROM port').fetchone()
    return count


def enabled_port_count():
    db = get_db()
    count = db.execute('SELECT COUNT(port_name) FROM port WHERE enabled=1').fetchone()
    return count


def test_message_broker():
    broker = 'localhost'
    port = 1883
    topic = '$ACTION/#'
    try:
        client_id =f'python-mqtt-{random.randint(0, 1000)}'
        client = mqtt.Client(client_id=client_id, userdata=None, protocol=mqtt.MQTTv311, transport='tcp')
        client.username_pw_set('heartbeat', 'heartbeat')
        rc = client.connect(broker, port)
        if rc is None:
            return 0
        if rc == 0:
            client.disconnect()
            return 1
        else:
            return 0

    except Exception as ex:
        print(f'test_message_broker(): Exception {ex} occured')
        return False

