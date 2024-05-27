from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ns')
def ns():
    return render_template("ns.html")

@app.route('/fenex')
def fenex():
    return render_template("fenex.html")

@app.route('/huron')
def huron():
    return render_template("huron.html")

@app.route('/zorros')
def zorros():
    return render_template("zorros.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Comentarios = request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into comenta (correo,comentario) values (%s, %s)',(aux_Correo, aux_Comentarios))
        conn.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)