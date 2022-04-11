from Training_validation import row_data_validations as rdw
from Logs import logger
from Training_validation import data_transformation as dtf
from Training_validation import feature_selection as fs

class train_validation:
    def __init__(self,file_path):
         self.file_path=file_path
         self.row_data=rdw.row_data_validation(file_path)
         self.data_transform=dtf.transformation()
         self.file_object=open("training_logs/training_main.txt",'a+')
         self.logger=logger.App_Logger()
         self.feature_selection=fs.Selection()

    def train_validation_data(self):
         self.logger.log(self.file_object,"train_validation_data function is started!!")
         try:
              data1=self.row_data.replace_by_null()
              self.logger.log(self.file_object, "replace_by_null is called")
              data2=self.row_data.drop_more_than_95_missing(data1)
              self.logger.log(self.file_object, "drop_more_than_95 function is called")
              data3=self.data_transform.miss_value_imputation(data2)
              self.logger.log(self.file_object,"Missing Value imputation function is called")
              data3.to_csv("Datasets/validated_data.csv")
              cols=['age','TSH','T3','TT4','T4U','FTI']
              data4=self.data_transform.object_type_into_float(data3,cols)
              data5=self.data_transform.Encoding(data4)
              data5.to_csv("Datasets/Encoded_data1.csv",header=True,index=None)
              thresh=0.112
              X=data5.drop(columns=['binaryClass_P'],axis=1)
              y=data5['binaryClass_P']
              final_data=self.feature_selection.feature_selection(X,thresh)
              final_data['Result'] = y
              final_data.to_csv("Datasets/final_data.csv",header=True,index=None)
              return final_data
         except:
              self.logger.log(self.file_object, "Error Occurred in train validation_data function!!")
         self.file_object.close()









