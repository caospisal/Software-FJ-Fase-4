
from abc import ABC, abstractmethod
import re

from Excepciones import DatosInvalidosError


# Clase abstracta que representa las entidades del sistema
class Entidad(ABC):

    def __init__(self, identificacion, nombre):

        if not identificacion or not identificacion.strip():
            raise DatosInvalidosError("La identificacion es obligatoria.")

        if not nombre or not nombre.strip():
            raise DatosInvalidosError("El nombre es obligatorio.")

        self._identificacion = identificacion
        self._nombre = nombre

    @abstractmethod
    def mostrar_informacion(self):
        pass


# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        super().__init__(identificacion, nombre)

        # Validar correo electronico
        patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron_correo, correo):
            raise DatosInvalidosError("El correo electronico no es valido.")

        # Validar telefono
        if not telefono.isdigit() or len(telefono) < 7:
            raise DatosInvalidosError("El telefono debe tener minimo 7 digitos.")

        # Atributos encapsulados
        self.__correo = correo
        self.__telefono = telefono

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):

        return (
            f"Identificacion: {self._identificacion}\n"
            f"Nombre: {self._nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )
