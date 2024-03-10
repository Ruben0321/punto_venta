import Cliente
import Proveedores
import Productos
import Ventas
class Reporte:
    def __init__(self, p_cli=Cliente, p_pr=Proveedores,p_pro=Productos,p_ve=Ventas):
        self.clientes=p_cli
        self.proveedores=p_pr
        self.productos=p_pro
        self.ventas=p_ve
    