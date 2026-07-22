from flask import Flask, jsonify, request
from management.management import Management
manager=Management()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
  "project": "Student Management REST API",
  "version": "1.0",
  "author": "Hariharan.R",
  "available_routes": [
      { "POST" : "/students",
        "GET" : "/students",
        "get" : "/students/filterby(department,age,city,firstname,lastname)",
        "PUT" : "/students",
        "DELETE" : "/students"
       }
  ]
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
@app.route("/students/<int:roll_num>", methods = ['PUT'])
def update_student(roll_num):
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data found"}), 400
    result=manager.update_student(data,roll_num)
    return jsonify(result),result["status"]

@app.route("/students/<int:roll_num>", methods = ['DELETE'])
def delete_student(roll_num):
    result=manager.delete_student(roll_num)
    return jsonify(result),result["status"]

@app.route("/students/sort/<field>", methods = ['GET'])
def sort_field(field):
    result=manager.sort_students(field)
    return jsonify(result), result["status"]

@app.route("/students/filter", methods = ['GET'])
def filter_field():
    filters=request.args.to_dict()
    result=manager.filter_students(filters)
    return jsonify(result),result["status"]

if __name__ == "__main__":
    app.run(debug=True)