from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# URL de conexión para SQLite (archivo local)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Para PostgreSQL sería asi:
# SQLALCHEMY_DATABASE_URL = "postgresql://usuario:contraseña@localhost/nombre_db"

# Crear el motor de SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear una clase Base que será la base para nuestros modelos
Base = declarative_base()


