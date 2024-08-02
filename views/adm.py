from flask import render_template, request, redirect, session, url_for
from app import app, db
from models import Usuarios, Cardapios

@app.route('/adm-pedidos')
def adm_pedidos():
    return render_template('admpedidos.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')