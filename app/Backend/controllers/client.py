from flask import Flask, render_template, request, redirect, url_for, jsonify
from Backend.models.models import Client, City
from app import db, app


@app.route('/clients', methods=['GET'])
def clients_list():
    city_cod = request.args.get('city_cod', default=None, type=int)

    page = request.args.get('page', 1, type=int)
    per_page = 10
    if city_cod is not None:
        clients = db.session.query(Client).filter(Client.city_cod == city_cod).paginate(
            page=page, per_page=per_page)
    else:
        clients = db.session.query(Client).paginate(
            page=page, per_page=per_page)

    cities = list(map(lambda a: a.to_dict(), City.query.all()))
    city_dict = {city['cod']: city['name'] for city in cities}

    delete_url = url_for('clients_delete', cod=0)
    edit_url = url_for('clients_edit', cod=0)

    return render_template('clients.html', clients=clients, cities=cities, city_dict=city_dict, delete_url=delete_url, edit_url=edit_url, current_city_cod=city_cod)


@app.route('/clients/create', methods=['POST'])
def clients_create():
    name = request.form.get('name')
    city_cod = request.form.get('city_cod')
    new_client = Client(name=name, city_cod=city_cod)
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'message': 'Cliente añadido correctamente', 'client': new_client.to_dict()}), 201


@app.route('/clients/<int:cod>/edit', methods=['POST'])
def clients_edit(cod):
    client = Client.query.get_or_404(cod)
    client.name = request.form.get('name')
    client.city_cod = request.form.get('city_cod')
    db.session.commit()
    return jsonify({'message': 'Cliente editado correctamente', 'client': client.to_dict()}), 200


@app.route('/clients/<int:cod>/delete', methods=['POST'])
def clients_delete(cod):
    client = Client.query.get_or_404(cod)
    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'Cliente eliminado correctamente', 'client': client.to_dict()}), 200
