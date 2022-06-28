from flask import render_template
from application import app
from application.model.entity import produto

@app.route('/produtos')
def lista_produto():
    return render_template('produtos.html')