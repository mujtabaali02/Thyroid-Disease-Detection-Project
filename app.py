from train_build import building_model
import pickle
from flask import Response
import numpy as np
from Logs import logger
from flask import Flask,request,render_template,redirect,url_for
from train_build import building_model
import training_validation
import js2py
from training_validation import train_validation
from DBOperations import operations
app=Flask(__name__,template_folder='templates')

@app.route("/",methods=['GET','POST'])
def login_page():
    return render_template('admin_login.html')

@app.route("/login",methods=['POST','GET'])
def admin_login():
    loger = logger.App_Logger()
    f=open("Prediction_logs/app_logs.txt",'a+')
    loger.log(f,"admin_login is started")
    try:
        values=[value for value in request.form.values()]
        obj=operations.Operation_DB()
        conn=obj.connection("thyroid_peoject")
        mycursor=conn.cursor()
        mycursor.execute("select * from `login_table` where user_id='{}' and admin_password='{}'".format(values[0],values[1]))
        result=mycursor.fetchall()
        if result:
            return redirect('home') # for route and redirect(url_for('function_name')) for function calling
            # return redirect(url_for('home_page'))
        else:
            return Response("Failed to login")
    except:
        loger.log(f,"Error in admin_login function ")
        f.close()
        return Response("Failed to connect")
    f.close()

@app.route("/home", methods=['POST','GET'])
def home_page():
    return  render_template('index.html')

@app.route("/training",methods=['GET','POST'])
def training_model():
    loger = logger.App_Logger()
    f = open("Prediction_logs/app_logs.txt", 'a+')
    loger.log(f,"training function is started!!")
    try:
        file_path="Datasets/hypothyroid.csv"
        object=building_model.Build(file_path)
        object.make_a_model(file_path)
        loger.log(f,"training done successfully")
        # return redirect("home")
        f.close()
    except Exception as e:
        loger.log(f, "Error Occurred in training "+e)
        f.close()
        return Response ("Error Occurred %s " % e)
    f.close()
    # return Response("Training done successful")
    return redirect("home")

@app.route('/prediction',methods=['POST','GET'])
def prediction_function():
    loger = logger.App_Logger()
    f = open("Prediction_logs/app_logs.txt", 'a+')
    loger.log(f,"prediction function is started !!")
    try:
        obj = operations.Operation_DB()
        db_name = "thyroid_peoject"
        loger=logger.App_Logger()
        loger.log(f,"prediction function is starter!!")
        model=pickle.load(open("Models/logistic_model.pkl",'rb'))
        values=[float(value) for value in request.form.values()]
        final=np.array([[values]])
        result=model.predict(final[0])
        result=int(result)
        values.append(result)
        obj.insert_on_table(db_name,values)
        if result==0:
            var = "Negative Report"
        else:
            var="Positive Report"
        loger.log(f, "prediction function is done successfully")
        f.close()
        return render_template("result.html",value=var)

    except Exception as e:
        loger.log(f, "Error Occurred : "+e)
        f.close()
        return Response ("Error Occurred %s " % e)
    f.close()
    return Response ("Prediction Successfully Done")


if __name__=="__main__":
    app.run(debug=True)

