from flask import Flask, render_template, request, redirect, url_for
from models.models import City
from app import db, app

@app.route('/cities', methods=['GET'])
def cities_list():
    cities = City.query.all()
    return render_template('cities.html', cities=cities)


@app.route('/cities/new', methods=['GET', 'POST'])
def cities_create():
    if request.method == 'POST':
        cod = request.form.get('cod')
        name = request.form.get('name')
        new_city = City(cod=cod, name=name)
        db.session.add(new_city)
        db.session.commit()
        return redirect(url_for('cities_list'))
    return render_template('city_new.html')


@app.route('/cities/<int:cod>/edit', methods=['GET', 'POST'])
def cities_edit(cod):
    city = City.query.get_or_404(cod)
    if request.method == 'POST':
        city.cod = request.form.get('cod')
        city.name = request.form.get('name')
        db.session.commit()
        return redirect(url_for('cities_list'))
    return render_template('city_edit.html', city=city)


@app.route('/cities/<int:cod>/delete', methods=['POST'])
def cities_delete(cod):
    city = City.query.get_or_404(cod)
    db.session.delete(city)
    db.session.commit()
    return redirect(url_for('cities_list'))
