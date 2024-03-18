from flask import jsonify
from Database.Connection import database_connection



con = database_connection()
cursor = con.cursor()


def diet_plan_db(day):
    query= f"SELECT * FROM diet_plan WHERE day = '{day}'"
    cursor.execute(query)
    data = cursor.fetchall()
    return jsonify(data)