
import numpy as np

class TitanicPreprocess:
    def __init__(self):
        pass

    def run_preprocessing(self, data):
        data = self._set_initial(data)
        data = self._set_fill_na(data)
        data = self._set_feature(data)
        data = self._set_replace(data)

        return data

    def _set_fill_na(self, data):
        data.loc[(data['Age'].isnull()) & (data['Initial'] == 'Mr'), 'Age'] = 33
        data.loc[(data['Age'].isnull()) & (data['Initial'] == 'Master'), 'Age'] = 5
        data.loc[(data['Age'].isnull()) & (data['Initial'] == 'Mrs'), 'Age'] = 36
        data.loc[(data['Age'].isnull()) & (data['Initial'] == 'Miss'), 'Age'] = 22
        data.loc[(data['Age'].isnull()) & (data['Initial'] == 'Other'), 'Age'] = 46
        data['Embarked'].fillna('S', inplace=True)

        return data

    def _set_initial(self, data):
        data['Initial'] = 0
        data['Initial'] = data['Name'].str.extract('([A-Za-z]+)\.')
        data['Initial'].replace(
            ['Mlle', 'Mme', 'Ms', 'Dr', 'Major', 'Lady', 'Countess', 'Jonkheer', 'Col', 'Rev', 'Capt', 'Sir', 'Don','Dona'],
            ['Miss', 'Miss', 'Miss', 'Mr', 'Mr', 'Mrs', 'Mrs', 'Other', 'Other', 'Other', 'Mr', 'Mr', 'Mr', 'Other'],
            inplace=True)

        return data

    def _set_feature(self, data):
        data['Fare'] = data["Fare"].map(lambda i: np.log(i) if i > 0 else 0)
        data['Age_band'] = 0
        data['Alone'] = 0
        data['Family_Size'] = 0

        data.loc[data['Age'] <= 16, 'Age_band'] = 0
        data.loc[(data['Age'] > 16) & (data['Age'] <= 32), 'Age_band'] = 1
        data.loc[(data['Age'] > 32) & (data['Age'] <= 48), 'Age_band'] = 2
        data.loc[(data['Age'] > 48) & (data['Age'] <= 64), 'Age_band'] = 3
        data.loc[data['Age'] > 64, 'Age_band'] = 4

        data['Family_Size'] = data['Parch'] + data['SibSp']

        data.loc[data.Family_Size == 0, 'Alone'] = 1

        return data

    def _set_replace(self, data):
        data['Sex'].replace(['male','female'],[0,1],inplace=True)
        data['Embarked'].replace(['S','C','Q'],[0,1,2],inplace=True)
        data['Initial'].replace(['Mr','Mrs','Miss','Master','Other'],[0,1,2,3,4],inplace=True)
        data.drop(['Name', 'Age', 'Ticket', 'Cabin', 'PassengerId'], axis=1, inplace=True)

        return data
