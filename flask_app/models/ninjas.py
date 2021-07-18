from flask_app.config.mysqlconnection import connectToMySQL

class Ninja():
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dojo_id = data['dojo_id']
        self.dojo = None

    def start_date(self):
        return self.created_at.strftime("%m/%d/%Y")

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninja (first_name, last_name, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(dojo_id)s);"

        new_ninja_id = connectToMySQL('dojo_and_ninjas_db').query_db(query, data)

        return new_ninja_id

    @classmethod
    def delete_ninja(cls, data):

        query = "DELETE FROM ninja WHERE id = %(id)s;"

        connectToMySQL('dojo_and_ninjas_db').query_db(query, data)

    @classmethod
    def update_ninja(cls, data):

        # UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)
        query = "UPDATE ninja SET first_name = %(first_name)s, last_name = %(last_name)s, dojo_id = %(dojo_id)s WHERE id = %(id)s;"

        connectToMySQL('dojo_and_ninjas_db').query_db(query, data)