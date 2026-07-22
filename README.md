# Student Management REST API (Flask)

A RESTful Student Management API built using **Python** and **Flask**.

This project demonstrates CRUD operations, validation, filtering, sorting, pagination, modular project structure, and file-based persistence without using a database.

---

## Features

- Add Student
- View All Students
- View Student by Roll Number
- Update Student Details
- Delete Student
- Sort Students
- Filter Students
- Pagination
- Input Validation
- File Storage
- Modular Project Structure
- Proper HTTP Status Codes
- JSON Responses

---

## Tech Stack

- Python 3
- Flask
- REST API
- JSON
- File Handling

---

## Project Structure

```
StudentManagement REST API/
│
├── app.py
│
├── management/
│   └── management.py
│
├── student/
│   └── student.py
│
├── utils/
│   └── validation.py
│
├── data/
│   └── student_list.txt
│
├── README.md
└── .gitignore
```

---

# Student Model

Each student contains:

| Field | Type |
|---------|------|
| roll_num | Integer |
| first_name | String |
| last_name | String |
| department | String |
| age | Integer |
| city | String |
| phone_num | String |

---

# API Endpoints

---

## Home

### GET /

Returns project information and available routes.

---

## Add Student

### POST /students

Creates a new student.

### Request Body

```json
{
    "roll_num": 101,
    "first_name": "Hari",
    "last_name": "Joe",
    "department": "ECE",
    "age": 22,
    "city": "Chennai",
    "phone_num": "9876543210"
}
```

### Success

**201 Created**

---

## Get All Students

### GET /students

Returns every student.

### Success

**200 OK**

---

## Get Student by Roll Number

### GET /students/<roll_num>

Example

```
GET /students/101
```

### Success

**200 OK**

Returns the requested student.

### Error

**404 Not Found**

Student does not exist.

---

## Update Student

### PUT /students/<roll_num>

Example

```
PUT /students/101
```

Only the fields you want to modify need to be sent.

Example

```json
{
    "city": "Coimbatore",
    "age": 23
}
```

### Success

**200 OK**

### Possible Errors

- 400 Bad Request
- 404 Not Found

---

## Delete Student

### DELETE /students/<roll_num>

Example

```
DELETE /students/101
```

### Success

**200 OK**

### Error

**404 Not Found**

---

# Sorting

Sort students using any supported field.

### GET

```
/students/sort/first_name
```

```
/students/sort/last_name
```

```
/students/sort/department
```

```
/students/sort/city
```

```
/students/sort/age
```

### Success

**200 OK**

### Error

**400 Bad Request**

Unknown field.

---

# Filtering

Filter students using one or multiple query parameters.

Example

```
GET /students/filter?department=ECE
```

Example

```
GET /students/filter?department=ECE&city=CHENNAI
```

Example

```
GET /students/filter?department=ECE&city=CHENNAI&age=22
```

### Success

**200 OK**

### Error

**400 Bad Request**

Unknown filter field.

---

# Pagination

Retrieve students page by page.

Example

```
GET /students?page=1&limit=5
```

Example

```
GET /students?page=2&limit=5
```

### Success

**200 OK**

Returns only the requested page.

---

# HTTP Status Codes Used

| Code | Meaning |
|------|---------|
|200|Success|
|201|Created|
|400|Bad Request|
|404|Not Found|
|409|Conflict|

---

# Validation

The project validates:

- Roll Number
- First Name
- Last Name
- Department
- Age
- City
- Phone Number

---

# Learning Outcomes

This project helped me understand:

- Flask Routing
- REST API Design
- CRUD Operations
- JSON Handling
- Input Validation
- File Handling
- Modular Project Structure
- Object-Oriented Programming
- Search Logic
- Sorting
- Filtering
- Pagination
- Proper HTTP Response Codes
- Clean Code Refactoring

---

# Future Improvements

- SQLite Integration
- PostgreSQL Integration
- SQLAlchemy ORM
- Authentication (JWT)
- Password Hashing
- Logging
- Unit Testing
- Docker
- Deployment