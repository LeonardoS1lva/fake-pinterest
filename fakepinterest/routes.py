from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCriarConta

@app.route("/", methods=["GET", "POST"])
def homepage():
    formLogin = FormLogin()
    return render_template("homepage.html", form=formLogin)

@app.route("/criar-conta", methods=["GET", "POST"])
def criar_conta():
    formCriarConta = FormCriarConta()
    return render_template("criar_conta.html", form=formCriarConta)

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
