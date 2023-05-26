from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies, jwt_required, get_jwt_identity
from flask_restful import Api, Resource
from Backend.models.models import User
from app import db, app
from werkzeug.security import generate_password_hash


@app.route('/', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.get(username)
        if user and user.check_password(password):
            access_token = create_access_token(identity=username)
            resp = make_response(redirect(url_for('clients_list')))
            set_access_cookies(resp, access_token)
            return resp
        else:
            error_message = "Credenciales inválidas"
            return render_template('login.html', error_message=error_message)

    else:  # si es una solicitud GET, renderiza la página de inicio de sesión
        return render_template('login.html', error_message=error_message)


@app.route('/logout', methods=['POST'])
def logout():
    resp = make_response(redirect(url_for('login')))
    unset_jwt_cookies(resp)
    return resp


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = generate_password_hash(request.form.get('password'))
        email = request.form.get('email')
        new_user = User(name=name, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
        access_token = create_access_token(identity=name)
        resp = make_response(redirect(url_for('clients_list')))
        set_access_cookies(resp, access_token)
        return resp
    return render_template('register.html')


@app.route('/users', methods=['GET'])
def users_list():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/users/new', methods=['GET', 'POST'])
def users_create():
    if request.method == 'POST':
        name = request.form.get('name')
        password = generate_password_hash(request.form.get('password'))
        email = request.form.get('email')
        # Aquí se asume que estás subiendo una foto como un archivo.
        photo = request.files['photo']
        new_user = User(name=name, password=password,
                        email=email, photo=photo.read())
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users_list'))
    return render_template('user_new.html')


@app.route('/users/<string:name>/edit', methods=['GET', 'POST'])
def users_edit(name):
    user = User.query.get_or_404(name)
    if request.method == 'POST':
        user.name = request.form.get('name')
        user.password = generate_password_hash(request.form.get('password'))
        user.email = request.form.get('email')
        user.photo = request.files['photo'].read()
        db.session.commit()
        return redirect(url_for('users_list'))
    return render_template('user_edit.html', user=user)


@app.route('/users/<string:name>/delete', methods=['POST'])
def users_delete(name):
    user = User.query.get_or_404(name)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users_list'))


api = Api(app)


class UserInfo(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.get(current_user)
        return {'name': user.name}, 200

    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        user = User.query.get(current_user)
        user.name = request.json.get('name', user.name)
        db.session.commit()
        return {'message': 'ok'}, 200


api.add_resource(UserInfo, '/api/user/info')
