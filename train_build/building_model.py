from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from training_validation import train_validation
from Logs import logger
import pickle
class Build:
    def __init__(self,file_path):
        # file_path = "Datasets/hypothyroid.csv"
        self.train_validations=train_validation(file_path)
        self.logger_object=logger.App_Logger()
        self.path=file_path
        self.make_a_model(file_path)

    def X_y(self,data,label_column):
        f = open("model_building_logs/model_building_main.txt", 'a+')
        self.logger_object.log(f, "X_y function is started!!")
        try:
            self.X=data.drop(columns=label_column,axis=1)
            self.y=data[label_column]
            self.logger_object.log(f, "X_y function done successfully")
            return self.X,self.y
        except Exception as e:
            self.logger_object.log(f,"Error Occurred : "+e)
            f.close()
        f.close()

    def train_test_split(self,X,y):
        f=open("model_building_logs/model_building_main.txt",'a+')
        self.logger_object.log(f,"train_test_split function is started!!")
        try:
            self.x_train,self.x_test,self.y_train,self.y_test = train_test_split(X,y,test_size=0.3,random_state=100)
            self.logger_object.log(f,"train_test_Split function is done successfully")
            return self.x_train,self.x_test,self.y_train,self.y_test
        except Exception as e:
            self.logger_object.log(f,"Error Occurred "+e)
            f.close()
        f.close()

    def make_a_model(self,file_path):
        f = open("model_building_logs/model_building_main.txt", 'a+')
        self.logger_object.log(f, "make_a_model function is started!!")
        try:
            data=self.train_validations.train_validation_data()
            X,y=self.X_y(data,'Result')
            x_train,x_test,y_train,y_test=self.train_test_split(X,y)
            lr=LogisticRegression()
            lr.fit(x_train,y_train)
            train_time = lr.score(x_train,y_train)
            test_time = lr.score(x_test,y_test)
            pickle.dump(lr,open("Models/logistic_model.pkl",'wb'))
            self.logger_object.log(f,f"model build successfully!! training_time : {train_time}  Testing_time : {test_time}")
            # return train_time,test_time
        except Exception as e:
            self.logger_object.log(f,"Error Occurred "+e)
            f.close()
        f.close()
















