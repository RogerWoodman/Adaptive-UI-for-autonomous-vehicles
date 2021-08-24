from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

bp = Blueprint('travelui', __name__, url_prefix='/travelui')

@bp.route('/', methods = ["POST", "GET"])
def index():
    user_preferences = request.form.to_dict() # to allow dictionary to be updated

    training_data = { # for 4 questions in form (fuel, news, traffic news, journey time)
        "detailed": [1, 1, 1, 0], # is there a lot to read?
        "numerical": [1, 0, 0, 1], # does selecting mean looking at numerical data on the whole
        "only_car": [1, 0, 1, 1], # is this category only needed whilst in the car
        "include": [user_preferences["fuel"], user_preferences["news"], user_preferences["traffic"], user_preferences["time"]] # the labels (to include = 1, not include = 0) (based on what the user chooses in the form on the destination selection page)
    }

    # load data into a DataFrame object:
    df = pd.DataFrame(training_data)

    cols = ['detailed', 'numerical', 'only_car']
    X_train = df[cols]
    y_train = df['include']

    clf = DecisionTreeClassifier(random_state=1)
    clf.fit(X_train, y_train)

    test_data = { # determine whether music, weather, stocks and speed need to be shown
        "detailed": [0, 1, 1, 0],
        "numerical": [0, 1, 1, 1],
        "only_car": [0, 0, 0, 1]
    }

    #load data into a DataFrame object:
    df_2 = pd.DataFrame(test_data)

    pred = clf.predict(df_2)

    # Add predictictions for other menu tiles to user_preferences
    user_preferences.update({"music": pred[0]})
    user_preferences.update({"weather": pred[1]})
    user_preferences.update({"stocks": pred[2]})
    user_preferences.update({"speed": pred[3]})

    return render_template('travelui/index.html', user_preferences=user_preferences)