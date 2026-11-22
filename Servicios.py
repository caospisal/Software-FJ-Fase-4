
from abc import ABC, abstractmethod
import math

from Excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)


class Servicio(ABC):

    def __init__(self, nombre, precio_base, disponible=True):
        if not nombre or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del servicio no puede estar vacio."
            )

        if (
            not isinstance(precio_base, (int, float))
            or isinstance(precio_base, bool)
            or not math.isfinite(precio_base)
            or precio_base <= 0
        ):
            raise DatosInvalidosError(
                "El precio base debe ser un numero positivo."
            )

        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = disponible

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        self._disponible = bool(valor)

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    def _calcular_total(self, duracion=1, descuento=0, impuesto=19):

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or not math.isfinite(duracion)
            or duracion <= 0
        ):
            raise DatosInvalidosError(
                "La duracion debe ser un numero positivo."
            )

        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or not math.isfinite(descuento)
            or descuento < 0
            or descuento > 100
        ):
            raise DatosInvalidosError(
                "El descuento debe estar entre 0 y 100."
            )

        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or not math.isfinite(impuesto)
            or impuesto < 0
        ):
            raise DatosInvalidosError(
                "El impuesto no puede ser negativo."
            )

        subtotal = self._precio_base * duracion

        valor_descuento = subtotal * (descuento / 100)
        subtotal -= valor_descuento

        valor_impuesto = subtotal * (impuesto / 100)
        total = subtotal + valor_impuesto

        return round(total, 2)

    @abstractmethod
    def calcular_costo(self, duracion=1, descuento=0, impuesto=19):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass


class ReservaSala(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        capacidad,
        disponible=True
    ):
        super().__init__(nombre, precio_base, disponible)

        if (
            not isinstance(capacidad, int)
            or isinstance(capacidad, bool)
            or capacidad <= 0
        ):
            raise DatosInvalidosError(
                "La capacidad debe ser un entero positivo."
            )

        self.capacidad = capacidad

    def validar_parametros(self):
        if self.capacidad <= 0:
            raise DatosInvalidosError(
                "La capacidad de la sala no es valida."
            )

    def calcular_costo(self, duracion=1, descuento=0, impuesto=19):

        if not self.disponible:
            raise ServicioNoDisponibleError(
                "La sala no esta disponible."
            )

        self.validar_parametros()

        return self._calcular_total(
            duracion,
            descuento,
            impuesto
        )

    def describir_servicio(self):
        return (
            f"Sala: {self.nombre} | "
            f"Capacidad: {self.capacidad} personas | "
            f"Precio por hora: ${self.precio_base}"
        )


class AlquilerEquipo(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        cantidad,
        disponible=True
    ):
        super().__init__(nombre, precio_base, disponible)

        if (
            not isinstance(cantidad, int)
            or isinstance(cantidad, bool)
            or cantidad <= 0
        ):
            raise DatosInvalidosError(
                "La cantidad de equipos debe ser un entero positivo."
            )

        self.cantidad = cantidad

    def validar_parametros(self):
        if self.cantidad <= 0:
            raise DatosInvalidosError(
                "La cantidad de equipos no es valida."
            )

    def calcular_costo(self, duracion=1, descuento=0, impuesto=19):

        if not self.disponible:
            raise ServicioNoDisponibleError(
                "El equipo no esta disponible."
            )

        self.validar_parametros()

        total = self._calcular_total(
            duracion,
            descuento,
            impuesto
        )

        return round(total * self.cantidad, 2)

    def describir_servicio(self):
        return (
            f"Alquiler de equipos: {self.nombre} | "
            f"Cantidad: {self.cantidad} | "
            f"Precio por unidad: ${self.precio_base}"
        )


class Asesoria(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        modalidad,
        disponible=True
    ):
        super().__init__(nombre, precio_base, disponible)

        if modalidad.lower() not in ["virtual", "presencial"]:
            raise DatosInvalidosError(
                "La modalidad debe ser virtual o presencial."
            )

        self.modalidad = modalidad.lower()

    def validar_parametros(self):
        if self.modalidad not in ["virtual", "presencial"]:
            raise DatosInvalidosError(
                "La modalidad de asesoria no es valida."
            )

    def calcular_costo(self, duracion=1, descuento=0, impuesto=19):

        if not self.disponible:
            raise ServicioNoDisponibleError(
                "La asesoria no esta disponible."
            )

        self.validar_parametros()

        total = self._calcular_total(
            duracion,
            descuento,
            impuesto
        )

        if self.modalidad == "presencial":
            total = total * 1.20

        return round(total, 2)

    def describir_servicio(self):
        return (
            f"Asesoria: {self.nombre} | "
            f"Modalidad: {self.modalidad} | "
            f"Precio por hora: ${self.precio_base}"
        )
