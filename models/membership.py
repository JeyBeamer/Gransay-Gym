class Membership:
    def __init__(self, membership_id, name, price):
        self.membership_id = membership_id
        self.name = name
        self.price = price

    def create_membership(self, cursor):
        query = "INSERT INTO memberships (name, price) VALUES (%s, %s)"
        cursor.execute(query, (self.name, self.price))

    def update_membership(self, cursor):
        query = "UPDATE memberships SET name = %s, price = %s WHERE membership_id = %s"
        cursor.execute(query, (self.name, self.price, self.membership_id))

    def delete_membership(self, cursor):
        query = "DELETE FROM memberships WHERE membership_id = %s"
        cursor.execute(query, (self.membership_id,))

    @classmethod
    def get_membership(cls, cursor, membership_id):
        query = "SELECT * FROM memberships WHERE membership_id = %s"
        cursor.execute(query, (membership_id,))
        result = cursor.fetchone()
        if result:
            return cls(result[0], result[1], result[2])
        return None

    @classmethod
    def get_all_memberships(cls, cursor):
        query = "SELECT * FROM memberships"
        cursor.execute(query)
        results = cursor.fetchall()
        return [cls(row[0], row[1], row[2]) for row in results]