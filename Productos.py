import Pedidos
class Productos:
    def __init__(self, p_cantidad=int(), p_descripcion=str(),p_id=int,p_nombre=str(),p_pedi=Pedidos,p_talla=float()):
        self.cantidad= p_cantidad
        self.descripcion=p_descripcion
        self.id=p_id
        self.nombre=p_nombre
        self.pedido= p_pedi
        self.talla=p_talla
    def consultarPro(self):
        return self
    def eliminarPro(self):
        return self
    def modificarPro(self):
        return self
    def mostrarPro(self):
        return self
    def registrarPro(self):
        return self