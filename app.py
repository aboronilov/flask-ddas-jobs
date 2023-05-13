from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': "Python developer",
        'location': "Bangkok, Thailand",
        'salary': "3 000 $"
    },
    {
        'id': 2,
        'title': "NodeJS developer",
        'location': "Bangkok, Thailand",
        'salary': "4 000 $"
    },
    {
        'id': 3,
        'title': "Go developer",
        'location': "Remote",
        'salary': "5 000 $"
    },
    {
        'id': 3,
        'title': "Rust developer",
        'location': "San Francisco, CA",
        'salary': "6 000 $"
    },
]


@app.route("/")
def main_page():
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

