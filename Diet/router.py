from flask import request, jsonify
from app import app
from Diet.model import diet_plan_db
from Exercise.services import  verify_user_auth
from Authentication_jwt.authentication import check_bearer_token
SECRET_KEY = 'Secret_key1234'






@app.route("/Diet_plan", methods=["GET"])
def Diet_plan():
    
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
    print(day)


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