from sqlalchemy.orm import Session
from app.adapters.database.models import Student, Course
from app.domain.entities import StudentCreate, CourseCreate


# Funções relacionadas a Cursos
def create_course(db: Session, course: CourseCreate):
    """
    Cria um novo curso no banco de dados.
    """
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def get_courses(db: Session):
    """
    Retorna todos os cursos cadastrados no banco de dados.
    """
    return db.query(Course).all()


# Funções relacionadas a Alunos
def get_students(db: Session):
    """
    Retorna todos os alunos cadastrados no banco de dados.
    """
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    """
    Retorna os detalhes de um aluno com base no ID fornecido.
    """
    return db.query(Student).filter(Student.id == student_id).first()


def create_student(db: Session, student: StudentCreate):
    """
    Cria um novo aluno no banco de dados e o associa a um curso.
    """
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def delete_student(db: Session, student_id: int):
    """
    Remove um aluno com base no ID fornecido.
    """
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return True
    return False
