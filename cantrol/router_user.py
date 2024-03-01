from app import app

from app import app
from flask import Flask, render_template, redirect, request, session, jsonify
from flask_session import Session
from database_table.user_db import user_login_db, user_delete_db, sign_up_db
from database_table.execercise_shedule_db import workout_plan_db
from database_table.Diet_plan_db import diet_plan_db, weight_gain, weight_loss
from flask import jsonify
from Services.token_login import generate_jwt_token
from Services.features import cal_bmi
import requests


#api for login the user  after passing the username and password 
from flask import request, jsonify

@app.route("/login", methods=["POST"])
def login_user():
    if request.method == "POST":
        Username =  request.form["Username"]
        Password = request.form["Password"].encode('utf-8')
        
        result = user_login_db(Username, Password)
        print(result)

        
            # Keys are present, proceed with login
            #result = user_login_db(data)
        if "successfully" in result:
                # If login is successful, generate JWT token
            token = generate_jwt_token(Username)
            return jsonify({"token": token}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    else:
            # Keys are missing in form data
            return jsonify({"error": "Missing Username or Password"}), 400


      
@app.route("/logout")
def logout():
    session.pop('Username', None) 
    return redirect("/"), 200


    
    
 ##api for signup ne user   
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
    return  cal_bmi(Weight, Height)  
    


@app.route("/get_data",methods =["GET"])
def get_data():
    response = requests.get("https://dummyjson.com/products")
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        product = data["products"]
        list = []
        for i in product:
            id = i["id"]
            title = i["title"]
            price = i["price"]
            list.append([id,title,price])
            
             
        print(list)
        return jsonify(list), 200
    return None
    





   
if __name__ == "__main__":
    app.run(debug=True)




    
        
    