
import pandas as pd

from MLproject.preprocess import TitanicPreprocess
from MLproject.config import PathConfig
from MLproject.dataio import DataIOSteam
from MLproject.model import TitanicModeling


class TitanicMain(TitanicPreprocess, PathConfig, TitanicModeling, DataIOSteam):
    def __init__(self):
        TitanicPreprocess.__init__(self)
        PathConfig.__init__(self)
        TitanicModeling.__init__(self)
        DataIOSteam.__init__(self)

    def prepro_data(self, f_name, **kwargs):
        # fname = train.csv
        data = self.get_data(self.titanic_path, f_name)
        data = self.run_preprocessing(data)
        data.to_csv(f"{self.titanic_path}/prepro_titanic.csv", index=False)
        kwargs['task_instance'].xcom_push(key='prepro_csv', value=f"{self.titanic_path}/prepro_titanic")
        return "end prepro"

    def run_modeling(self, n_estimator, flag, **kwargs):
        # n_estimator = 100
        f_name = kwargs["task_instance"].xcom_pull(key='prepro_csv')
        data = self.get_data(self.titanic_path, f_name, flag)
        X, y = self.get_X_y(data)
        model_info = self.run_sklearn_modeling(X, y, n_estimator)
        kwargs['task_instance'].xcom_push(key='result_msg', value=model_info)
        return "end modeling"
