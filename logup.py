import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql

#el inicio de sesion y el de registrar usuario estan en el mismo codigo
def menu_pantalla():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("300x380")
    pantalla.title("Mock's")
    pantalla.iconbitmap("srv.ico")

    image=PhotoImage(file="srv.gif")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label(text="acceso al sistema", bg="navy", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesion", height="3", width="30", command=inicio_sesion).pack()
    Label(text="").pack()

    Button(text="Registrar", height="3", width="30", command=registrar).pack()

    pantalla. mainloop()

def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x300")
    pantalla1.title("inicio de sesion")
    pantalla1.iconbitmap("srv.ico")

    Label(pantalla1, text="por favor ingrese su usuario y contraseña\n a continuacion", bg="navy", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    Label(pantalla1, text="").pack()

    global nombreu_verify
    global constrasenau_verify

    nombreu_verify=StringVar()
    constrasenau_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="usuario").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreu_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="contraseña").pack()
    contrasena_usuario_entry = Entry(pantalla1, show="*", textvariable=constrasenau_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="iniciar sesion", command=validacion_datos).pack()

def registrar():
    global pantalla2
    pantalla2=Toplevel(pantalla)
    pantalla2.geometry("400x300")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("srv.ico")

    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry=StringVar()
    contrasena_entry=StringVar()

    Label(pantalla2, text="señor usuario, \n Por favor ingrese sus datos a continuacion", bg="navy", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    Label(pantalla2, text="").pack()

    Label(pantalla2, text="usuario").pack()
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="contraseña").pack()
    contrasena_entry = Entry(pantalla2, show="*")
    contrasena_entry.pack()
    Label(pantalla2).pack()


    Button(pantalla2, text="Registrar", command=inserta_datos).pack()



def inserta_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="mocks"
        )

    fcursor=bd.cursor()

    sql="INSERT INTO login (usuario, contrasena) VALUES ('{0}', '{1}')".format(nombreusuario_entry.get(), contrasena_entry.get())
    
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="registro exitoso", title="Aviso")

    except:
        bd.rollback()
        messagebox.showinfo(message="registro no exitoso", title="Aviso")

    bd.close()
    

def validacion_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="mocks"
        )

    fcursor=bd.cursor()

    fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreu_verify.get()+"' and contrasena='"+constrasenau_verify.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo(title="Inicio de sesion correcto", message="usuario y contraseña correcta")
        
    else:
        messagebox.showinfo(title="Inicio de sesion incorrecto", message="usuario y/o contraseña incorrecta")
    

    bd.close()


    
    
menu_pantalla()

    
