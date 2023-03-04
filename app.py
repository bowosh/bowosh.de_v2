from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def load_projects_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from projects"))
    projects = result.mappings().all()
    return projects


@app.route("/")
def hello_world():
  jobs = load_projects_from_db()
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
