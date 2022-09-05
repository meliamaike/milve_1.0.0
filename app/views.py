from app import app
from flask import render_template, url_for

@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/public/login')
def login():
    return render_template("public/login.html")

@app.route('/public/reservar')
def reservar():
    return render_template("public/reservar.html")

@app.route('/public/registrar')
def registrar():
    return render_template("public/registrar.html")

@app.route('/public/olvido-password')
def olvido_password():
    return render_template("public/olvido-password.html")

@app.route('/public/reseteo-password')
def reset_password():
    return render_template("public/reset-password.html")

