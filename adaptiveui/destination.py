import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('destination', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        user_preferences = request.form
        
        return redirect(url_for('travelui.index'))

    return render_template('destination/index.html')