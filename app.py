from  tkinter import *
from tkinter import messagebox
import hashlib
import os
import sqlite3

# -------- FUNCIONES ----------#

# -------- FUNCIONES - MENU - BBDD ----------#
def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute(''' 
            CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD BLOB,
                APELLIDO VARCHAR(10),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(200)
            )
            ''')
        messagebox.showinfo("BBDD","BBDD creada con exito")
    except:
       messagebox.showwarning("!Atencion!","La BBDD ya existe")
    finally:
        miConexion.close()

def salirAplicacion():
    valor =  messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")

    if valor =="yes":
        root.destroy()

# -------- FUNCIONES - MENU - BORRAR ----------#

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    textoComentario.delete(1.0,END)

# -------- FUNCIONES - MENU - CRUD ----------#

def crear():
    miconexion = sqlite3.connect("Usuarios")
    miCursor = miconexion.cursor()
    try:
        miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", ( 
            miNombre.get(), 
            passwordHash(miPass.get()),
            miApellido.get(),
            miDireccion.get(),
            textoComentario.get("1.0", END) 
            )
        )
        miconexion.commit()
        messagebox.showinfo("BBDD","Registro insertado con exito")
    except :
        messagebox.showwarning("!Error!","Ha ocurrido un error al cargar tus datos")
    finally:
        limpiarCampos()
        miconexion.close()
        

def leer():
    miconexion = sqlite3.connect("Usuarios")
    miCursor = miconexion.cursor()
    try:
        miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID= ?", miId.get())

        elUsuario = miCursor.fetchall()

        for usuario in elUsuario:
            miId.set(usuario[0])
            miNombre.set(usuario[1]), 
            miPass.set(usuario[2]),
            miApellido.set(usuario[3]),
            miDireccion.set(usuario[4]),
            textoComentario.insert(1.0,usuario[5])

        miconexion.commit()
    except:
        messagebox.showwarning("!Error!","No se ha encontrado el usuario solicitado")
        miId.set("")
    finally:
        miconexion.close()

def actualizar():
    miconexion = sqlite3.connect("Usuarios")
    miCursor = miconexion.cursor()
    try:
        miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?,APELLIDO=?,DIRECCION=?, COMENTARIOS=? WHERE ID= ? ",(
            miNombre.get(),
            passwordHash(miPass.get()),
            miApellido.get(),
            miDireccion.get(),
            textoComentario.get("1.0", END),
            miId.get()
        ))
        miconexion.commit()
        messagebox.showinfo("BBDD","Registro actualizado con exito")
    except:
        messagebox.showwarning("!Error!","No se ha podido actualizar la informacion de el usuario solicitado")
    finally:
        limpiarCampos()
        miconexion.close()

def borrar():
    miconexion = sqlite3.connect("Usuarios")
    miCursor = miconexion.cursor()
    try:
        miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=?",miId.get())
        miconexion.commit()
        messagebox.showinfo("BBDD","Registro borrado con exito")
    except:
        messagebox.showwarning("!Error!","No se ha podido eliminar el usuario solicitado")
    finally:
        limpiarCampos()
        miconexion.close()  

def passwordHash(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    passwordHash = key  + salt
    return passwordHash

# -------- CONFIG 1 TKINTER ----------#
root = Tk()

# -------- MENU ----------#

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=lambda:conexionBBDD())
bbddMenu.add_command(label="Salir", command=lambda:salirAplicacion())

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar", command=lambda:limpiarCampos())

crudborrarMenu = Menu(barraMenu, tearoff=0)
crudborrarMenu.add_command(label="Crear", command=lambda:crear())
crudborrarMenu.add_command(label="Leer", command=lambda:leer())
crudborrarMenu.add_command(label="Actualizar", command=lambda:actualizar())
crudborrarMenu.add_command(label="Borrar", command=lambda:borrar())

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudborrarMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# -------- FRAME ----------#
miFrame = Frame(root)
miFrame.pack()

miFrame2 = Frame(root)
miFrame2.pack()

# -------- LABEL - FRAME 1 ----------#

idLabel = Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e")

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e")

passLabel = Label(miFrame, text="Contraseña:")
passLabel.grid(row=2, column=0, sticky="e")

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0 , sticky="e")

direccionLabel = Label(miFrame, text="Direccion:")
direccionLabel.grid(row=4, column=0, sticky="e")

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e")

# -------- ENTRY - FRAME 1 ----------#

miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar()

cuadroId = Entry(miFrame, textvariable=miId)
cuadroId.grid(row=0, column=1, pady=5 , padx=5)

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, pady=5 , padx=5)
cuadroNombre.config(fg="red",justify="left")

cuadroPass = Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, pady=5 , padx=5)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, pady=5 , padx=5)

cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1,  pady=5 , padx=5)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, pady=5)
scrollVert = Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=5,column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

# -------- BUTTON -  FRAME 2----------#

botonCrear = Button(miFrame2, text="Crear", command=lambda:crear())
botonCrear.grid(row=1,column=0, sticky="nsew",  pady=5 , padx=5)

botonLeer = Button(miFrame2, text="Leer", command=lambda:leer())
botonLeer.grid(row=1,column=1, sticky="nsew",  pady=5 , padx=5)

botonActualizar = Button(miFrame2, text="Actualizar",  command=lambda:actualizar())
botonActualizar.grid(row=1,column=2, sticky="nsew",  pady=5 , padx=5)

botonBorrar = Button(miFrame2, text="Borrar", command=lambda:borrar())
botonBorrar.grid(row=1,column=3, sticky="nsew",  pady=5 , padx=5)

# -------- CONFIG 2 TKINTER ----------#

root.mainloop() 