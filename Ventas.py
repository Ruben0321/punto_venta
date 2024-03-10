import Productos
import Ticket
class Ventas:
    def __init__(self,p_cantidad=int(),p_cliente=str(),p_fecha=str(),p_id=int(),p_prodd=Productos(), p_producto=str(),p_tic=Ticket,p_total=float()):
        self.cantidad= p_cantidad
        self.cliente= p_cliente
        self.fecha= p_fecha
        self.id= p_id
        self.prodd=p_prodd
        self.productos= p_producto
        self.ticket= p_tic
        self.total= p_total
    def consultarVent(self):
        return Ventas
    def eliminarVent(self):
        return Ventas
    def modificarVent(self):
        return Ventas
    def registrarVent(self):
        return Ventas