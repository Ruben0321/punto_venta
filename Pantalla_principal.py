from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
class Pantallas:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Pantalla Administrador")
        self.ventana.geometry("1200x630+100+50")
        ttk.Separator(
        self.ventana
        ).grid(row=2, column=0, columnspan=7, sticky="EW")
        textos=["CLIENTE", "PEDIDOS", "PRODUCTOS", "PROVEEDORES", "REPORTE","USUARIO","VENTAS"]
        botones=[]
        for texto in textos:
            boton=Button(self.ventana,cursor="hand2", text=texto,width=20,height=10)
            botones.append(boton)
        
        for i in range (7):
            fila=i//7
            columna=i%7
            botones[i].grid(row=fila,column=columna,padx=5, pady=5)
            botones[i].config(command=lambda i=i: self.botones(i))
        self.ventana.mainloop()
    def botones(self,index):
        if index == 0: 
            ventana_cliente = tk.Toplevel(self.ventana)
            ventana_cliente.title("Ventana del Cliente")
            ventana_cliente.geometry("1200x630+100+50")
        
        elif index == 1:
            ventana_pedidos = tk.Toplevel(self.ventana)
            ventana_pedidos.title("Ventana del Pedido")
            ventana_pedidos.geometry("1200x630+100+50")
            
        elif index == 2:
            ventana_productos = tk.Toplevel(self.ventana)
            ventana_productos.title("Ventana Producto")
            ventana_productos.geometry("425x1000+500+50")
            Marco_productos= Frame(ventana_productos, bg="white")
            Marco_productos.place(x=0, y=0, width=500, height=1000)
            Label(Marco_productos,text="Productos", font=("Verdana", 20, "bold"), fg="#800080",bg="white").place(x=115, y=10)
            Label(Marco_productos,text="Clave", font=("Verdana", 20, "bold"), bg="white").place(x=15, y=60)
            Label(Marco_productos,text="Nombre", font=("Verdana", 20, "bold"), bg="white").place(x=15, y=120)
            Label(Marco_productos,text="Descripcion", font=("Verdana", 20, "bold"),bg="white").place(x=15, y=180)
            Label(Marco_productos,text="Precio", font=("Verdana", 20, "bold"), bg="white").place(x=15, y=240)
             
        elif index == 3:
            ventana_proveedores = tk.Toplevel(self.ventana)
            ventana_proveedores.title("Ventana del Pedido")
            ventana_proveedores.geometry("1200x630+100+50")
            
        elif index == 4:
            ventana_reporte = tk.Toplevel(self.ventana)
            ventana_reporte.title("Ventana del Pedido")
            ventana_reporte.geometry("1200x630+100+50")
            
        elif index == 5:
            ventana_usuario = tk.Toplevel(self.ventana)
            ventana_usuario.title("Ventana del Pedido")
            ventana_usuario.geometry("1200x630+100+50")
            
        elif index == 6:
            ventana_ventas = tk.Toplevel(self.ventana)
            ventana_ventas.title("Ventana del Pedido")
            ventana_ventas.geometry("1200x630+100+50")