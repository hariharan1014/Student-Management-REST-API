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
