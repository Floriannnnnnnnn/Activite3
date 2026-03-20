
from flask import Flask, render_template, session, redirect
from questions import questions
from resultats import resultats, noms
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
        scores_sorted = sorted(session["score"], key = session["score"].get, reverse=True)

        gagnant = scores_sorted[0]

        nom_gagnant = noms[gagnant]

        resultats_description = resultats[gagnant]

        return render_template('resultats.html', nom_gagnant = nom_gagnant, resultats_description = resultats_description)

@app.route('/reponse/<numero>')
def reponse(numero):
    symbole = session["symboles"][int(numero)]
    session["score"][symbole] += 1

    session["numero_question"] += 1

    return redirect("/question")

app.run(host='192.168.3.16', port=81)