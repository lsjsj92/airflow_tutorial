import os
import pathlib


class PathConfig:
    def __init__(self):
        self.project_path = pathlib.Path(__file__).parent.resolve()
        self.titanic_path = f"{self.project_path}/data/titanic"

class EnvConfig:
    def get_gender_mapping_code(self):
        gender_mapping_info = {
            'male' : 0,
            'female' : 1,
        }

        return gender_mapping_info
    
    def get_column_list(self):
        columns_list = ['Sex', 'Age_band', 'Pclass']
        return columns_list