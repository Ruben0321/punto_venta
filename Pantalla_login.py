from tkinter import * 
from PIL import ImageTk
from Mensajes import Mensajes
class  Login:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Inicio de sesion")
        self.ventana.geometry("1200x630+100+50") 
        
        #fondo imagen
        #self.bg=ImageTk.PhotoImage(file="Imagenes/2.jpg")
        #self.bg_image= Label(self.ventana, image=self.bg,).place(x=0, y=0, relwidth=1, relheight=1 )
        
        #Marco del login
        self.Marco_login= Frame(ventana, bg="white")
        self.Marco_login.place(x=330, y=150, width=550, height=440)
        
        #Titulo
        self.Titulo= Label(self.Marco_login, text="Acceder", font=("Verdana", 35, "bold"), fg="#800080", bg="white").place(x=90, y=30)
        #Usuario
        leb_usuario= Label(self.Marco_login, text="Nombre de usuario", font=("Roboto", 15, "bold"), fg="grey", bg="white").place(x=90, y=100)
        self.nombre_usuario= Entry(self.Marco_login,font=("Roboto", 15), bg="#E7E6E6")
        self.nombre_usuario.place(x=90, y=130, width=320,height=35)
        
        #Contraseña
        self.leb_contraseña= Label(self.Marco_login, text="Contraseña", font=("Roboto", 15, "bold"), fg="grey",bg="white").place(x=90, y=170)
        self.contraseña= Entry(self.Marco_login,font=("Roboto", 15), bg="#E7E6E6",show="*")
        self.contraseña.place(x=90, y=200, width=320,height=35)
        
        #botonsillo       
        self.button=Button(self.Marco_login,command=lambda:self.Validar_login(),cursor="hand2",text="Iniciar sesion", bd=0,font=("Roboto", 15), bg="#00FF00", fg="white").place(x=165, y=240,width=180,height=40)
        #Registrarse= Button(Marco_login,command=self.verificar_funcion,cursor="hand2",text="Registrarse", bd=0,font=("Roboto", 15), bg="#00FF00", fg="white").place(x=90, y=240,width=100,height=40)
        #cancelar= Button(Marco_login,command=self.verificar_funcion,cursor="hand2",text="Cancelar", bd=0,font=("Roboto", 15), bg="#00FF00", fg="white").place(x=200, y=240,width=80,height=40)
    
    def Validar_login (self):
            mensaje=""
            a="ruben"
            b="123"
            if self.nombre_usuario.get()=="" or self.contraseña.get() == "":
                #messagebox.showerror("Error" , "todos los compos son requeridos", parent=self.root)
                mensaje="Todos los campos son requeridos"
            elif self.nombre_usuario.get()!=a:
                #messagebox.showerror("Error" , "Nombre invalido", parent=self.root)
                mensaje="Nombre invalido"
            elif self.contraseña.get()!=b:
                #messagebox.showerror("Error" , "contraseña invalida", parent=self.root)
                mensaje="contraseña invalida"
            #if nombre_usuario.get()!=a or contraseña.get()!=b:
                #mensaje="Usuario y contraseña incorrecta"
                
            else:
                #messagebox.showinfo("Bienvenido", f"Bienvenido {self.Nombre_usuario.get()}")
                mensaje="Bienvenido"
                ventana.withdraw()
            obj_m=Mensajes()
            obj_m.Mensaje_login(mensaje)
        
if __name__=="__main__":
    ventana = Tk()
    ob= Login(ventana)
    ventana.mainloop()