from flask import Flask, render_template, request, jsonify, url_for
from Backend.models.models import City
from app import db, app


@app.route('/cities', methods=['GET'])
def cities_list():
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
    city = City.query.get_or_404(cod)
    db.session.delete(city)
    db.session.commit()
    return jsonify({'message': 'Ciudad eliminada correctamente', 'city': city.to_dict()}), 200
