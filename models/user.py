class User:
    def __init__(self, user_id, username, membership_id):
        self.user_id = user_id
        self.username = username
        self.membership_id = membership_id

    def create_user(self, cursor):
        query = "INSERT INTO users (username, membership_id) VALUES (%s, %s)"
        cursor.execute(query, (self.username, self.membership_id))

    def update_user(self, cursor):
        query = "UPDATE users SET username = %s, membership_id = %s WHERE user_id = %s"
        cursor.execute(query, (self.username, self.membership_id, self.user_id))

    def delete_user(self, cursor):
        query = "DELETE FROM users WHERE user_id = %s"
        cursor.execute(query, (self.user_id,))

    @staticmethod
    def get_user_by_id(cursor, user_id):
        query = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        return cursor.fetchone()

    @staticmethod
    def get_all_users(cursor):
        query = "SELECT * FROM users"
        cursor.execute(query)
        return cursor.fetchall()