from flask import request
from jwt import decode as decode_token
import jwt
from app import app
#SECRET_KEY = 'Secret_key1234'










def cal_bmi(Weight, Height):
    # Convert height to meters
    height_meters = float(Height) / 100
    
    # Convert weight to kilograms
    weight_kg = float(Weight)
    
    # Calculate BMI
    if height_meters > 0:
        bmi = round((weight_kg / (height_meters ** 2)), 2)
        ##checking the bmi values and giving the masage 
        if bmi < 18.5:
            return f" Bmi is : {str(bmi)} you are Underweight"
        elif bmi >= 18.5 and bmi < 25:
            return f"Bmi is: {str(bmi)} Normal weight"
        elif bmi >= 25 and bmi < 30:
            return f" Bmi is : {str(bmi)} You are Overweight need to Workout"
        else:
            return f"Bmi is {str(bmi)} you are Obese you should losse some weight"

    else:
        return "Invalid Height and Weight"
    
    
    
    
# def check_bearer_token(request, SECRET_KEY):
#     auth_header = request.headers.get('Authorization')
    
    
#     if auth_header is None:
#         return {'error': 'Missing Authorization header'}, 401

#     scheme, token = auth_header.split()
#     #print(token)
#     if scheme != 'Bearer':
#         return {'error': 'Invalid Authorization header'}, 401

#     try:
#         user = decode_user(token,SECRET_KEY)
#     except Exception as e:
#         return {'error': str(e)}, 401

#     return user


# def decode_user(token,secret_key):

#     decoded_token = jwt.decode(jwt=token,
#                               key= secret_key ,
#                               algorithms=["HS256"])

    
#     return decoded_token