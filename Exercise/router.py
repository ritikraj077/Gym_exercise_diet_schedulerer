from app import app
from flask import request, jsonify
from Exercise.services import workout_plan_db, verify_user_auth
from Exercise.model import cal_bmi
from Authentication_jwt.authentication import check_bearer_token
SECRET_KEY = 'Secret_key1234'







@app.route("/Exercise", methods = ["GET"])
def exercise():

    cheak = check_bearer_token(request, SECRET_KEY)
   
    if 'error' in cheak and 'Bearer token has expired' in cheak['error']:
        error_message = cheak['error']
        
        return jsonify ({"Error": error_message})
    else:
    # Proceed with the decoded token or user information
    
        # Return a proper error response
       
        
        username = cheak["Username"]
        if not username:
            return jsonify({'error': 'Username not found in token'}), 401
        else:
        
            user = verify_user_auth(username)
            
            if user is None:
                return {'error': 'Unauthorized'}, 401
            
            day = request.args.get('Day')
        try:
            
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
        except Exception as e:
            print("error :",e)
            
            
        

@app.route("/bmi", methods=["POST"])
#current_user having token or not
#if token then token is EQUAL to login bearer token or not  
def bmi():
    print(request.form)
    Weight = request.form["weight"] #weight in kilogram
    Height = request.form["height"] #Height in meters 
    return  cal_bmi(Weight, Height) , 200
        
        
        
        
        
# from flask import request, jsonify

# @app.route("/Exercise", methods=["GET"])
# def exercise():
#     check = check_bearer_token(request, SECRET_KEY)
#     if "Error" in check:
#         # Return a proper error response
#         return jsonify({'error': 'Bearer token check failed'}), 401
        
#     username = check.get("Username")
#     if not username:
#         return jsonify({'error': 'Username not found in token'}), 401
    
#     user = verify_user_auth(username)
#     if user is None:
#         return jsonify({'error': 'Unauthorized user'}), 401

#     # If everything is fine, proceed with your logic here
