from tkinter import *
import mysql.connector
from addCurso import AddCurso

class Login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x300")

        #Conectarse a la base de datos
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="proyectoformacion"
        )

        #Hacer una consulta
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT entidad FROM login WHERE id = 1")
        resultado = self.mycursor.fetchone()

        #Imprimir el resultado y almacenarlo en una variable
        if resultado:
            self.user = resultado[0]
            print(self.user)
        else:
            print("No se encontró ningún registro con id = 1")

        self.mycursor.execute("SELECT password FROM login WHERE id = 1")
        resultado = self.mycursor.fetchone()
        if resultado:
            self.passw = resultado[0]
            print(self.passw)
        else:
            print("No se encontró ningún registro con id = 1")

        #Crear widgets
        self.label_user = Label(self.ventana, text="Usuario:", pady=20)
        self.label_user.pack()

        self.entry_user = Entry(self.ventana)
        self.entry_user.pack()

        self.label_password = Label(self.ventana, text="Contraseña:", pady=20)
        self.label_password.pack()

        self.entry_password = Entry(self.ventana, show="*")
        self.entry_password.pack()

        self.button_accept = Button(self.ventana, text="Aceptar", command=self.accept)
        self.button_accept.pack(side="left")

        self.button_cancel = Button(self.ventana, text="Cancel", command=self.ventana.destroy)
        self.button_cancel.pack(side="right")

        self.label_correcto = Label(self.ventana, text="Correct", bg="green")
        self.label_incorrecto = Label(self.ventana, text="Incorrect", bg="red")

    def accept(self):
        usuario = self.entry_user.get()
        password = self.entry_password.get()
        if usuario == self.user and password == self.passw:
            self.label_correcto.pack()
            self.ventana.destroy()
            self.addCurso = AddCurso()

        else:
            self.label_incorrecto.pack()

    def run(self):
        self.ventana.mainloop()
