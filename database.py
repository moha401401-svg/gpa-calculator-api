import os
import mysql.connector
from urllib.parse import urlparse

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
