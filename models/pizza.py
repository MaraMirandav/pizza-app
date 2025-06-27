class Pizza:
    #_id_pizza_contador = 1000

    #Constructor
    def __init__(self, masa:str, salsa:str, ingredientes:list[str]) -> None:
        self.__id_pizza = None
        self.__masa = masa
        self.__salsa = salsa
        self.__ingredientes = ingredientes
        self.__tiempo_preparacion = self.calcular_tiempo_preparacion()

    #Setter /Getter
    @property
    def id_pizza(self) -> str:
        return self.__id_pizza

    @property
    def masa(self) -> str:
        return self.__masa

    @masa.setter
    def masa(self,nueva_masa) -> None:
        self.__masa = nueva_masa

    @property
    def salsa(self) -> str:
        return self.__salsa

    @salsa.setter
    def salsa(self,nueva_salsa) -> None:
        self.__salsa = nueva_salsa

    @property
    def ingredientes(self) -> list[str]:
        return self.__ingredientes

    @ingredientes.setter
    def ingredientes(self,nuevos_ingredientes) -> None:
        self.__ingredientes = nuevos_ingredientes

    @property
    def tiempo_preparacion(self):
        return self.__tiempo_preparacion

    #Método para asignar el tiempo de preparación
    def calcular_tiempo_preparacion(self) -> int:
        tiempo_base_preparacion = 20
        tiempo_total_preparacion = tiempo_base_preparacion + len(self.ingredientes) * 2
        return tiempo_total_preparacion

    #---------------------------------------------
    # #Función para asignar id al cliente
    # def asignar_id(self) -> int:
    #     Pizza._id_pizza_contador += 1
    #     return Pizza._id_pizza_contador
    #---------------------------------------------

    #Método STR
    def __str__(self) -> str:
        return f'''
    Pizza:
    --------------------------------------------------------
    ID pizza: {self.id_pizza}
    Masa: {self.masa}
    Salsa: {self.salsa}
    Ingredientes: {', '.join(self.ingredientes)}
    Tiempo preparación: {self.tiempo_preparacion} minutos
    --------------------------------------------------------
    '''