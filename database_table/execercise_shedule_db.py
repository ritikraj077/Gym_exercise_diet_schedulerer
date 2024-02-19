import mysql.connector
from flask import jsonify


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
    
 ##this function is used to show to the workout for the particular day of the week by taking in put day as a query parameter in router_user.py file in exercise api   
def workout_plan_db(day):
    query = f"SELECT * FROM workout_plan WHERE day = '{day}'"
    cursor.execute(query)
    data = cursor.fetchone()
    return jsonify(data)


