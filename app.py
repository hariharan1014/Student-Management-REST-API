from flask import Flask, jsonify, request
from management.management import Management
manager=Management()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "Student Management REST API",
        "version": "1.0",
        "author": "Hariharan R",
        "description": "RESTful API built using Flask for managing student records.",

        "endpoints": {
            "POST": {
                "/students": "Add a new student"
            },

            "GET": {
                "/students": "Get all students",
                "/students/<roll_num>": "Get student by roll number",
                "/students/sort/<field>": "Sort students",
                "/students/filter?field=value": "Filter students",
                "/students?page=1&limit=5": "Pagination"
            },

            "PUT": {
                "/students/<roll_num>": "Update student"
            },

            "DELETE": {
                "/students/<roll_num>": "Delete student"
            }
        }
    }), 200

@app.route("/students" , methods = ['POST'])
def post_students():
   data = request.get_json()
   if not data:
       return jsonify({"message": "No data found"}), 400
   result= manager.add_student(data)
   return jsonify(result),result["status"]

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

@app.route("/students", methods = ['GET'])
def pagination_or_get_students():
    page=request.args.get("page",type=int)
    limit=request.args.get("limit",type=int)
    if  page is None and  limit is None:
        all_students = manager.get_students()
        return jsonify(all_students)
    else:
        if  page is None or  limit is None:
            return jsonify({"message": "No data found"}), 404
        elif page < 1 or limit < 1 :
            return jsonify({
                        "success": False,
                        "status": 400,
                        "message": "Page and limit must be greater than 0."
                        }), 400
        else:
            result=manager.pagination(page,limit)
            return jsonify(result),result["status"]

if __name__ == "__main__":
    app.run(debug=True)