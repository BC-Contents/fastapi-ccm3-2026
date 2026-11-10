from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class BookBase(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=150,
        description="Title of the book",
        examples=["Don Quijote"]
    )
    author: str = Field(
            ...,
            min_length=1,
            max_length=100,
            description="Author of the book",
            examples=["Miguel de Cervantes"]
    )
    pages: Optional[int] = Field(
        None,
        gt=0,
        description="Total page",
        examples=[850]
    )
    stock: bool = Field(
        default=True,
        description="Flag indicating",
        examples=[True]
    )
    
class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int = Field(...,description="Identify",examples=[1])
    
    model_config= ConfigDict(from_attributes=True)