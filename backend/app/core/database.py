#Database connection and session management using SQLAlchemy

import psycopg2
from app.core.config import settings

def get_db_connection():
    return psycopg2.connect(settings.DB_URL)

def init_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS uretim_hatti (
                id SERIAL PRIMARY KEY,
                kayit_zamani TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                motor_sicaklik FLOAT,
                enerji_kw FLOAT,
                toplam_uretim INT,
                hatali_uretim INT
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("Veritabanı Tabloları Hazır!")
    except Exception as e:
        print("DB Hatası:", e)