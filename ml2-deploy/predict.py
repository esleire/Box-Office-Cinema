import numpy as np
import pandas as pd
import joblib

model = joblib.load('model/TMDB_fr.joblib')


def get_form_data(data):
    feature_values = {
        'budget': 100000,
        'popularity': 5,
        'runtime': 60,
        'has_collection': 0,
        'is_english': 1,
        'crew_count': 5,
        'cast_count': 5,
    }

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]
    return feature_values


def predict(data, debug=False):
    values = get_form_data(data)

    if debug:
        print(f'Feature values: {values}\n')

    colums_order = ['budget', 'popularity', 'runtime', 'has_collection', 'is_english',
                    'crew_count', 'cast_count']

    values = np.array([values[feature]
                      for feature in colums_order], dtype=object)

    if debug:
        print('ordered feature values: ')
        print(list(zip(colums_order, values)))

    pred = model.predict(values.reshape(1, -1))
    return str(pred[0])
