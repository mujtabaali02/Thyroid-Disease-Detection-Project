import pandas as pd
from sklearn.impute import SimpleImputer
from Logs import  logger
class transformation:
    def __init__(self):
        self.logger_object=logger.App_Logger()


    def miss_value_imputation(self,df):
        f=open("Validation_logs/data_transformation.txt",'a+')
        self.logger_object.log(f,"miss_value_imputation function is started!!")
        try:
            imputer=SimpleImputer(strategy='most_frequent')
            arr=imputer.fit_transform(df)
            self.df_imputed=pd.DataFrame(data=arr,columns=df.columns)
            self.df_imputed.to_csv("Datasets/imputed_data.csv",index=None,header=True)
            self.logger_object.log(f,"miss_value_imputated successfully by miss_value_imputation function!!")
            return self.df_imputed
        except Exception as e:
            self.logger_object.log(f,"Error Occurred in miss_value_imputation function!!")
            f.close()
        f.close()

    def Encoding(self,df):
        f = open("Validation_logs/data_transformation.txt", 'a+')
        self.logger_object.log(f, "Encoding is started!!")
        try:
            list_cat=[]
            list_num=[]
            for col in df.columns:
                if df[col].dtype=='float64':
                    list_num.append(col)
                else:
                    list_cat.append(col)
            self.encoded=pd.get_dummies(data=df,columns=list_cat,drop_first=True)
            self.encoded.to_csv("Datasets/Encoded_data.csv",header=True,index=None)
            self.logger_object.log(f,"Encoded function done successfully!!")
            return self.encoded
        except Exception as e:
            self.logger_object.log(f,"Error Occurred in Encoding Function!!")
            f.close()
        f.close()


    def object_type_into_float(self,data,cols):
        f = open("Validation_logs/data_transformation.txt", 'a+')
        self.logger_object.log(f, "object_type_into_float started!!")
        try:
            data[cols]=data[cols].astype('float64')
            self.data1=data
            self.logger_object.log(f, "object_into_float done successfully")
            return self.data1
        except Exception as e:
            self.logger_object.log(f,"Some Error Occurred!!")
            f.close()
        f.close()



