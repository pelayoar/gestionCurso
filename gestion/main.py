from tkinter import *
import mysql.connector

ventana = Tk()
ventana.geometry("400x300")

#CONSULTAS LOGIN
# Conectarse a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="proyectoformacion"
)

# Hacer una consulta
mycursor = mydb.cursor()
mycursor.execute("SELECT entidad FROM login WHERE id = 1")
resultado = mycursor.fetchone()

# Imprimir el resultado y almacenarlo en una variable
if resultado:
    user = resultado[0]
    print(user)
else:
    print("No se encontró ningún registro con id = 1")

mycursor.execute("SELECT password FROM login WHERE id = 1")
resultado = mycursor.fetchone()
if resultado:
    passw = resultado[0]
    print(passw)
else:
    print("No se encontró ningún registro con id = 1")


def accept():
    usuario = entry_user.get()
    password = entry_password.get()
    if usuario == user and password == passw:
        label_correcto.pack()
    else:
        label_incorrecto.pack()


label_user = Label(ventana, text="Usuario:")
label_user.pack()

entry_user = Entry(ventana)
entry_user.pack()

label_password = Label(ventana, text="Contraseña:")
label_password.pack()

entry_password = Entry(ventana, show ="*")
entry_password.pack()

button_accept = Button(ventana, text="Aceptar", command = lambda: accept())
button_accept.pack()

button_cancel = Button(ventana, text="Cancel", command=ventana.destroy)
button_cancel.pack()

label_correcto = Label(ventana, text="Correct", bg="green")
label_incorrecto = Label(ventana, text="Incorrect", bg="red")


ventana.mainloop()

