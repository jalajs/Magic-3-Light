from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import random
import time

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

device_id = 'e00fce681a2443bc6afde9d4'
access_token = '?access_token=aa1c16a8b44996a0616072ccdbcbb55bdb4a7eb1'
URL = 'https://api.particle.io/v1/devices/'
FLASH_URL = URL + device_id + '/flash' + access_token


class QuestionEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    response = db.Column(db.String(10))
    time = db.Column(db.DateTime)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/history", methods=['GET'])
def history():
    questions = QuestionEntry.query.all()
    return render_template('history.html', questions=questions)


@app.route('/answer', methods=['GET'])
def answer():
    return render_template('answer.html')


if __name__ == '__main__':
    app.run(debug=True)


@app.route("/ask", methods=['POST'])
def ask():
    led = random.randint(1, 3)
    print(led)
    random.seed(random.randint(0, 1000))
    requests.post(
        url='https://api.particle.io/v1/devices/e00fce681a2443bc6afde9d4/flash?access_token=5dbeb57e8bb4de81818be3c2d96ca7b093cb6617',
        data={'content': str(led)})

    time.sleep(5)

    ques = QuestionEntry(question=request.form['questionInput'], time=datetime.now(), response=get_choice(led))
    db.session.add(ques)
    db.session.commit()

    return render_template('answer.html', answer=get_choice(led), question=request.form['questionInput'])


def get_choice(led):
    if led == 1:
        return "Yes"
    elif led == 2:
        return "No"
    else:
        return "Maybe"
