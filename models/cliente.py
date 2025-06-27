class Cliente:
    #_id_cliente_contador = 0

    #Constructor
    def __init__(self, nombre:str, telefono:str, direccion:str, email:str) -> None:
        self.__id_cliente = None
        self.__nombre = nombre
        self.__telefono = telefono
        self.__direccion = direccion
        self.__email = email

    #Setter / Getter
    @property
    def id_cliente(self) -> int:
        return self.__id_cliente

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self,nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre

    @property
    def telefono(self) -> str:
        return self.__telefono

    @telefono.setter
    def telefono(self,nuevo_telefono) -> None:
        self.__telefono = nuevo_telefono

    @property
    def direccion(self) -> str:
        return self.__direccion

    @direccion.setter
    def direccion(self,nueva_direccion) -> None:
        self.__direccion = nueva_direccion

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self,nuevo_email) -> None:
        self.__email = nuevo_email

    #---------------------------------------------
    #Método para asignar id al cliente
    # def asignar_id(self) -> int:
    #     Cliente._id_cliente_contador += 1
    #     return Cliente._id_cliente_contador
    #---------------------------------------------

    #Método STR
    def __str__(self) -> str:
        return f'''
    Datos Cliente:
    --------------------------------------------------------
    ID cliente: {self.id_cliente}
    Cliente: {self.nombre}
    Telefono: {self.telefono}
    Dirección: {self.direccion}
    Correo: {self.email}
    --------------------------------------------------------
    '''
