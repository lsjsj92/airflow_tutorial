
import pandas as pd

class DataIOSteam:

    def get_data(self, path, f_name, flag=False):
        if flag:
            # flag이면 xcom으로 path를 받기 때문에 전체 경로 값이 fname에 존재함
            return pd.read_csv(f'{f_name}.csv')
        return pd.read_csv(f'{path}/{f_name}.csv')
    
    def get_X_y(self, data):
        X = data[data.columns[1:]]
        X = X[['Sex', 'Age_band', 'Pclass']]
        y = data['Survived']

        return X, y
