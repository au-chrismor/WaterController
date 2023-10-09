from flask import Blueprint, render_template
from controller.db import get_db
from controller.auth import login_required


bp = Blueprint('sched', __name__, url_prefix='/sched')


@bp.route('/')
def sched_index():
    print('index(): Starting')
    db = get_db()
    schedules = db.execute('SELECT s.day, d.day_name, s.hour, s.minute, s.state, c.controller_name, p.port_name, p.enabled FROM sched as s, day as d, controller as c, port as p WHERE d.day_id = s.day AND c.controller_id = s.controller_id AND p.port_id = s.port_id AND p.controller_id = s.controller_id ORDER BY s.day, s.hour, s.minute').fetchall()
    return render_template('sched/index.html', scheds=schedules)


