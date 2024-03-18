from flask import Flask 
from flask import Flask,request,jsonify,session,redirect
from Gym_exercise_diet_schedulerer.app import app
import os


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx'}

def allowed_file(filename):
    # Check if the file extension is in the allowed extensions set
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods =["POST"])
def upload_file():
    # file = request.files
    print(request.files)
    if 'file ' not in  request.files :
        
        return jsonify({"error": "no file part"})
    file = request.files['file ']
    if file.filename == '':
        return jsonify({'error':'no selected file'})
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'})
    upload_folder = r'C:\Users\rajri\Projects\gym_management\upload_file\uploaded_files'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file.save(os.path.join(upload_folder, file.filename))
    

    return jsonify({'message': 'File uploaded successfully', "success": True, 'path': r'C:\Users\rajri\Projects\gym_management\upload_file\uploaded_files'})

    
    
    
    
    
