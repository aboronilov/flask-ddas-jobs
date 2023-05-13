import os
from sqlalchemy import create_engine, text, engine
from dotenv import load_dotenv
load_dotenv()

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
URI = f"mysql+pymysql://{LOGIN}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4"

engine = create_engine(
    URI,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs;"))
        jobs = []
        for row in result.all():
            jobs.append(row)
        return jobs