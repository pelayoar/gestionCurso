from tkinter import *
import mysql.connector

class AddCurso:
    def __init__(self):
        self.ventana = Tk()


        #Conectarse a la base de datos
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="proyectoformacion"
        )

        #Crear widgets
        self.label_nombreCurso = Label(self.ventana, text="Nombre del curso:", pady=20)
        self.label_nombreCurso.pack()

        self.entry_nombreCurso = Entry(self.ventana)
        self.entry_nombreCurso.pack()

        self.label_codigo = Label(self.ventana, text="Codigo del curso:", pady=20)
        self.label_codigo.pack()

        self.entry_codigo = Entry(self.ventana)
        self.entry_codigo.pack()

        self.button_accept = Button(self.ventana, text="Aceptar")
        self.button_accept.pack(side="left")

        self.button_cancel = Button(self.ventana, text="Cancel", command=self.ventana.destroy)
        self.button_cancel.pack(side="right")

        self.label_correcto = Label(self.ventana, text="Correct", bg="green")
        self.label_incorrecto = Label(self.ventana, text="Incorrect", bg="red")

    '''def accept(self):
        usuario = self.entry_user.get()
        password = self.entry_password.get()
        if usuario == self.user and password == self.passw:
            self.label_correcto.pack()
        else:
            self.label_incorrecto.pack()
'''
    def run(self):
        self.ventana.mainloop()
