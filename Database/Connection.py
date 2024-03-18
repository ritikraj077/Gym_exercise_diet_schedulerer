######### Database connection #############
import mysql.connector






#Function to connect database 
def database_connection():

    try:

        con = mysql.connector.connect(host="localhost",
                                    user="ritik",
                                    password="Ritik@1234",
                                    database="gym_database"
                                    )

        print("connection established")
        return con
        
    except Exception as e:
        print(e)
        return "Error :"+str(e)
    
    
