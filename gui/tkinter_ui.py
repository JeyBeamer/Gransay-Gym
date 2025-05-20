import tkinter as tk
from tkinter import messagebox
from models.membership import Membership

class MainWindow(tk.Frame):
    def __init__(self, master, db_cursor):
        super().__init__(master)
        self.master = master
        self.db_cursor = db_cursor

        self.label = tk.Label(master, text="Bienvenido a Gransay")
        self.label.config(font=("Arial", 24))
        self.label.config(fg="black")
        self.label.config(bg="white")
        self.label.config(pady=20)
        self.label.config(padx=20)
        self.label.config(borderwidth=2, relief="groove")
        self.label.config(anchor="center")
        self.label.config(width=30)
        self.label.config(height=2)
        self.label.config(justify="center")
        self.label.pack()

        self.user_info_button = tk.Button(master, text="Usuarios", command=self.show_user_info)
        self.user_info_button.pack()

        self.memberships_button = tk.Button(master, text="Membresias", command=self.show_memberships)
        self.memberships_button.pack()

        self.plans_button = tk.Button(master, text="Planes", command=self.show_plans)
        self.plans_button.pack()
        

    def show_user_info(self):
        # Logic to display user information
        pass

    def show_memberships(self):
        memberships = Membership.get_all_memberships(self.db_cursor)
        if memberships:
            info = "\n".join([f"{m.membership_id}: {m.name} - ${m.price}" for m in memberships])
        else:
            info = "No memberships found."
        messagebox.showinfo("Memberships", info)

    def show_plans(self):
        # Logic to display plans
        pass