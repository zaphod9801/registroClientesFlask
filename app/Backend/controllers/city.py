from flask import Flask, render_template, request, jsonify, url_for
from flask_jwt_extended import get_jwt_identity, jwt_required
from Backend.models.models import City, Client
from app import db, app


@app.route('/cities', methods=['GET'], endpoint='cities_list')
@jwt_required()
def cities_list():
    current_user = get_jwt_identity()
    page = request.args.get('page', 1, type=int)
    per_page = 10
    cities = db.session.query(City).paginate(page=page, per_page=per_page)
    delete_url = url_for('cities_delete', cod=0)
    edit_url = url_for('cities_edit', cod=0)
    return render_template('cities.html', cities=cities, delete_url=delete_url, edit_url=edit_url)


@app.route('/cities/new', methods=['POST'])
def cities_create():
    cod = request.form.get('cod')
    name = request.form.get('name')
    new_city = City(cod=cod, name=name)
    db.session.add(new_city)
    db.session.commit()
    return jsonify({'message': 'Ciudad añadida correctamente', 'city': new_city.to_dict()}), 201


@app.route('/cities/<int:cod>/edit', methods=['POST'])
def cities_edit(cod):
    city = City.query.get_or_404(cod)
    city.name = request.form.get('name')
    db.session.commit()
    return jsonify({'message': 'Ciudad editada correctamente', 'city': city.to_dict()}), 200


@app.route('/cities/<int:cod>/delete', methods=['POST'])
def cities_delete(cod):
    # El código de la ciudad predeterminada
    default_city_cod = 0

    # Verificar si la ciudad predeterminada existe
    default_city = City.query.get(default_city_cod)
    if default_city is None:
        default_city = City(cod=default_city_cod, name="Sin ciudad")
        db.session.add(default_city)
        db.session.commit()

    city = City.query.get_or_404(cod)

    # Reasignar todos los clientes de la ciudad a la ciudad predeterminada
    Client.query.filter_by(city_cod=city.cod).update(
        {Client.city_cod: default_city.cod}, synchronize_session='fetch')

    # Después de reasignar todos los clientes, se puede eliminar la ciudad
    db.session.delete(city)
    db.session.commit()

    return jsonify({'message': 'Ciudad eliminada correctamente', 'city': city.to_dict()}), 200
