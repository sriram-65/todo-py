from flask import Flask , redirect , render_template , request , jsonify , url_for
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)

client = MongoClient("mongodb+srv://sriram65raja:1324sriram@cluster0.dejys.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['ai']
USERS = db["TODO"]


@app.route("/")
def home():
    value = USERS.find({} , {"_id":1 , "TODO":1})
    return render_template("index.html" , todo = value)


@app.route("/add" , methods=["POST"])
def add():
    try:
        
        Task = request.form.get("task")
        if not Task:
            return jsonify("Error Pls Provide the Task")
        
        Data = {
            "TODO" : Task
        }
        
        USERS.insert_one(Data)
        return redirect('/')
    except :
        return jsonify({"Error" : "Error on adding the todo"})
    

@app.route("/del/<post_id>" , methods=["POST"])
def delte(post_id):
    USERS.delete_one({"_id":ObjectId(post_id)})
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


