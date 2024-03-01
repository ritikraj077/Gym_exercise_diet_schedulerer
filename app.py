from flask import Flask
from flask import Flask, render_template, redirect, request, session
from flask_session import Session




app = Flask(__name__)
app.config['SECRET_KEY'] = "93168340169316834016"



@app.route("/")
def Welcome_screeen():
    # if not session.get("name"):
    #     # if not there in the session then redirect to the login page
    #     return redirect("/login")
    return "Welcome to the Wellness fitness center "
    
    
#from cantrol import router_user, member
from cantrol import router_user
