from models.pizza import Pizza
from models.cliente import Cliente

from datetime import datetime


class Pedido:
    #_id_pedido_contador = 2000
    _estado_pizza = "Pendiente"

    #Constructor
    def __init__(self,cliente:Cliente, pizza:Pizza, estado = _estado_pizza) -> None:
        self.__id_pedido = None
        self.__id_cliente = cliente.id_cliente
        self.__id_pizza = pizza.id_pizza
        self.__estado_pedido = estado
        self.__tiempo_preparacion = pizza.tiempo_preparacion
        self.__fecha_pedido = datetime.now()

    #Setter y Getter
    @property
    def id_pedido(self) -> int:
        return self.__id_pedido

    @property
    def id_cliente(self) -> int:
        return self.__id_cliente

    @property
    def id_pizza(self) -> int:
        return self.__id_pizza

    @property
    def estado_pedido(self) -> str:
        return self.__estado_pedido

    @estado_pedido.setter
    def estado_pedido(self,estado_pedido) -> None:
        self.__estado_pedido = estado_pedido

    @property
    def tiempo_preparacion(self) -> str:
        return self.__tiempo_preparacion

    @property
    def fecha_pedido(self) -> datetime:
        return self.__fecha_pedido

    #---------------------------------------------
    #Método para asignar id al cliente
    #def asignar_id(self) -> int:
    #    Pedido._id_pedido_contador += 1
    #    return Pedido._id_pedido_contador
    #---------------------------------------------

    #Método STR
    def __str__(self) -> str:
        return f'''
    Detalle pedido:
    --------------------------------------------------------
    ID Pedido: {self.id_pedido}
    ID Cliente: {self.id_cliente}
    ID Pizza: {self.id_pizza}
    Estado: {self.estado_pedido}
    Tiempo preparación: {self.tiempo_preparacion} minutos
    Fecha pedido: {self.fecha_pedido.strftime("%d-%m-%Y / %H:%M:%S")}
    --------------------------------------------------------
    '''
