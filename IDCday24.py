#Create a dataclass to represent a library book with fields for title, author, ISBN, and publication year, including a method to display book details
from dataclasses import dataclass   

@dataclass(frozen=True)
class Book:     
    title: str
    author:str
    isbn: str
    publication_year: int
    def display_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Publication Year: {self.publication_year}"
 
def main(): 
    book = Book(title="Harvest Love", author="Melanie Moreland", isbn="1234567890", publication_year=2022)
    print(book.display_details()) 
    
main()


