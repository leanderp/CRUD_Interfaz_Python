from  tkinter import *
from tkinter import messagebox
import sqlite3

# -------- FUNCIONES ----------#

def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute(''' 
            CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(10),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(200)
            )
            ''')
        messagebox.showinfo("BBDD","BBDD creada con exito")
    except:
       messagebox.showwarning("!Atencion!","La BBDD ya existe")

def salirAplicacion():
    valor =  messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")

    if valor =="yes":
        root.destroy()
        
# -------- CONFIG 1 TKINTER ----------#
root = Tk()

# -------- MENU ----------#

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=lambda:conexionBBDD())
bbddMenu.add_command(label="Salir", command=lambda:salirAplicacion())

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar")

crudborrarMenu = Menu(barraMenu, tearoff=0)
crudborrarMenu.add_command(label="Crear")
crudborrarMenu.add_command(label="Leer")
crudborrarMenu.add_command(label="Actualizar")
crudborrarMenu.add_command(label="Borrar")

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

cuadroId = Entry(miFrame)
cuadroId.grid(row=0, column=1, pady=5 , padx=5)

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=1, column=1, pady=5 , padx=5)
cuadroNombre.config(fg="red",justify="left")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=2, column=1, pady=5 , padx=5)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=3, column=1, pady=5 , padx=5)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=4, column=1,  pady=5 , padx=5)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, pady=5)
scrollVert = Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=5,column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

# -------- BUTTON -  FRAME 2----------#

botonCrear = Button(miFrame2, text="Crear", command=())
botonCrear.grid(row=1,column=0, sticky="nsew",  pady=5 , padx=5)

botonLeer = Button(miFrame2, text="Leer", command=())
botonLeer.grid(row=1,column=1, sticky="nsew",  pady=5 , padx=5)

botonActualizar = Button(miFrame2, text="Actualizar", command=())
botonActualizar.grid(row=1,column=2, sticky="nsew",  pady=5 , padx=5)

botonBorrar = Button(miFrame2, text="Borrar", command=())
botonBorrar.grid(row=1,column=3, sticky="nsew",  pady=5 , padx=5)

# -------- CONFIG 2 TKINTER ----------#

root.mainloop() 