
from flask import Flask, render_template, session
from questions import questions
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)




@app.route('/')
def index():

    session["numero_question"] = 0

    session["score"] = {"Sw": 0, "Ro": 0, "Ka": 0, "Me": 0}


    return render_template('index.html')

@app.route('/question')
def question():
    global questions

    numero = session["numero_question"]

    if numero < len(questions):
        enonce_question = questions[numero]["enonce"]

        symboles_et_reponse = questions[numero].copy()

        symboles_et_reponse.pop("enonce")

        reponses = list(symboles_et_reponse.values())
        symboles = list(symboles_et_reponse.keys())

        session["symboles"] = symboles

        return render_template('question.html', enonce = enonce_question, reponses = reponses, symboles = symboles)
    else:
        return render_template('resultat.html')


app.run(host='192.168.3.16', port=81)