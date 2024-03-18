from flask import jsonify
from Database.Connection import database_connection



con = database_connection()
cursor = con.cursor()




def workout_plan_db(day):
    query = f"SELECT * FROM workout_plan WHERE day = '{day}'"
    cursor.execute(query)
    data = cursor.fetchone()
    return jsonify(data)




def verify_user_auth(username):
    query = f"SELECT * FROM  members_database WHERE Username = '{username}'" 
    cursor.execute(query)
    data = cursor.fetchone()
    
    return data