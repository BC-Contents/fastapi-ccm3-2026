from typing import List
from fastapi import APIRouter,Depends, HTTPException, Query,status
from sqlalchemy.orm import Session

from database.database import get_db
import controller.book_controller as controller
from schema.book_schema import BookCreate, BookResponse


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get(
    "/",
    response_model=List[BookResponse], 
    summary="Lectura libros"
)
def read_books(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=100, description="Maximum number of records to return"),
    db: Session = Depends(get_db)
):
    return controller.get_all_books(db=db, skip=skip, limit=limit)


@router.post(
    "/",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new book",
    description="Add a new book entry to the library catalog."
)
def create_new_book(
    book_data: BookCreate,
    db: Session = Depends(get_db)
):
    return controller.create_book(db=db, book_data=book_data)