import mysql.connector as my
import os

def database():
    # بنجرب نجيب بيانات ريل واي، لو مش موجودة (لوكل) بيستخدم الـ default
    host = os.getenv("MYSQLHOST", "localhost")
    user = os.getenv("MYSQLUSER", "root")
    password = os.getenv("MYSQLPASSWORD", "12345678") # حط باسورد جهازك هنا
    port = int(os.getenv("MYSQLPORT", 3306))
    dbname = os.getenv("MYSQLDATABASE", "GPA")

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

# دالة لتهيئة الجدول عشان م تضربش والسيرفر بيقوم
def initialize_db():
    db = database()
    if db:
        cr = db.cursor()
        # جرب تغير DECIMAL لـ FLOAT لو لسه فيه مشاكل
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

# نادى الدالة دي في بداية تشغيل main.py أو هنا
if __name__ == "__main__":
    initialize_db()