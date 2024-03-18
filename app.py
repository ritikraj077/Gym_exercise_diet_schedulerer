from flask import Flask


app = Flask(__name__)
@app.route("/")
def Welcome_Screen():
    
    return "This is the Welcome Screen"
app.config['SECRET_KEY'] = 'Secret_key1234'


from User import router
from Diet import router
from  Exercise import router
from Trainer import trainer_route
from upload_file import file_upload_router

if __name__ == '__main__':
    app.run(debug=True)