# FastAPI REST APIs Starter Code

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="Student Management API", version="1.0.0")

# TODO: Define your Pydantic models here
class Student(BaseModel):
    id: int
    name: str
    email: str
    age: int
    grade: str

class Book(BaseModel):
    id: int
    title: str
    author: str
    publication_year: int
    genre: str
    available: bool = True

# In-memory storage (replace with database in real applications)
students_db = []
books_db = []

# TODO: Implement your API endpoints here

@app.get("/")
async def root():
    """
    Basic hello world endpoint
    TODO: Implement this endpoint
    """
    pass

@app.get("/hello/{name}")
async def hello_name(name: str):
    """
    Personalized greeting endpoint
    TODO: Implement this endpoint
    """
    pass

# Student endpoints
@app.get("/students")
async def get_students():
    """
    Get all students
    TODO: Implement this endpoint
    """
    pass

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    """
    Get a specific student by ID
    TODO: Implement this endpoint
    """
    pass

@app.post("/students")
async def create_student(student: Student):
    """
    Create a new student
    TODO: Implement this endpoint
    """
    pass

@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    """
    Update an existing student
    TODO: Implement this endpoint
    """
    pass

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    """
    Delete a student
    TODO: Implement this endpoint
    """
    pass

# Book endpoints
@app.get("/books")
async def get_books(genre: Optional[str] = None, author: Optional[str] = None, available: Optional[bool] = None):
    """
    Get all books with optional filtering
    TODO: Implement this endpoint with query parameters
    """
    pass

@app.post("/books")
async def create_book(book: Book):
    """
    Add a new book
    TODO: Implement this endpoint
    """
    pass

@app.put("/books/{book_id}/checkout")
async def checkout_book(book_id: int):
    """
    Check out a book (mark as unavailable)
    TODO: Implement this endpoint
    """
    pass

@app.put("/books/{book_id}/return")
async def return_book(book_id: int):
    """
    Return a book (mark as available)
    TODO: Implement this endpoint
    """
    pass

@app.get("/books/search")
async def search_books(q: str):
    """
    Search books by title or author
    TODO: Implement this endpoint
    """
    pass

if __name__ == "__main__":
    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=8000)
