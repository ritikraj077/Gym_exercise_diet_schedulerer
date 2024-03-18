import bcrypt
import datetime
import jwt
from app import app
from User.mobile_number_validation import isValid
from pydantic import BaseModel





# class Registration(BaseModel):
#     def __init__(self, Name: str, Age: int, Mobile: str, Email: str, Username: str, Password: str):
#         if not isinstance(Name, str):
#             raise TypeError("Name must be a string")
#         if not isinstance(Age, int):
#             raise TypeError("Age must be an integer")
#         if not isinstance(Mobile, str) or not Mobile.isdigit() or len(Mobile) != 10:
#             raise TypeError("Mobile must be a string of 10 digits")
#         if not isinstance(Email, str):
#             raise TypeError("Email must be a string")
#         if not isinstance(Username, str):
#             raise TypeError("Username must be a string")
#         if not isinstance(Password, str):
#             raise TypeError("Password must be a string")


class Registration(BaseModel):
    Name: str
    Age: int
    Mobile: str # Mobile number as a string of 10 digits
    Email: str
    Username: str
    Password: str
    




class login:
    def __init__(self,data):
        self.username = data["Username"]
        self.password = data["Password"].encode('utf-8')
        #self.salt = bcrypt.gensalt()
        #self.hashed: str =  bcrypt.hashpw(self.password, self.salt)
    def get_login_data(self):
        return (self.username, self.password)
    



    def generate_jwt_token(data,SECRET_KEY):
    
        # Generate JWT token with user's username and expiration time
        username = data["Username"]
        token_payload = {
            'Username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)  # Token expiration time
        }
        token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')
    
        return token

    
    
class delete:
    def __init__(self,data):
        self.username = data["Username"]
        self.password = data["Password"].encode('utf-8')
        
    def delete_user_data(self):
        return (self.username, self.password)







class update:
    def __init__(self,data):
        print(data)
        self.Id = data["Id"]
       
       
        self.Name = data["Name"]
        self.Age = data["Age"]
        self.Mobile = data["Mobile"]
        self.Email = data["Email"]
        self.username= data["Username"] 
    def update_user_data(self):
        return(self.Id, self.Name, self.Age, self.Mobile, self.Email, self.username)
    
    
    
    
    
    
class forget_pass:
    def __init__(self,data):
        self.Username =  data["Username"]
        self.Password = data["Password"]
        
    def password_username(self):
        return(self.Username,self.Password)