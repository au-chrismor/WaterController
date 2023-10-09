import sqlite3
from flask import Blueprint, render_template, request
from controller.db import get_db

bp = Blueprint('controller', __name__, url_prefix='/controller')


@bp.route('/')
def controller_index():
    return render_template('controller/index.html',
                           controllers=list_controllers())

@bp.route('/<int:controller_id>')
def controller_detail(controller_id):
    db = get_db()
    controller = db.execute('SELECT controller_id, controller_name, enabled FROM controller WHERE controller_id=?',
                            (controller_id,)).fetchone()
    return render_template('controller/detail.html',
                           controller=controller,
                           port_count=count_ports(controller_id))


@bp.route('/<int:controller_id>/port')
def port_detail(controller_id):
    db = get_db()
    ports = db.execute('SELECT port_id, port_number, port_name, enabled, controller_id FROM port WHERE controller_id=?', (controller_id,)).fetchall()
    return render_template('controller/ports.html',
                           ports=ports)


@bp.route('/<int:controller_id>/port/<int:port_id>', methods=('GET', 'POST'))
def port_edit(controller_id, port_id):
    if request.method == 'POST':
        print(request.values)
        controller_id = request.form['controller']
        port_id = request.form['port']
        port_name = request.form['name']
        enabled = request.form.get('enabled')
        if enabled is None:
            stat = 0
        else:
            stat = 1
        print(f'enabled={enabled}')
        db = get_db()
        db.execute('UPDATE port SET port_name=?, enabled=? WHERE controller_id=? AND port_id=?',
                   (port_name, stat, controller_id, port_id))
        db.commit()
        return render_template('controller/index.html',
                               controllers=list_controllers())
    else:
        db = get_db()
        port = db.execute('SELECT port_id, controller_id, port_number, port_name, enabled FROM port WHERE port_id=? AND controller_id=?', (port_id, controller_id)).fetchone()
        return render_template('controller/edit_port.html', port=port)

def list_controllers():
    db = get_db()
    return db.execute(
        'SELECT controller_id, controller_name, enabled FROM controller ORDER BY controller_name').fetchall()


def count_ports(controller_id=None):
    db = get_db()
    return db.execute('SELECT COUNT(port_id) FROM port WHERE controller_id=?', (controller_id,)).fetchone()
