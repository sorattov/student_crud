from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.adapters.database.base import Base

# Modelo de Curso
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    # Relacionamento com alunos
    students = relationship("Student", back_populates="course")


# Modelo de Aluno
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    age = Column(Integer, nullable=False)

    # Relacionamento com curso
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="students")
