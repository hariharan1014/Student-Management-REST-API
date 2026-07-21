# Student Management REST API

A simple REST API built with Flask for managing student records.

## Features

- Add Student
- Input Validation
- Duplicate Roll Number Check
- File-based Storage
- JSON Responses
- Tested using Postman

## Technologies Used

- Python
- Flask
- REST API
- JSON

## API

### Add Student

**POST**

```
/students
```

### Example Request

```json
{
    "roll_num": "101",
    "first_name": "Saba",
    "last_name": "Joe",
    "department": "AIML",
    "age": "21",
    "city": "Trichy",
    "phone_num": "9876543210"
}
```

### Example Success Response

```json
{
    "success": true,
    "message": "Student added successfully",
    "student": {
        "roll_num": "101",
        "first_name": "Saba",
        "last_name": "Joe",
        "department": "AIML"
    }
}
```
## API Endpoints

### Home

| Method | Endpoint | Description                                       |
| ------ | -------- | ------------------------------------------------- |
| GET    | `/`      | Displays API information and available endpoints. |

### Students

| Method | Endpoint    | Description                                 |
| ------ | ----------- | ------------------------------------------- |
| POST   | `/students` | Add a new student after validation.         |
| GET    | `/students` | Retrieve all students stored in the system. |

---

## Current Features

* Add a new student (`POST /students`)
* Retrieve all students (`GET /students`)
* Rule-based validation using function references
* Duplicate roll number detection
* Automatic loading of student records from file on application startup
* Automatic saving of student records after successful insertion
* Object-oriented design using a `Student` model with `to_dict()` serialization
* JSON responses with appropriate HTTP status codes

---

## Progress

* ✅ POST `/students`
* ✅ GET `/students`
* 🔄 GET `/students/<roll_num>`
* 🔄 PUT `/students/<roll_num>`
* 🔄 DELETE `/students/<roll_num>`
* 🔄 Database Integration (SQLite → PostgreSQL)
* 🔄 SQLAlchemy ORM
* 🔄 JWT Authentication

## Get Student by Roll Number

Returns the details of a specific student using the roll number.

### Endpoint

```http
GET /students/<roll_num>
```

### Success Response (200)

```json
{
    "success": true,
    "status": 200,
    "student": {
        "roll_num": 101,
        "first_name": "HARI",
        "last_name": "KUMAR",
        "department": "AIML",
        "age": 21,
        "city": "TRICHY",
        "phone_num": "9876543210"
    }
}
```

### Error Response (404)

```json
{
    "success": false,
    "status": 404,
    "message": "Student with roll number 101 does not exist"
}
```

---

## Update Student

Updates one or more details of an existing student.

> **Note:** `roll_num` cannot be modified because it is the unique identifier of a student.

### Endpoint

```http
PUT /students/<roll_num>
```

### Request Body (Example)

```json
{
    "city": "Chennai",
    "age": "22"
}
```

### Success Response (200)

```json
{
    "success": true,
    "status": 200,
    "message": "Student updated successfully",
    "student": {
        "roll_num": 101,
        "first_name": "HARI",
        "last_name": "KUMAR",
        "department": "AIML",
        "age": 22,
        "city": "CHENNAI",
        "phone_num": "9876543210"
    }
}
```

### Error Responses

#### Student Not Found (404)

```json
{
    "success": false,
    "status": 404,
    "message": "Student with roll number 101 does not exist for update."
}
```

#### Validation Error (400)

```json
{
    "success": false,
    "status": 400,
    "message": "Age should contain numbers"
}
```

#### Roll Number Modification Not Allowed (400)

```json
{
    "success": false,
    "status": 400,
    "message": "Roll number cannot be modified."
}
```

#### Unknown Field (400)

```json
{
    "success": false,
    "status": 400,
    "message": "Unknown field: salary"
}
```