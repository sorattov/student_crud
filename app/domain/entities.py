from pydantic import BaseModel
from typing import Optional

# Esquema de Curso
class CourseBase(BaseModel):
    name: str

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int

    class Config:
        orm_mode = True


# Esquema de Aluno
class StudentBase(BaseModel):
    name: str
    email: str
    age: int
    course_id: int  # Relaciona o aluno a um curso pelo ID

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    course: Optional[CourseResponse]  # Inclui informações do curso no retorno

    class Config:
        orm_mode = True
