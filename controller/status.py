from flask import Blueprint, render_template
from controller.db import get_db
from controller.auth import login_required


bp = Blueprint('status', __name__)


@bp.route('/')
def index():
    power = 'OK'
    return render_template('status/index.html',
                           power=power,
                           tanklevel=80,
                           controllers=controller_count(),
                           ports=port_count(),
                           enabled_ports=enabled_port_count())


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
