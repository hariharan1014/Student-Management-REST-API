from flask import Flask,request,jsonify
from management.management import Management


manager=Management()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({ "status" : 200,
        "message" : "Welcome to the home page",
        "contents" : "/students POST for add students"
    })

@app.route("/students" , methods = ['POST'])
def get_students():
   data = request.get_json()
   if not data:
       return jsonify({"message": "No data found"}), 400
   result= manager.add_student(data)
   return jsonify(result),result["status"]

if __name__ == "__main__":
    app.run(debug=True)