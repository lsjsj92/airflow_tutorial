import sys

import numpy as np
from sklearn.ensemble import RandomForestClassifier



class TitanicModeling:
    def __init__(self):
        pass

    def run_sklearn_modeling(self, X, y, n_estimator):
        model = self._get_rf_model(n_estimator)

        model.fit(X, y)

        model_info = {
            'score' : {
                'model_score' :  model.score(X, y)
            },
            'params' : model.get_params()
        }

        return model_info

    def _get_rf_model(self, n_estimator):
        return RandomForestClassifier(n_estimators=n_estimator, max_depth=5)
