class Plan:
    def __init__(self, plan_id, membership_id, details):
        self.plan_id = plan_id
        self.membership_id = membership_id
        self.details = details

    def create_plan(self, cursor):
        query = "INSERT INTO plans (membership_id, details) VALUES (%s, %s)"
        cursor.execute(query, (self.membership_id, self.details))

    def update_plan(self, cursor):
        query = "UPDATE plans SET membership_id = %s, details = %s WHERE plan_id = %s"
        cursor.execute(query, (self.membership_id, self.details, self.plan_id))

    def delete_plan(self, cursor):
        query = "DELETE FROM plans WHERE plan_id = %s"
        cursor.execute(query, (self.plan_id,))

    @staticmethod
    def get_plan(cursor, plan_id):
        query = "SELECT * FROM plans WHERE plan_id = %s"
        cursor.execute(query, (plan_id,))
        return cursor.fetchone()

    @staticmethod
    def get_all_plans(cursor):
        query = "SELECT * FROM plans"
        cursor.execute(query)
        return cursor.fetchall()