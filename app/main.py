from fastapi import FastAPI
from app.routers import student, auth

app = FastAPI()
app.include_router(student.router)
app.include_router(auth.router)
