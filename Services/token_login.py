import datetime
import jwt
SECRET_KEY = "Secret_key"



def generate_jwt_token(Username):
    
    # Generate JWT token with user's username and expiration time
    token_payload = {
        'Username': Username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expiration time
    }
    token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')
    return token

    