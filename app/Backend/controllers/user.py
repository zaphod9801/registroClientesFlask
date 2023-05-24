from flask import Flask, render_template, request, redirect, url_for
from models.models import User
from app import db, app
from werkzeug.security import generate_password_hash


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
