from flask import render_template
from application import app
from application.model.entity import carrinho

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')