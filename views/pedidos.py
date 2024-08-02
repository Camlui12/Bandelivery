from flask import render_template, request, redirect, session, url_for
from app import app, db
from models import Usuarios, Cardapios
import datetime

data = datetime.datetime.now()
dia_semana = data.weekday()

msgPedidoLogin = ''

arrozb = 'Arroz branco'
feijao = 'Feijão'
arrozi = 'Arroz integral'

pedido = []
opcoes = []

@app.route('/cardapio')
def cardapio():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        global msgPedidoLogin
        msgPedidoLogin = 'Você precisa fazer login antes de montar seu pedido!'
        return redirect(url_for('login'))
    else:
        global pedido
        pedido = []
        global dia_semana
        match dia_semana:
            case 0:
                dia = 'segunda'
            case 1:
                dia = 'terca'
            case 2:
                dia = 'quarta'
            case 3:
                dia = 'quinta'
            case 4:
                dia = 'sexta'
            case _:
                dia = 'outro'

        cardapio_do_dia = Cardapios.query.filter_by(dia = dia).first()
        if dia:
            global arrozb
            global feijao
            global arrozi
            global opcoes

            op_onivora = cardapio_do_dia.op_onivora
            op_veg = cardapio_do_dia.op_veg
            guarnicao = cardapio_do_dia.guarnicao
            salada1 = cardapio_do_dia.salada1
            salada2 = cardapio_do_dia.salada2
            refresco = cardapio_do_dia.refresco

            opcoes = [op_onivora, op_veg, guarnicao, salada1, salada2, refresco, arrozb, feijao, arrozi]

            msgPedidoLogin = ''
            return render_template('cardapio.html', op_onivora = op_onivora, op_veg = op_veg, guarnicao = guarnicao, arrozb = arrozb, feijao = feijao, arrozi = arrozi, salada1 = salada1, salada2 = salada2, refresco = refresco)
        else:
            ...

@app.route('/receber-pedido', methods=['POST', 'GET'])
def receber_pedido():

    global pedido
    global opcoes

    oponiv = request.form.get('oponiv')
    opveg = request.form.get('opveg')
    guarnic = request.form.get('guarnic')
    arb = request.form.get('arrozb')
    fjao = request.form.get('feijao')
    ari = request.form.get('arrozi')
    sal1 = request.form.get('salada1')
    sal2 = request.form.get('salada2')
    ref = request.form.get('refresco')

    teste = [oponiv, opveg, guarnic, arb, fjao, ari, sal1, sal2, ref]

    for opcao in teste:
        if opcao in opcoes:
            pedido.append(opcao)
    
    return redirect(url_for('confirmar_pedido'))

@app.route('/confirmar-pedido')
def confirmar_pedido():
    return render_template('confirmarpedido.html', pedido = pedido)

@app.route('/pagamento')
def pagamento():
    return render_template('pagamento.html')
