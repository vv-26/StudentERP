
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.student_model import Student
from schemas.student_schema import StudentCreate, StudentUpdate


class Service:
    
    def addNewStudent(self,db:Session, stud:StudentCreate):
        student = Student(
            name = stud.name,
            dept = stud.dept,
            program = stud.program,
            DOB = stud.DOB,
            batch = stud.batch,
            email = stud.email
        )
        if db.query(Student).filter(Student.email == student.email).first():
            raise HTTPException(409,"Student email already registered")
        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    
    def getAllStudents(self,db:Session):
        return db.query(Student).all()

    
    def getStudentById(self,db:Session, id:int):
        student = db.query(Student).filter(Student.stuid == id).first()
        if student:
            return student
        raise HTTPException(404,"No such student")

    
    def updateStudentById(self,db:Session, id:int, stud:StudentUpdate):
        student = db.query(Student).filter(Student.stuid == id).first()
        if not student:
            raise HTTPException(404, "No such student")
        
        update_data = stud.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(student, key, value)
        db.commit()
        db.refresh(student)

        return student

    
    def deleteStudentById(self,db:Session, id:int):
        student = db.query(Student).filter(Student.stuid == id).first()
        if not student:
            raise HTTPException(404,"No such student")
        db.delete(student)
        db.commit()
        return "Deleted successfully"
