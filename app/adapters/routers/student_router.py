from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.adapters.database.session import SessionLocal
from app.domain.entities import StudentCreate, StudentResponse, CourseCreate, CourseResponse
from app.usecases.student_usecases import (
    get_students,
    get_student,
    create_student,
    delete_student,
    get_courses,
    create_course,
)

router = APIRouter(prefix="/students", tags=["students"])


# Dependency para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Rotas para Cursos
@router.post("/courses/", response_model=CourseResponse)
def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
    """Cria um novo curso no banco de dados."""
    return create_course(db, course)


@router.get("/courses/", response_model=list[CourseResponse])
def list_courses(db: Session = Depends(get_db)):
    """Lista todos os cursos disponíveis."""
    return get_courses(db)


# Rotas para Alunos
@router.get("/", response_model=list[StudentResponse])
def list_students(db: Session = Depends(get_db)):
    """Lista todos os alunos cadastrados no banco de dados."""
    return get_students(db)


@router.get("/{student_id}", response_model=StudentResponse)
def retrieve_student(student_id: int, db: Session = Depends(get_db)):
    """Obtém detalhes de um aluno pelo ID."""
    student = get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.post("/", response_model=StudentResponse)
def create_new_student(student: StudentCreate, db: Session = Depends(get_db)):
    """Cria um novo aluno associado a um curso."""
    return create_student(db, student)


@router.delete("/{student_id}")
def remove_student(student_id: int, db: Session = Depends(get_db)):
    """Remove um aluno pelo ID."""
    if not delete_student(db, student_id):
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
