from fastapi import FastAPI
from app.adapters.database.base import Base
from app.adapters.database.session import engine
from app.adapters.routers import student_router

app = FastAPI()

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Incluir rotas
app.include_router(student_router.router)
