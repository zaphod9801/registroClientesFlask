from flask import Flask, render_template, request, redirect, url_for, jsonify
from Backend.models.models import Client, City
from app import db, app


@app.route('/clients', methods=['GET'])
def clients_list():
    clients = Client.query.all()
    cities = City.query.all()
    return render_template('clients.html', clients=clients, cities=cities)


@app.route('/clients/create', methods=['POST'])
def clients_create():
    name = request.form.get('name')
    city_cod = request.form.get('city_cod')
    new_client = Client(name=name, city_cod=city_cod)
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'message': 'Cliente añadido correctamente'}), 201


@app.route('/clients/<int:cod>/edit', methods=['POST'])
def clients_edit(cod):
    client = Client.query.get_or_404(cod)
    client.name = request.form.get('name')
    client.city_cod = request.form.get('city_cod')
    db.session.commit()
    return redirect(url_for('clients_list'))


@app.route('/clients/<int:cod>/delete', methods=['POST'])
def clients_delete(cod):
    client = Client.query.get_or_404(cod)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('clients_list'))
