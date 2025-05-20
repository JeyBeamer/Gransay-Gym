def connect_to_db():
    import mariadb
    import sys

    try:
        conn = mariadb.connect(
            user="root",
            password="151106",
            host="localhost",
            port=3306,
            database="gransay"
        )
        cursor = conn.cursor()
        return cursor
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)