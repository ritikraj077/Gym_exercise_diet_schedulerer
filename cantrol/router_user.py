from app import app

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
    
    
    
@app.route("/logout")
def logout():
    session.pop('Username', None) 
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


##api to calculate the bmi index of a member 
@app.route("/bmi", methods=["POST"])
def bmi():
    Weight = request.form["weight"]
    Height = request.form["height"]
    Bmi = cal_bmi(Weight, Height)  
    if Bmi < 18.5:
        return f" Bmi is : {str(Bmi)} you are Underweight"
    elif Bmi >= 18.5 and Bmi < 25:
        return f"Bmi is: {str(Bmi)} Normal weight"
    elif Bmi >= 25 and Bmi < 30:
        return f" Bmi is : {str(Bmi)} You are Overweight need to Workout"
    else:
        return f"Bmi is {str(Bmi)} you are Obese you should losse some weight"

     #Height : {Height } and Weight :{Weight} is {str(Bmi)} " # Convert Bmi to string before returning

def cal_bmi(Weight, Height):
    # Convert height to meters
    height_meters = float(Height) / 100
    
    # Convert weight to kilograms
    weight_kg = float(Weight)
    
    # Calculate BMI
    if height_meters > 0:
        bmi = round((weight_kg / (height_meters ** 2)), 2)
        return bmi
    else:
        return "Invalid height"

    
    
# def cal_bmi(Height, Weight):
#     # Convert height to meters
#     height_meters = float(Height)/ 100
    
#     # Calculate BMI
#     if height_meters > 0:
#         bmi = round((Weight / (height_meters ** 2)), 2)
#         return bmi
#     else:
#         return "Invalid height"



    
    
   



    
   
if __name__ == "__main__":
    app.run(debug=True)




    
        
    