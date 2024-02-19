
from flask import Flask, request, jsonify
from app import app
import mysql.connector





#### database connectivity at this place only 
##because this connectivity i am mainly doint the have the large database that who attenden the gym  


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



def sign_up_db(data):
    Id = data["Id"]
    Name= data["Name"]
    Age = data["Age"]
    Mobile = data["Mobile"]
    Email = data["Email"]
    Username = data["Username"]
    Password = data["Password"]
    
    query = f"INSERT INTO USER (Id, Name, Age, Mobile, Email, Username, Password) VALUES ('{Id}', '{Name}', '{Age}','{Mobile}','{Email}' , '{Username}', '{Password})"
    cursor.execute(query)
    con.commit()

