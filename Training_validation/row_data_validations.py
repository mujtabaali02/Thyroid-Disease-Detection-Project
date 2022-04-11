import numpy as np
from  training_validation import *
from Logs import logger
import pandas as pd
import numpy as np

class row_data_validation:
    def __init__(self,path):
        self.path=path
        self.logger=logger.App_Logger()
        # self.file_object=open("training_logs/row_data_validation.txt",'a+')

    def replace_by_null(self):
        f=open("Validation_logs/row_data_validation.txt",'a+')
        self.logger.log(f,"replace_by_null is started!!")
        try:
            self.data=pd.read_csv(self.path)
            print(self.data.head())
            self.df=self.data.replace('?',np.nan)
            self.logger.log(f,"Dataset's ? is replaced by Nan Successfully !!")
            self.df.to_csv("Datasets/Missing_replaced.csv",index=None,header=True)
            return self.df
        except Exception as e:
            self.logger.log(f,"Error is Occurred in replace_by_null function : "+e)
            f.close()
        f.close()

    def drop_more_than_95_missing(self,data):
        f = open("Validation_logs/row_data_validation.txt", 'a+')
        try:
            self.col_to_drop=[col for col in data.columns if data[col].isnull().mean()>0.95]
            self.new_data=data.drop(columns=self.col_to_drop,axis=1)
            self.logger.log(f, "drop_more_than_95_missing function done successfully!!")
            return self.new_data
        except Exception as e:
            self.logger.log(f,"Some Error Occurred in drop_more_than_95_missing function")
            f.close()
        f.close()










