import mysql.connector as my
import os

def database():
    host = os.getenv("MYSQLHOST")
    user = os.getenv("MYSQLUSER")
    password = os.getenv("MYSQLPASSWORD")
    port = int(os.getenv("MYSQLPORT", 3306))
    dbname = os.getenv("MYSQLDATABASE")

    try:
        return my.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=dbname
        )
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return None
def initialize_db():
    db = database()
    if db:
        cr = db.cursor()
        cr.execute('''CREATE TABLE IF NOT EXISTS calcs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(25),
            CS INT,
            Math1 INT,
            Discrete INT,
            Elctronics INT,
            Creative_thinking INT,
            Technical_writing INT,
            GPA FLOAT 
        )''')
        db.commit()
        cr.close()
        db.close()
        print("✅ Database is ready!")


if __name__ == "__main__":
    initialize_db()