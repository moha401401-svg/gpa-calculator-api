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
            CS DECIMAL(5,2),
            Math1 DECIMAL(5,2),
            Discrete DECIMAL(5,2),
            Elctronics DECIMAL(5,2),
            Creative_thinking DECIMAL(5,2),
            Technical_writing DECIMAL(5,2),
            GPA DECIMAL(5,2)
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
            CS DECIMAL(5,2),
            Discrete DECIMAL(5,2),
            Elctronics DECIMAL(5,2),
            Creative_thinking DECIMAL(5,2),
            Technical_writing DECIMAL(5,2),
            GPA DECIMAL(5,2)
        )
        ''')
        db.commit()
        cr.close()
        db.close()
        print("✅ Database is ready!")

