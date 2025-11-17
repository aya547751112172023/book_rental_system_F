from pydantic import BaseModel


class Insert_Student(BaseModel):
    full_name: str
    year_level: int
    department: str


class Delete_Student(BaseModel):
    student_id: int


class Student(Insert_Student, Delete_Student):
    pass
