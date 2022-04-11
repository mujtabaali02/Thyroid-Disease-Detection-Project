from sklearn.feature_selection import VarianceThreshold
from Logs import logger
class Selection:
    def __init__(self):
        self.logger_object=logger.App_Logger()
        self.file_object=open("Validation_logs/feature_Selection.txt",'a+')

    def feature_selection(self,data,thresh):
        self.logger_object.log(self.file_object,"feature selection is started!!")
        try:
            thresh_object=VarianceThreshold(threshold=thresh)
            thresh_object.fit(data)
            self.cols_selected=data.columns[thresh_object.get_support()]
            self.new_data=data[self.cols_selected]
            self.logger_object.log(self.file_object,"feature_selection done successfully")
            return self.new_data
        except Exception as e:
            self.logger_object.log(self.file_object,"Error Occurred !!")
            self.file_object.close()
        self.file_object.close()

