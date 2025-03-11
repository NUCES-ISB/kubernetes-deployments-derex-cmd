from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_NAME = os.getenv("POSTGRES_DB", "omerdb")
DB_USER = os.getenv("POSTGRES_USER", "omer")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "omer")
DB_HOST = os.getenv("POSTGRES_HOST", "postgres-service")

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST
        )
        return conn
    except Exception as e:
        return str(e)

@app.route("/")
def index():
    conn = connect_db()
    if isinstance(conn, str):
        return f"Database connection failed: {conn}"
    return "Connected to PostgreSQL successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
