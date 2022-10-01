from flask import Flask, render_template, redirect, session
app = Flask(__name__)
# nuestra ruta de índice manejará la representación de nuestro formulario
app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta

@app.route('/')
def counter():
    if 'num' in session:
        session ['num'] += 1
    else:
        session['num'] = 1
    return render_template("index.html")

@app.route('/sumar')
def sumar():
    session['num'] += 1
    return redirect('/')

@app.route('/destroy_session')
def eliminar():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

