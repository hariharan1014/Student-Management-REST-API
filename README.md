# Student Management REST API

A RESTful Student Management System built with **Python** and **Flask**. This project demonstrates CRUD operations, input validation, modular project structure, and REST API development using a text file as the data storage.

---

## Features

- Add a new student
- View all students
- View a student by Roll Number
- Update student details
- Delete a student
- Search students by Department
- Search students by City
- Search students by First Name
- Search students by Last Name
- Search students by Age
- Input validation
- Duplicate Roll Number prevention
- File-based data persistence
- Modular project architecture

---

## Technologies Used

- Python 3
- Flask
- REST API
- JSON
- File Handling

---

## Project Structure

```
Student-Management-API/
│
├── app.py
├── management/
│   └── management.py
├── student/
│   └── student.py
├── utils/
│   └── validation.py
├── data/
│   └── student_list.txt
└── README.md
```

---

# API Endpoints

## Home

### GET /

Returns available API endpoints.

---

## Add Student

### POST /students

### Request Body

```json
{
    "roll_num": "101",
    "first_name": "Hari",
    "last_name": "R",
    "department": "AIML",
    "age": "21",
    "city": "Trichy",
    "phone_num": "9876543210"
}
```

### Success Response

**201 Created**

```json
{
    "success": true,
    "message": "Student added successfully",
    "student": {
        ...
    }
}
```

---

## Get All Students

### GET /students

Returns all students.

---

## Get Student by Roll Number

### GET /students/<roll_num>

Example

```
GET /students/101
```

Returns the student details if found.

Returns **404 Not Found** if the student does not exist.

---

## Update Student

### PUT /students/<roll_num>

Updates one or more student fields.

### Example Request

```json
{
    "city": "Chennai",
    "age": "22"
}
```

### Notes

- Roll Number cannot be modified.
- Invalid fields are rejected.
- Only provided fields are updated.

---

## Delete Student

### DELETE /students/<roll_num>

Deletes the specified student.

Returns **404 Not Found** if the student does not exist.

---

# Search APIs

## Search by Department

### GET /students/department/<department>

Example

```
GET /students/department/AIML
```

---

## Search by City

### GET /students/city/<city>

Example

```
GET /students/city/TRICHY
```

---

## Search by First Name

### GET /students/firstname/<first_name>

Example

```
GET /students/firstname/HARI
```

---

## Search by Last Name

### GET /students/lastname/<last_name>

Example

```
GET /students/lastname/KUMAR
```

---

## Search by Age

### GET /students/age/<age>

Example

```
GET /students/age/21
```

---

# Validation

The application validates:

- Required fields
- Integer values
- String values
- Phone number format
- Duplicate Roll Number
- Unknown fields during update
- Roll Number modification restriction

---

# Data Storage

Student records are stored in

```
data/student_list.txt
```

The application automatically loads records on startup and saves changes after every Create, Update, and Delete operation.

---

# Future Improvements

- SQLite / PostgreSQL database integration
- SQLAlchemy ORM
- Pagination
- Authentication & Authorization
- Logging
- Unit Testing
- Docker Support
- Deployment

---

# Learning Outcomes

This project demonstrates:

- Flask fundamentals
- REST API development
- CRUD operations
- Object-Oriented Programming
- Modular Python architecture
- File handling
- Data validation
- Dynamic attribute handling using `getattr()` and `setattr()`
- JSON request/response handling
- HTTP status codes