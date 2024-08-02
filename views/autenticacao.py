from flask import render_template, request, redirect, session, url_for
from app import app, db
from models import Usuarios
from views.pedidos import msgPedidoLogin

mensagem = ''
mensagemreg = ''
mensagemCE = ''

@app.route('/login')
def login():
    return render_template('login.html', mensagem = mensagem, mensagemreg = mensagemreg, mensagemCE = mensagemCE, msgPedidoLogin = msgPedidoLogin)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(matricula=request.form.get('matricula')).first()
    if usuario:
        if request.form.get('senha') == usuario.senha:
            global mensagem
            global mensagemCE
            global mensagemreg
            global msgPedidoLogin

            session['usuario_logado'] = usuario.matricula

            msgPedidoLogin = ''
            mensagem = ''
            mensagemreg = ''
            mensagemCE = ''
            return redirect(url_for('index'))
        else:
            mensagemreg = ''
            mensagemCE = ''
            mensagem = 'Usuario ou senha incorretos!'
            return redirect(url_for('login'))
    else:
        mensagemreg = ''
        mensagemCE = ''
        mensagem = 'Usuario ou senha incorretos!'
        return redirect(url_for('login'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/criar-conta', methods=['POST'])
def criar_conta():
    nome = request.form.get('nome')
    matricula = request.form.get('matricula')
    endereco = request.form.get('endereco')
    senha = request.form.get('senha')
    tipo = request.form.get('tipo')
    adm = False

    conta = Usuarios.query.filter_by(matricula = matricula).first()
    if conta:
        global mensagemCE
        global mensagemreg
        global mensagem
        mensagem = ''
        mensagemreg = ''
        mensagemCE = 'Conta já existente, faça seu login'
        return redirect(url_for('login'))
    
    nova_conta = Usuarios(matricula = matricula, nome = nome, senha = senha, tipo = tipo, endereco = endereco, adm = adm)
    db.session.add(nova_conta)
    db.session.commit()

    mensagem = ''
    mensagemCE = ''
    mensagemreg = 'Conta criada com sucesso, faça seu login'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect(url_for('index'))