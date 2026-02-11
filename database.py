import os
import mysql.connector
from dotenv import load_dotenv
from urllib.parse import urlparse
load_dotenv()

def database():
    try:
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise Exception("DATABASE_URL not found")

        parsed = urlparse(database_url)

        conn = mysql.connector.connect(
            host=parsed.hostname,
            user=parsed.username,
            password=parsed.password,
            database=parsed.path.lstrip("/"),
            port=parsed.port,
            ssl_disabled=False
        )
        print("✅ Connected to Railway MySQL!")
        return conn

    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return None


def initialize_db():
    db = database()
    if db:
        cr = db.cursor()
        cr.execute('''
        CREATE TABLE IF NOT EXISTS calcs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(25),
            CS FLOAT,
            Math1 FLOAT,
            Discrete FLOAT,
            Elctronics FLOAT,
            Creative_thinking FLOAT,
            Technical_writing FLOAT,
            GPA FLOAT
        )
        ''')
        db.commit()
        cr.close()
        db.close()
        print("✅ Database is ready!")
def initialize_db2():
    db = database()
    if db:
        cr = db.cursor()
        cr.execute('''
        CREATE TABLE IF NOT EXISTS calcs2 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(25),
            CS FLOAT,
            Discrete FLOAT,
            Elctronics FLOAT,
            Creative_thinking FLOAT,
            Technical_writing FLOAT,
            GPA FLOAT
        )
        ''')
        db.commit()
        cr.close()
        db.close()
        print("✅ Database is ready!")
initialize_db2()

