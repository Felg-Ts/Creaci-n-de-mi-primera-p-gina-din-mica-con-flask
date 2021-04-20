from flask import Flask, render_template
app = Flask(__name__)	

@app.route('/')
def principal():
    return render_template("principal.html")


@app.route('/potencia/<int:bp>/<int:ep>/', methods=["GET","POST"])
def potencia(bp, ep):
    if ep <= -1:
        ep2 = ep * -1
        return render_template("potencia.html", base=bp, exponente=ep, solucion=bp**ep, solucion2=bp**ep2)
    else:
        return render_template("potencia.html", base=bp, exponente=ep, solucion=bp**ep)

@app.route('/cuentaletras/')
def cuentaletras():

    return render_template("cuentaletras.html")



app.run("0.0.0.0",5000,debug=True)