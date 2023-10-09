import sqlite3
from flask import Blueprint
from controller.db import get_db


bp = Blueprint('port', __name__, url_prefix='/port')
