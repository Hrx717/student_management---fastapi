from fastapi import FastAPI
from routes.students import student

app = FastAPI()

app.include_router(student)
