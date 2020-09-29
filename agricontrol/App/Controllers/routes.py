
from flask import render_template,request,redirect,url_for,session
from markupsafe import escape
from App import app,db
from App.Templates.Components.formLogin import LoginForm
from App.Templates.Components.formRegister import RegisterForm
from App.Templates.Components.formProducer import ProducerForm
import pandas as pd
import json
import os,os.path
from App.Models.Models import  User,Producer
from sqlalchemy import distinct
from sqlalchemy import func
from App.Controllers.loginController import AuthFinger,Register
from App.Controllers.dashboardController import makeGraph;

# index routes
# @app.route("/", defaults = {"user": None})
# def index(user):
#     return render_template('index.html',user = user)

@app.route("/")
def index():
    if 'user' in session:
        Producers = Producer.query.all()
        return render_template('index.html',
                nivel = int(escape(session['nivel'])),
                Producers = Producers)
    return redirect(url_for('login'))

# login route
@app.route("/login", methods =['POST','GET'])
def login():
    form = LoginForm()
    # validando formulário
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        
        userSelect = User.query.filter_by(username=form.username.data).first()
        # vaidando usuário
        if(userSelect!=None):
            print(userSelect)
            # validando digital
            if AuthFinger(userSelect.fingerimage):

                # validou com sucesso
                session['user'] = userSelect.username
                session['nivel'] = userSelect.nivelAcesso
                return redirect(url_for('index'), code=302)
                
            errorFinger = "Digital não cadastrada ou incorreta"
            return render_template('login.html', form = form,errorBd = errorFinger)

        # print(form.errors)
        errorUser = 'Usuário nao encontrado'
        return render_template('login.html', form = form,errorBd = errorUser)

    print(form.errors)
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    a =  teste
    session.pop('user', None)
    session.pop('nivel',None)
    return redirect(url_for('login'))


@app.route("/users")
def indexUser():
    users = User.query.all()
    print(users)
    return render_template('user/index.html',users= users)

@app.route("/users/<id>")
def user(id):
    form = RegisterForm()
    user = User.query.get(id)
    print(user)
    return render_template('user/show.html',user = user,form=form)

# user create route
@app.route("/users/create", methods =['POST','GET'])
def register():
    form = RegisterForm()
    userExist = User.query.filter_by(username=form.username.data).first()

    if userExist:
        return render_template('register.html', form = form,messageBd = "Nome de usuário já em uso, escolha outro!" , user = escape(session['user']))

    if form.validate_on_submit():
        fingerImageName = Register()
        createUser = User(form.username.data, form.password.data, form.name.data, fingerImageName, form.email.data, form.nivel.data)
        db.session.add(createUser)
        db.session.commit()
        form= RegisterForm()
        return render_template('user/create.html', form = form, messageBd="Cadastrado com sucesso")

    return render_template('user/create.html', form = form, user = escape(session['user']))

@app.route("/produtores/create", methods =['POST','GET'])
def createProducer():
    form = ProducerForm()
    if form.validate_on_submit():
        createProducer = Producer(form.name.data, form.farming.data, form.annualamount.data, form.pesticide.data)
        db.session.add(createProducer)
        db.session.commit()
        return render_template("createProducer.html",form=form,messageBd="Cadastrado com sucesso")
    return render_template("createProducer.html",form = form)

@app.route("/dashboard", methods =['GET'])
def dashboard():
    makeGraph();
    return render_template("dashboard.html",producers = 'producers') 

@app.route("/create")
def create():
    i = User("jonathasa","123","jonathas augusto", "/Images/a.png", "a@gmail.com",1)
    db.session.add(i)
    db.session.commit()
    return "CREATE"

@app.route("/select")
def select():
    r = User.query.filter_by(username="jonathasa").first()
    print(r.username)
    return "READ"

@app.route("/update")
def update():
    u = User.query.filter_by(username="jonathas").first()
    u.username="jonathasUPDATE"
    db.session.add(u)
    db.session.commit()
    return "UPDATEE"

@app.route("/delete")
def delete():
    d = User.query.filter_by(username="jonathasUPDATE").first()
    db.session.delete(d)
    db.session.commit()
    return "DELETADO"

@app.route("/deleteuser",methods =['POST','GET'])
def deleteuser():
    promisse = json.loads(request.data)
    d = User.query.get(promisse['id'])
    db.session.delete(d)
    db.session.commit()
    return "DELETADO"

@app.route("/updateuser",methods =['POST','GET'])
def teste():
    promisse = json.loads(request.data)
    
    u = User.query.get(promisse['id'])

    u.username=promisse['username']
    u.name=promisse['nome']
    u.email=promisse['email']
    u.nivelAcesso=promisse['nivel']
    db.session.add(u)
    db.session.commit()


    return request.values