from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('travelui', __name__, url_prefix='/travelui')

@bp.route('/', methods = ["POST", "GET"])
def index():
    destination = request.form.get('destination')
    return render_template('travelui/index.html', destination=destination)