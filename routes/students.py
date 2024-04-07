from fastapi import APIRouter
from config.db import conn
from models.student import Student, updatedStudent
from schemas.student import students, studentEntity
from bson import ObjectId

student = APIRouter(prefix='/students')

db = conn.test

# route to get all students
@student.get('/', status_code=200)
async def find_all_students(country: str | None = None, age: int | None = None):
    result = students(db.students.find())
    if(country==None and age==None):
        return {"data" : result}
    
    if(country != None):
        result = students(db.students.find({"address.country": country}))
    if(age == None):
        return {"data": result}
    
    filter_age = []
    if(age != None):
        for element in result:
            if(element["age"] >= age):
                filter_age.append(element)
    result=filter_age
    return {"data": result}

# route to get one student by id
@student.get('/{id}', status_code=200)
async def find_one_student(id):
    if(db.students.find_one({"_id": ObjectId(id)})):
        return studentEntity(db.students.find_one({"_id": ObjectId(id)}))

# route to create new student:
@student.post('/', status_code=201)
async def create_student(student: Student):
    result = (db.students.insert_one(dict(student))).inserted_id
    return {"id": str(result)}

# route to update a student:
@student.patch('/{id}', status_code=204)
async def update_user(id : str, student: updatedStudent):
    student=dict(student)
    if(db.students.find_one({"_id": ObjectId(id)})):
        student_from_db = studentEntity(db.students.find_one({"_id": ObjectId(id)}))
        
        for key, value in student.items():
            if(value==None):
                student[key]=student_from_db[key]

        db.students.find_one_and_update({"_id": ObjectId(id)}, {
            "$set": student
        })
    return {}

# route to delete a student:
@student.delete('/{id}', status_code=200)
async def delete_user(id):
    if(db.students.find_one({"_id": ObjectId(id)})):
        studentEntity(db.students.find_one_and_delete({"_id": ObjectId(id)}))
    return {}