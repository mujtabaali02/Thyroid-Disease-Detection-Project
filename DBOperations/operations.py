import mysql.connector as cont
from Logs import logger
class Operation_DB:
    def __init__(self):
        self.logger_object=logger.App_Logger()

    def connection(self, db):
        f = open("DbLogs/connections.txt",'a+')
        self.logger_object.log(f, "connection function is started!!")
        try:
            conn = cont.connect(host="localhost", user="root", password="", database=db)
            self.logger_object.log(f, "Connected Successfully")
            f.close()
            return conn
        except Exception as e:
            self.logger_object.log(f,",failed to connect")
            f.close()
        f.close()

    def insert_on_table(self,db_name,values):
        f=open("DbLogs/connections.txt",'a+')
        self.logger_object.log(f,"insert_on_table is started!!")
        try:
            conn=self.connection(db_name)
            mycursor=conn.cursor()
            mycursor.execute("INSERT INTO `info_data` VALUES(null,{},{},{},{},{},{},{},{},{},{})".format(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9]))
            conn.commit()
            conn.close()
            mycursor.close()
            self.logger_object.log(f,"insert_on_table done successfully")
        except Exception as e:
            self.logger_object.log(f,"Error Occurred in insert_on_table function!!")
            f.close()
        f.close()