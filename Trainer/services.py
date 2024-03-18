import mysql.connector

from Database.Connection import database_connection

con = database_connection()
cursor = con.cursor()

def trainer_table():
    query = '''
    CREATE TABLE IF NOT EXISTS trainers (
        Id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Specialty TEXT,
        Age INTEGER,
        Email TEXT
    );
    '''
    cursor.execute(query)
    con.commit()
    
    return "Table trainers created successfully"

def data():
    query = """INSERT INTO trainers (Id, Name, Specialty, Age, Email) 
               VALUES 
               (1, 'Rohit Sharma', 'Upperbody trainer (Diet, Nutrition)', 26, 'Rohit223@gmail.com'),
               (2, 'Anand Kumar', 'Full body trainer (dietician)', 25, 'anand&&*@gmail.com'),
               (3, 'Ritik Raj', 'Full body muscles gainer (dietician, Physician)', 23, 'ritik887@gmail.com')
            """
    cursor.execute(query)
    con.commit()
    return "Details added successfully"




def get_all_trainers():
    query = "SELECT * FROM trainers"
    cursor.execute(query)
    fetch_all = cursor.fetchall()
    
    
    trainers = []
    for row in fetch_all:
        name = row[1]  # Accessing the first column (Name)
        speciality = row[2]  # Accessing the second column (speciality)
        email = row[3]  # Accessing the third column (Email)
        trainers.append({"Name": name, "speciality": speciality, "Email": email})
    
    return trainers

