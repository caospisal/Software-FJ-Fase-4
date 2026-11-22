
from Entidades import Cliente
from Servicios import Servicio
from Excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError
)


class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion):

        # Validar codigo
        if not codigo or not codigo.strip():
            raise DatosInvalidosError("El codigo de reserva es obligatorio.")

        # Validar cliente
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("Debe seleccionar un cliente valido.")

        # Validar servicio
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("Debe seleccionar un servicio valido.")

        # Validar duracion
        if (isinstance(duracion, bool)
                or not isinstance(duracion, (int, float))
                or duracion <= 0):
            raise DatosInvalidosError("La duracion debe ser mayor que cero.")

        self.__codigo = codigo
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = 0
        self.__procesando = False

    # Metodo para procesar la reserva
    def procesar(self):

        if self.__estado == "Cancelada":
            raise ReservaInvalidaError(
                "No se puede procesar una reserva cancelada."
            )

        if self.__procesando:
            raise ReservaInvalidaError(
                "La reserva ya se encuentra en procesamiento."
            )

        self.__procesando = True

        try:
            costo = self.__servicio.calcular_costo(
                duracion=self.__duracion
            )

        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible procesar la reserva."
            ) from error

        else:
            self.__costo = costo
            return costo

        finally:
            self.__procesando = False

    # Metodo para confirmar la reserva
    def confirmar(self):

        if self.__estado != "Pendiente":
            raise ReservaInvalidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        costo = self.procesar()
        self.__estado = "Confirmada"

        return costo

    # Metodo para cancelar la reserva
    def cancelar(self):

        if self.__estado == "Cancelada":
            raise ReservaInvalidaError(
                "La reserva ya se encuentra cancelada."
            )

        self.__estado = "Cancelada"

        return "Reserva cancelada correctamente."

    # Metodo para consultar la informacion
    def mostrar_informacion(self):

        return (
            f"Codigo: {self.__codigo}\n"
            f"Cliente: {self.__cliente.mostrar_informacion()}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duracion: {self.__duracion} horas\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo:,.2f}"
        )

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion