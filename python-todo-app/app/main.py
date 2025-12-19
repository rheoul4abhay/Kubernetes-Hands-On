from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.getenv("DB_PATH", "todo.db")
SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY,
                task TEXT
            )
        """)
        conn.commit()

@app.route("/", methods=["GET", "POST"])
def index():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        if request.method == "POST":
            task = request.form.get("task")
            if task:
                cursor.execute("INSERT INTO todos (task) VALUES (?)", (task,))
                conn.commit()
            return redirect(url_for("index"))
        cursor.execute("SELECT * FROM todos")
        todos = cursor.fetchall()
    return render_template("index.html", todos=todos)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
