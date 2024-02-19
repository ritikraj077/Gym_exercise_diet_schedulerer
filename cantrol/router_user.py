from app import app
from flask import Flask, render_template, redirect, request, session, jsonify
from flask_session import Session
import mysql.connector
from database_table.user_db import user_login_db, user_delete_db, sign_up_db
from database_table.execercise_shedule_db import workout_plan_db
from database_table.Diet_plan_db import diet_plan_db, weight_gain, weight_loss










@app.route("/login", methods=["POST", "GET"])
def login_user():
    if request.method == "POST":
        
        Username = request.form['Username']
        Password = request.form['Password']
        # if Username in user and user['username'] == Password:
        return user_login_db(Username,Password)
    else :
        return "Username and Password is Incorrect"
    
@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

# @app.route("/sign_up" , methods = ["POST"])
# def sign_up_user():
    
#     if "Name" not in  request.form or "Price" not in  request.form:
#         return {"massage":"Plezz mention name and price"}, 400

#         Id = request.form["Id"]
#         Username = request.form['Username']
#         Password = request.form['Password']
        

    
#         return user_signup_db(Id,Username,Password)
    
    
    
@app.route("/sign_up", methods=["POST"])
def sign_up_user():
    if "Id" not in request.form or "Username" not in request.form or "Password" not in request.form:
        return {"message": "Please mention Id, Username, and Password"}, 400

    data = request.form
    return sign_up_db(data)



@app.route("/Delete_user", methods = ["DELETE"])
def delete_user():
    return user_delete_db() 







@app.route("/Diet_plan", methods=["GET"])
def Diet_plan():
    day = request.args.get('Day')

    if day == 'Monday':
        return diet_plan_db(day)
    
    elif day == 'Tuesday':
        return diet_plan_db(day)
    
    elif day == 'Wednesday':
        return diet_plan_db(day)
    
    elif day == 'Thursday':
        return diet_plan_db(day)
    
    elif day == 'Friday':
        return  diet_plan_db(day)
    
    elif day == 'Saturday':
        return  diet_plan_db(day)
    
    elif day == 'Sunday':
        return  diet_plan_db(day)
    else :
        return "Enter the Valid day"
    
    




@app.route("/Excercise", methods = ["GET"])
def exercise():
    day = request.args.get('Day')
    if day == 'Monday':
        return workout_plan_db(day)
    
    elif day == 'Tuesday':
        return workout_plan_db(day)
    
    elif day == 'Wednesday':
        return workout_plan_db(day)
    
    elif day == 'Thursday':
        return workout_plan_db(day)
    
    elif day == 'Friday':
        return  workout_plan_db(day)
    
    elif day == 'Saturday':
        return  workout_plan_db(day)
    
    elif day == 'Sunday':
        return  workout_plan_db(day)
    else :
        return "Enter the Valid day"
    
    


@app.route("/Weight_gain" , methods = ["GET"])
def weightgain():
    return weight_gain()

@app.route("/Weight_loss", methods = ["GET"])
def weightloss():
    return weight_loss()
   



    
   
if __name__ == "__main__":
    app.run(debug=True)




    
        
    