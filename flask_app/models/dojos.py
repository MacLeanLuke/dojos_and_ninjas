from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninjas import Ninja

class Dojo():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []


    @classmethod
    def get_all_dojos(cls):

        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojo_and_ninjas_db').query_db(query)

        dojos = []

        for item in results:
            new_dojo = Dojo(item)
            dojos.append(new_dojo)

        return dojos

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        new_dojo_id = connectToMySQL('dojo_and_ninjas_db').query_db(query, data)

        return new_dojo_id

    @classmethod
    def get_ninjas_by_dojo_id(cls, data):

        query = "SELECT * FROM dojos LEFT JOIN ninja ON dojos.id = ninja.dojo_id WHERE dojos.id = %(id)s;"

        results = connectToMySQL('dojo_and_ninjas_db').query_db(query, data)

        print(results)

        return results

        dojos = []

        

        for item in results:
            if len(dojos) == 0:
                new_dojo = Dojo(item)
                dojos.append(new_dojo)
            elif dojos[-1].id != item['id']:
                new_dojo = Dojo(item)
                dojos.append(new_dojo)
            if item['ninja.id'] != None:
                ninja_data = {
                    'id': item['ninja.id'],
                    'first_name': item['first_name'],
                    'last_name': item['last_name'],
                    'created_at': item['ninja.created_at'],
                    'updated_at': item['ninja.updated_at'],
                    'dojo_id': item['dojo_id'],
                }
                ninja = Ninja(ninja_data)
                ninja.dojo = new_dojo
                new_dojo.ninjas.append(ninja)

        return dojos

    @classmethod
    def delete_dojo(cls, data):

        query = "DELETE FROM dojos WHERE id = %(id)s;"

        connectToMySQL('dojo_and_ninjas_db').query_db(query, data)

    @classmethod
    def update_dojo(cls, data):

        # UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)
        query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s;"

        connectToMySQL('dojo_and_ninjas_db').query_db(query, data)