from tkinter import messagebox
from Pantalla_principal import Pantallas
class Mensajes:
    def Mensaje_login(self,mensaje):
        if mensaje=="Bienvenido":
            self.Pantalla=Pantallas()
        else:
            messagebox.showinfo("Error" , mensaje)
