from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/')
def index():
    session.clear()
    dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos=dojos)

@app.route('/dojo')
def view_dojo_with_employees():
    dojos = Dojo.get_all_dojos()
    if 'dojo' in session:
        results = session['dojo']
        dojo_data = {
            'id': results[0]['id'],
            'name': results[0]['name']
        }
        dojo = Dojo(dojo_data)
        ninjas = []
        for item in results:
            if item['ninja.id'] != None:
                ninja_data = {
                    'id': item['ninja.id'],
                    'first_name': item['first_name'],
                    'last_name': item['last_name'],
                    'created_at': item['ninja.created_at'],
                    'updated_at': item['ninja.updated_at'],
                    'dojo_id': item['dojo_id'],
                }
                new_ninja = Ninja(ninja_data)
                ninjas.append(new_ninja)
            

    return render_template('generic.html', dojo=dojo, ninjas=ninjas, dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/')

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/')

@app.route('/dojos/<int:dojo_id>')
def dojo_info(dojo_id):
    data = {
        'id': dojo_id
    }
    session['dojo'] = Dojo.get_ninjas_by_dojo_id(data)
    return redirect('/dojo')

@app.route('/users/<int:ninja_id>/delete')
def delete_ninja(ninja_id):
    data = {
        'id': ninja_id
    }
    Ninja.delete_ninja(data)
    return redirect('/')