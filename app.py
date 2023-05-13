from flask import Flask, render_template, jsonify
from sqlalchemy import text
from database import load_jobs_from_db

app = Flask(__name__)

@app.route("/")
def main_page():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

