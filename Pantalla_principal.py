from tkinter import *
class Pantallas:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Pantalla Administrador")
        self.ventana.geometry("500x500+70+50")
        cliente= Button(self.ventana,cursor="hand2",text="CLIENTE", bd=0,font=("Roboto", 15), bg="#00FF00", fg="white").place(x=20, y=10,width=180,height=30)
        pedidos= Button(self.ventana,cursor="hand2",text="PEDIDOS", bd=0,font=("Roboto", 15), bg="#00FF00", fg="white").place(x=20, y=50,width=180,height=30)
        productos= Button(self.ventana,cursor="hand2",text="PRODUCTOS", bd=0,font=("Roboto", 15), bg="#00FF00", fg="white").place(x=20, y=90,width=180,height=30)
        proveedores= Button(self.ventana,cursor="hand2",text="PROVEEDORES", bd=0,font=("Roboto", 15), bg="#00FF00", fg="white").place(x=20, y=140,width=180,height=30)
        reporte= Button(self.ventana,cursor="hand2",text="REPORTE", bd=0,font=("Roboto", 15), bg="#00FF00", fg="white").place(x=20, y=190,width=180,height=30)
        usuario= Button(self.ventana,cursor="hand2",text="USUARIO", bd=0,font=("Roboto", 15), bg="#00FF00", fg="white").place(x=20, y=230,width=180,height=30)
        ventas= Button(self.ventana,cursor="hand2",text="VENTAS", bd=0,font=("Roboto", 15), bg="#00FF00", fg="white").place(x=20, y=270,width=180,height=30)
        self.ventana.mainloop()
