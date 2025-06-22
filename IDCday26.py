#Develop a FastAPI application with endpoints to manage a library of books, including creating, 
# reading, updating, and deleting books
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
app = FastAPI()
class Book(BaseModel):
    id: int
    title: str

class BookCreate(BaseModel):
    title: str
       

class BookUpdate(BaseModel):
    title: Optional[str] = None
    id: Optional[int] = None

class BookInDB(Book):
    pass    
books_db: List[BookInDB] = []


@app.post("/Createbooks/", response_model=Book)
def create_book(book: BookCreate):
    new_book = BookInDB(id=len(books_db) + 1, title=book.title)
    books_db.append(new_book)
    return new_book  
   
@app.get("/Listbooks/", response_model=List[Book])
def read_books():
    return books_db   
  
@app.get("/Viewbooks/{book_id}", response_model=Book)
def read_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/Updatebooks/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate):
    for book in books_db:
        if book.id == book_id:
            if book_update.title is not None:
                book.title = book_update.title
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/Deletebooks/{book_id}", response_model=Book)
def delete_book(book_id: int):  
    for index, book in enumerate(books_db):
        if book.id == book_id:
            deleted_book = books_db.pop(index)
            return deleted_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/")
def read_root():    
    return {"message": "Welcome to the Book Library API!"}  



if __name__ == "__main__":
    uvicorn.run(app)    






