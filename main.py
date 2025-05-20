# filepath: /university-assignment/university-assignment/src/main.py

import tkinter as tk
from db.mariadb_connector import connect_to_db
from gui.tkinter_ui import MainWindow

def main():
    # Iniciar conexion a la db
    db_cursor = connect_to_db()

    # Establecer la ventana principal
    root = tk.Tk()
    root.title("User Management System")

    # Crear y mostrar la ventana principal
    app = MainWindow(root, db_cursor)
    app.pack()

    # iniciar la aplicacion principal loop
    root.mainloop()

if __name__ == "__main__":
    main()