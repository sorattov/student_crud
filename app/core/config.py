POSTGRES_USER = "admin"  # Deve corresponder ao valor definido no docker-compose.yml
POSTGRES_PASSWORD = "admin"  # Deve corresponder ao valor definido no docker-compose.yml
POSTGRES_DB = "app_db"  # Deve corresponder ao valor definido no docker-compose.yml
POSTGRES_HOST = "postgres"  # Nome do serviço do banco de dados no docker-compose.yml

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"
)
