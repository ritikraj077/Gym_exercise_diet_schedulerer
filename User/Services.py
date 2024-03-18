from pydantic import BaseModel
from Database.Connection import database_connection
import bcrypt
from flask import jsonify, session
import json
import mysql.connector
from User.mobile_number_validation import isValid

SECRET_KEY = 'Secret_key1234'


con = database_connection()
cursor = con.cursor()


def sign_up_db(user_obj):
    try:
        query = "INSERT INTO members_database (Name, Age, Mobile, Email, Username, Password) VALUES (%s, %s, %s, %s, %s, %s)"
        print(user_obj)
        print(user_obj.Name)
        
        # hashing user password
        salt = bcrypt.gensalt()
        user_obj.Password =  bcrypt.hashpw(user_obj.Password.encode('utf-8'), salt)
        validate = isValid(user_obj.Mobile)
        if not validate:
            return "Invalid Mobile Number"
        cursor.execute(query, (user_obj.Name, user_obj.Age, user_obj.Mobile, user_obj.Email, user_obj.Username, user_obj.Password))
        con.commit()
        return {"massage":f"{user_obj.Name} registration successfully completed"}
    
           
    except Exception as e:
        return {"status_code":422,"success":False, "message":str(e)}
    
     
    
    
def check_registration_user(user_data):
    Username = user_data["Username"]
    Mobile = user_data["Mobile"]
    query =  f" SELECT * FROM members_database WHERE Username = '{Username}' AND Mobile = '{Mobile}'"
    cursor.execute(query)
    output = cursor.fetchone()
    return output

    
def user_login_db(user_data):
    try:
        query = "SELECT * FROM members_database WHERE Username = %s "
        cursor.execute(query,(user_data[0],))
        output = cursor.fetchone()
        print(output)
        
        if output:
            stored_hashed_password = output[6].encode('utf-8')
            
            if bcrypt.checkpw(user_data[1], stored_hashed_password):
                session['Username'] = user_data[0]
                name = output[1]
                return f"{name} Login successfully"
            else:
                return "Username and Password are incorrect"
        else:
                return "User not found"
    except mysql.connector.Error as err:
        print("Error:", err)
        return "An error occurred during login"

    
    
    
def user_delete_db(user_data):
    query = "SELECT * FROM members_database Where Username = %s"
    cursor.execute(query,(user_data[0],))
    output = cursor.fetchone()
    print(output)
    
    if output:
        
        stored_hashed_password = output[6].encode('utf-8')
            
        if bcrypt.checkpw(user_data[1], stored_hashed_password):
            query1 = "DELETE FROM members_database WHERE Username = %s"
            cursor.execute(query1, (user_data[0],))
            con.commit()
            return " User deleted Sucessfully"
        else:
            return "Incorrect password"
    else:
        return "User not found"
    
    
    






def user_update_db(user_data):
    query = "UPDATE members_database SET Name = %s, Age = %s, Mobile = %s, Email = %s, Username = %s WHERE Id = %s"
    
    cursor.execute(query, (user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[0]))

    con.commit()
    return f"User with username {user_data[5]} updated successfully"





def forget_password_db(user_data):
    query = "UPDATE members_database  SET Password = %s WHERE Username = %s"
    salt = bcrypt.gensalt()
    hashed_Password =  bcrypt.hashpw(user_data[1].encode('utf-8'), salt)
    cursor.execute(query,(user_data[1],user_data[0]))
    con.commit()
    return "Password updated Sucessfully"




