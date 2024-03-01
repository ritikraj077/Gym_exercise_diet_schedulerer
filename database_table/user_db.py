import bcrypt

import mysql.connector
from flask import Flask, render_template, redirect, request, session, jsonify



try:

    con = mysql.connector.connect(host="localhost",
                                                user="root",
                                                password="Ritik@1234",
                                                database="gym_database"
                                                )
    cursor = con.cursor(dictionary=True)
    print("connection sucesssfull")
    
    
except Exception as e:
    print("Error :" ,e)
    
    
    
    
    

      
      
def user_login_db(Username, Password):
    
   
    
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(Password, salt)
    print(hashed)
    # check = bcrypt.checkpw(password=Password,hashed_password=hashed)
    # print(check)
    query = f"SELECT * FROM members_database WHERE Username = %s "
    cursor.execute(query,(Username,))
    output = cursor.fetchone()
    
    if output:
        stored_hashed_password = output["Password"].encode('utf-8')
        
        if bcrypt.checkpw(Password, stored_hashed_password):
            #print(check)
        
        

        # If user exists and password is correct, process the result
            session['Username'] = Username
            name = output["Name"]
            return f"{name} Login successfully"
        else:
            return "Username and Password are incorrect"

    




def user_delete_db(Username,Password):
     query = f"DELETE FROM members_database WHERE Username = {Username} and Password = {Password}"
     cursor.execute(query)
     con.commit()
     return " User deleted Sucessfully"




# def sign_up_db(data):
#     Id = data["Id"]
#     Name= data["Name"]
#     Age = data["Age"]
#     Mobile = data["Mobile"]
#     Email = data["Email"]
#     Username = data["Username"]
#     password = data["Password"].encode('utf-8')

#     salt = bcrypt.gensalt()
#     hashed = bcrypt.hashpw(password, salt)
#     query = f"INSERT INTO members_database (Id, Name, Age, Mobile, Email, Username, Password) VALUES ('{Id}', '{Name}', '{Age}','{Mobile}','{Email}' , '{Username}', '{hashed}')"
#     con.commit()
#     cursor.execute(query)
#     data = cursor.fetchone()
#     con.commit()
#     return f" {Name}  Registration Sucessfully completed"
def sign_up_db(data):
    Id = data["Id"]
    Name = data["Name"]
    Age = data["Age"]
    Mobile = data["Mobile"]
    Email = data["Email"]
    Username = data["Username"]
    password = data["Password"].encode('utf-8')

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    
    query = "INSERT INTO members_database (Id, Name, Age, Mobile, Email, Username, Password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (Id, Name, Age, Mobile, Email, Username, hashed))
    con.commit()

    return f"{Name} registration successfully completed"



def user_update_details_db(data):
    Id = data["Id"]
    Name = data["Name"]
    Age = data["Age"]
    Mobile = data["Mobile"]
    Email = data["Email"]
    password = data["Password"].encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    query = f"UPDATE INTO member_database SET  Name = {Name}, Age= {Age}, Mobile= {Mobile}, Email = {Email}, Password = {password} WHERE Id = {Id}"
    cursor.execute(query)
    con.commit()
    return f"User with Id {Id} updated successfully"

