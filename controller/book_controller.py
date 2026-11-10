from typing import List
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from models.book_model import Book
from schema.book_schema import BookCreate

def get_all_books(db:Session, skip: int =0, limit:int = 100)-> List[Book]:
    try:
        return db.query(Book).offset(skip).limit(limit).all()
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Hay problemas en la conexión de base de datos:{str(error)}"
        )
        
def create_book(db:Session, book_data:BookCreate)->Book:
    
    new_book=Book(
        title=book_data.title,
        author=book_data.author,
        pages=book_data.pages,
        stock=book_data.stock
    )
    
    try:
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Hay problemas en la conexión de base de datos: {str(error)}"
        )
    