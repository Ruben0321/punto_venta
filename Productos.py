import Pedidos
class Productos:
    def __init__(self, p_cantidad=int(), p_descripcion=str(),p_id=int,p_nombre=str(),p_pedi=Pedidos,p_talla=float()):
        self.cantidad= p_cantidad
        self.descripcion=p_descripcion
        self.id=p_id
        self.nombre=p_nombre
        self.pedido= p_pedi
        self.talla=p_talla
    def consultarClie(self):
        return self
    def eliminarClie(self):
        return self
    def modificarClie(self):
        return self
    def mostrarClie(self):
        return self
    def registrarClie(self):
        return self