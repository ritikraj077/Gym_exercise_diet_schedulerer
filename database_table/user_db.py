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
    
    
    
    
    
def user_login_db(Username,Password):
    query = f"SELECT * FROM members_database  WHERE Username = '{Username}' and Password = '{Password}'"
    cursor.execute(query)
    output = cursor.fetchone()
    if output:
        session['Username'] = Username
        name =  output["Name"]
        return f"{name} Login  sucessfully"
    else:
          return "Username and Password is Incorrect"
    
    
    



# def user_signup_db(Id,Username,Password):

#     query = f"INSERT INTO USER (Id, Username, Password) VALUES ('{Id}', '{Username}', '{Password}')"
#     cursor.execute(query)
#     cursor.fetchone()
#     con.commit()
#     return "sign_up complted sucessfully"




def user_delete_db(Username,Password):
     query = f"DELETE FROM members_database WHERE Username = {Username} and Password = {Password}"
     cursor.execute(query)
     con.commit()
     return " User deleted Sucessfully"




def sign_up_db(data):
    Id = data["Id"]
    Name= data["Name"]
    Age = data["Age"]
    Mobile = data["Mobile"]
    Email = data["Email"]
    Username = data["Username"]
    Password = data["Password"]
    
    query = f"INSERT INTO members_database (Id, Name, Age, Mobile, Email, Username, Password) VALUES ('{Id}', '{Name}', '{Age}','{Mobile}','{Email}' , '{Username}', '{Password}')"
    cursor.execute(query)
    data = cursor.fetchone()
    con.commit()
    return f" {Name}  registration Sucessfully completed"


