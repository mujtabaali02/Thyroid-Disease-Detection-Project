# from DBOperations import operations
# db_name="thyroid_peoject"
#
# # Table: info_data"
# value=[51.0,1.9,2.2,74.0,81.0,1,1,0,0]
# value.append(0)
# obj=operations.Operation_DB()
# obj.insert_on_table(db_name,value)

#import pickle
# from DBOperations import operations
import pandas as pd
# from train_build import building_model
# file_path="Datasets/hypothyroid.csv"
# building_model.Build(file_path)
# object.make_a_model(file_path)

# obj=operations.Operation_DB()
# obj.insert_on_table("mydb")


# from training_validation import *
# file_path="Datasets/hypothyroid.csv"
# object=train_validation(file_path)
# data=object.train_validation_data()
#
# df=pd.read_csv("Datasets/final_data.csv")
# df.head()
# df=pd.read_csv("Datasets/validated_data.csv")
# df.isnull().sum().sort_values(ascending=False)

# print(data.head())
# import pickle
# import numpy as np
# list1=[44.0,45.0,1.4,39.0,33.0,1,1,1,0]
# arra1=np.array([list1])
# model=pickle.load(open("Models/logistic_model.pkl",'rb'))
# result=model.predict(arra1)
# print(result)


import pandas as pd
df=pd.read_csv("Datasets/hypothyroid.csv")
print(df.shape)