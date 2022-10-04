from dojo_encuesta import app
from flask import render_template, request, redirect, session
from flask import Flask


@app.route('/')
def index():
    return render_template("encuesta.html")

@app.route('/process', methods=["POST"])
def formulaire():
    print(request.form) #Que contiene el formulario

    #data = {
    #    'nombre':request.form['name'],
    #    'ciudad':request.form['ciudad'],
    #    'lenguaje':request.form['lenguaje'],
    #    'comentarios':request.form['comentarios']
    #}

    session['nombre'] = request.form['name']
    session['ciudad'] = request.form['city']
    session['lenguaje'] = request.form['lengua']
    session['comentarios'] = request.form['comments']

    return redirect('/result')


@app.route('/result')
def datos():
    print(session) 
    return render_template("datos.html")


if __name__ == '__main__':
    app.run(debug= True)

