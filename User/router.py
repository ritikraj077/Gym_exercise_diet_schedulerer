from flask import Flask,request,jsonify,session,redirect
from app import app
from Database.Connection import database_connection
from User.Services import sign_up_db, user_login_db, user_delete_db , user_update_db, check_registration_user, forget_password_db
from User import Model as user_models
import json
from Exercise.services import  verify_user_auth
from Authentication_jwt.authentication import check_bearer_token
SECRET_KEY = 'Secret_key1234'



 ##api for signup ne user   
@app.route("/sign_up", methods=["POST"])
def sign_up_user():
    
    try:
        user_data = request.json
        print(user_data)
        output = check_registration_user(user_data)
        
        if not output:
        
            user_model = user_models.Registration(**user_data)
           
            #user_data= user_model(request.json)
            
            sign_up = sign_up_db(user_model)
            print(sign_up)
            if "Invalid Mobile Number" in sign_up:
                return jsonify({"status_code": 422, "success": False, "message": "Invalid Mobile Number"})
            else:
                return jsonify({"status_code": 200, "success": True, "message": "User signed up successfully"})
        return jsonify({"status_code": 409, "success": False, "message": "User already exist change mobile and username"})

    except Exception as e:
        # Handle validation errors
        return jsonify({"status_code": 422, "success": False, "message": str(e)})
    # except Exception as e:
    #     # Handle other exceptions
    #     return jsonify({"status_code": 500, "success": False, "message": str(e)})

       
    

        
    
    
       


##api for login user 
@app.route("/login", methods=["POST"])
def login_user():
    if request.method == "POST":
        data = request.json
        user_data = user_models.login(data).get_login_data()
        result = user_login_db(user_data)
        

        
            # Keys are present, proceed with login
            #result = user_login_db(data)
        if "successfully" in result:
                # If login is successful, generate JWT token
            token = user_models.login.generate_jwt_token(data, SECRET_KEY)
            return jsonify({"status_code":200, "sucess_status":True, "token": token}), 200
        else:
            return jsonify({"status_code": 401, "success": False,"error": "Invalid credentials"}), 401
    else:
            # Keys are missing in form data
            return jsonify({"status_code": 400, "success": False,"error": "Missing Username or Password"}), 400



@app.route("/logout",methods = ["POST"])
def logout():
    session.pop('Username', None) 
    return redirect("/"), 200





@app.route("/Update_user", methods = ["POST"])
def update_user():
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
    data = request.json
    print(data)
    user_data = user_models.update(data).update_user_data()
    print(user_data)
    
    return user_update_db(user_data)


@app.route("/Delete_user", methods = ["DELETE"])
def delete_user():
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
    data = request.json
    user_data = user_models.delete(data).delete_user_data()
    return  user_delete_db(user_data)


@app.route("/Forget_password", methods = ["POST"])
def forget_password():
    data = request.json
    user_data = user_models.forget_pass(data).password_username()
    return forget_password_db(user_data)