from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    address: dict

class updatedStudent(BaseModel):
    name: str | None = None
    age: int | None = None
    address: dict | None = None