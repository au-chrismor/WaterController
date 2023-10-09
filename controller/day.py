import sqlite3
from flask import Blueprint
from controller.db import get_db


bp = Blueprint('day', __name__, url_prefix='/day')
