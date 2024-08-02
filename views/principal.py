from flask import render_template, request, redirect, session, url_for
from app import app, db
from models import Usuarios
from views.pedidos import pedido

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perfil')
def perfil():
    matricula = session['usuario_logado']
    usuario = Usuarios.query.filter_by(matricula = matricula).first()
    if usuario.adm == False:
        matricula = session['usuario_logado']
        usuario = Usuarios.query.filter_by(matricula = matricula).first()
        nome = usuario.nome
        tipo = usuario.tipo
        endereco = usuario.endereco
        match tipo:
            case 'grad':
                tipo = 'Graduação'
            case 'func':
                tipo = 'Funcionário'
            case 'dout':
                tipo = 'Doutorado'
        return render_template('perfil.html', nome = nome, tipo = tipo, endereco = endereco, matricula = matricula)
    else:
        return redirect(url_for('adm_pedidos'))

@app.route('/pedidos')
def pedidos():

    return render_template('pedidos.html', pedido = pedido)

