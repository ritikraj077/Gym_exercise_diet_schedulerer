from app import app
from Trainer.services import trainer_table, data, get_all_trainers

@app.route("/all_trainers", methods = ["GET"])
def all_trainer():
    return get_all_trainers()



@app.route("/create_table", methods = ["GET"]) 
def create_table():
    table = trainer_table()
    trainers  = data()
   
    return table, trainers



# @app.route("/trainer_list", methods = ["GET"])
# def trainer():
#     return get_all_trainers()
    