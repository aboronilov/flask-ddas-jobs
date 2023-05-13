import os
from sqlalchemy import create_engine, text, engine
from dotenv import load_dotenv
load_dotenv()

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
URI = f"mysql+pymysql://{LOGIN}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4"
# sql_url = engine.url.URL(
#     drivername="mysql+pymysql",
#     username=LOGIN,
#     password=PASSWORD,
#     host=HOST,
#     port=3306,
#     database=DATABASE,
#     query={"ssl_ca": "main_app/certs/BaltimoreCyberTrustRoot.crt.pem"},
# )

engine = create_engine(
    URI,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    print(result.all())
