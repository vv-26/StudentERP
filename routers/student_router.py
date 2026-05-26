from fastapi import APIRouter, Depends

from schemas.student_schema import StudentCreate, StudentResponse, StudentUpdate

from sqlalchemy.orm import Session
from dependency import get_db

from services.student_service import Service 

service = Service()

class Router:

    def __init__(self):
        self.router = APIRouter(tags=["student"])
        self.router.post("/add_student",response_model = StudentResponse, status_code=201)(self.add_student)
        self.router.get("/all_students", response_model=list[StudentResponse])(self.all_students)
        self.router.get("/student/{id}", response_model=StudentResponse)(self.get_student_by_id)
        self.router.put("/update/{id}", response_model=StudentResponse)(self.update_student)
        self.router.delete("/delete/{id}")(self.delete_student)

    def add_student(self,stud : StudentCreate, db:Session = Depends(get_db)):
        return service.addNewStudent(db,stud)

    def all_students(self,db:Session = Depends(get_db)):
        return service.getAllStudents(db)

    def get_student_by_id(self,id : int, db:Session = Depends(get_db)):
        return service.getStudentById(db,id)

    def update_student(self,id:int, stud:StudentUpdate, db:Session = Depends(get_db)):
        return service.updateStudentById(db,id,stud)

    def delete_student(self,id:int, db:Session = Depends(get_db)):
        return service.deleteStudentById(db,id)
