# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, fast REST APIs using the FastAPI framework. By completing this assignment, you'll understand how to create web APIs that can handle HTTP requests, work with JSON data, and implement basic CRUD operations for real-world applications.

## 📝 Tasks

### 🛠️ Basic FastAPI Setup and Hello World

#### Description
Create your first FastAPI application with a simple endpoint that returns a greeting message. This will introduce you to the FastAPI framework basics and help you understand how web APIs work.

#### Requirements
Your completed program should:

- Install FastAPI and uvicorn using pip
- Create a basic FastAPI app instance
- Implement a GET endpoint at "/" that returns a JSON greeting message
- Include a GET endpoint at "/hello/{name}" that accepts a name parameter and returns a personalized greeting
- Run the server and test the endpoints in a browser or API testing tool
- Include proper HTTP status codes and response formatting


### 🛠️ Student Management API

#### Description
Build a RESTful API for managing student records with full CRUD (Create, Read, Update, Delete) operations. This will help you practice working with different HTTP methods and data persistence.

#### Requirements
Your completed program should:

- Create a Student model with fields: id, name, email, age, and grade
- Implement GET /students endpoint to retrieve all students
- Implement GET /students/{id} endpoint to retrieve a specific student
- Implement POST /students endpoint to create a new student
- Implement PUT /students/{id} endpoint to update an existing student
- Implement DELETE /students/{id} endpoint to remove a student
- Use in-memory storage (Python list/dictionary) for simplicity
- Include proper error handling for invalid requests (404, 400 status codes)
- Return appropriate JSON responses for all operations


### 🛠️ Book Library API with Query Parameters

#### Description
Create a more advanced API for managing a book library that demonstrates query parameters, data validation, and filtering capabilities. This will enhance your understanding of API design patterns.

#### Requirements
Your completed program should:

- Create a Book model with fields: id, title, author, publication_year, genre, and available
- Implement GET /books endpoint with optional query parameters for filtering (genre, author, available)
- Implement POST /books endpoint to add new books with data validation
- Implement PUT /books/{id}/checkout to mark a book as checked out (available=False)
- Implement PUT /books/{id}/return to mark a book as returned (available=True)
- Include search functionality with GET /books/search?q={query} that searches titles and authors
- Add proper Pydantic models for request/response validation
- Include comprehensive error messages and status codes
- Document your API endpoints with FastAPI's automatic documentation
