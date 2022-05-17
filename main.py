import mysql.connector

def insert_random(name, birthdate):
    mydb = mysql.connector.conect(
        user="aluno",
        password="aluno123",
        database="gso"
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        'insert into Pessoa (nome, nascimento) VALUES (%s, %s)', values
    )

    mydb.commit()


import names

from faker import Faker
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root_path():
    return jsonify(msg="It's running!", code=200)

@app.route("/pessoa/random", methods=["POST"])
def random_person():

    name = names.get_full_name()
    birthdate = Faker().date_between(
        start_date="-100y", end_date="-18y")

    response = {
        'nome' : name,
        'nascimento' :  birthdate
    }

    print(name, birthdate)
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=43333)