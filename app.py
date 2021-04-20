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

@app.route('/cuenta/<string:palabra>/<string:letra>/')
def cuentaletras(palabra, letra):
    cont = 0

    for i in palabra:
        if i == letra:
            cont = cont + 1
    rels = (f"En la palabra {palabra} aparece {cont} veces el carácter {letra}")
    return render_template("cuentaletras.html", aparece=rels)



app.run("0.0.0.0",5000,debug=True)
