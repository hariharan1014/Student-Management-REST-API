from flask import Flask,request,jsonify
from management.management import Management


manager=Management()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({ "status" : 200,
        "message" : "Welcome to the home page",
        "contents" : "/students POST for add students \n"
                     "/students GET for display students \n"
    })

@app.route("/students" , methods = ['POST'])
def post_students():
   data = request.get_json()
   if not data:
       return jsonify({"message": "No data found"}), 400
   result= manager.add_student(data)
   return jsonify(result),result["status"]

@app.route("/students", methods = ['GET'])
def get_students():
    result=manager.get_students()
    return jsonify(result)

@app.route("/students/<int:roll_num>", methods = ['GET'])
def get_student(roll_num):
    result=manager.get_student_by_roll_num(roll_num)
    return jsonify(result),result["status"]


if __name__ == "__main__":
    app.run(debug=True)