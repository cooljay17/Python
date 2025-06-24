#Use SQLAlchemy in the book management rest API 
# and store the data in a SQLite database
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from contextlib import asynccontextmanager

class BookBase(SQLModel):
    title: str = Field(index=True)   


class Book(BookBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author_name: str


class BookPublic(BookBase):
    id: int


class BookCreate(BookBase):
    author_name: str


class BookUpdate(BookBase):
    title: str | None = None
    author_name: str | None = None


sqlite_file_name = "test.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    # Here you can add any cleanup code if needed
app = FastAPI(lifespan=lifespan) 


@app.post("/books/", response_model=BookPublic)
def create_book(book: BookCreate, session: SessionDep):
    db_book = Book.model_validate(book)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


@app.get("/books/", response_model=list[BookPublic])
def read_books(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    books = session.exec(select(Book).offset(offset).limit(limit)).all()
    return books


@app.get("/books/{book_id}", response_model=BookPublic)
def read_book(book_id: int, session: SessionDep):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.patch("/books/{book_id}", response_model=BookPublic)
def update_book(book_id: int, book: BookUpdate, session: SessionDep):
    book_db = session.get(Book, book_id)
    if not book_db:
        raise HTTPException(status_code=404, detail="Book not found")
    book_data = book.model_dump(exclude_unset=True)
    book_db.sqlmodel_update(book_data)
    session.add(book_db)
    session.commit()
    session.refresh(book_db)
    return book_db


@app.delete("/books/{book_id}")
def delete_book(book_id: int, session: SessionDep):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(book)
    session.commit()
    return {"ok": True}