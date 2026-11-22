
import logging

from Entidades import Cliente

from Servicios import (
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)

from Reservas import Reserva

from Excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError
)


# Configuracion del registro de eventos y errores
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)


print("========================================")
print(" PRUEBAS DEL SISTEMA SOFTWARE FJ")
print("========================================")


# PRUEBA 1: Registro de cliente valido
print("\nPRUEBA 1: Registro de cliente valido")

try:
    cliente1 = Cliente(
        "1001",
        "Carlos",
        "carlos@gmail.com",
        "3001234567"
    )

    print("Cliente registrado correctamente.")
    print(cliente1.mostrar_informacion())

except Exception as error:
    print("Error:", error)
    logging.exception("Prueba 1: error al registrar cliente")


# PRUEBA 2: Registro de cliente con correo invalido
print("\nPRUEBA 2: Registro de cliente con correo invalido")

try:
    cliente_invalido = Cliente(
        "1002",
        "Andres",
        "correo_incorrecto",
        "3001234567"
    )

except DatosInvalidosError as error:
    print("Error controlado correctamente:", error)
    logging.exception("Prueba 2: correo invalido")

else:
    print("El cliente fue registrado.")

finally:
    print("Finalizo la prueba 2.")


# PRUEBA 3: Registro de un segundo cliente valido
print("\nPRUEBA 3: Registro de segundo cliente")

try:
    cliente2 = Cliente(
        "1003",
        "Maria",
        "maria@gmail.com",
        "3101234567"
    )

    print("Segundo cliente registrado correctamente.")

except Exception as error:
    print("Error:", error)
    logging.exception("Prueba 3: error al registrar segundo cliente")


# PRUEBA 4: Creacion de una sala
print("\nPRUEBA 4: Creacion de servicio de sala")

try:
    sala = ReservaSala(
        "Sala de reuniones",
        50000,
        20
    )

    print(sala.describir_servicio())
    logging.info("Prueba 4: sala creada correctamente")

except Exception as error:
    print("Error:", error)
    logging.exception("Prueba 4: error al crear sala")


# PRUEBA 5: Creacion de alquiler de equipos
print("\nPRUEBA 5: Creacion de alquiler de equipos")

try:
    equipo = AlquilerEquipo(
        "Computadores",
        30000,
        3
    )

    print(equipo.describir_servicio())
    logging.info("Prueba 5: alquiler de equipos creado")

except Exception as error:
    print("Error:", error)
    logging.exception("Prueba 5: error al crear equipos")


# PRUEBA 6: Creacion de asesoria
print("\nPRUEBA 6: Creacion de asesoria")

try:
    asesoria = Asesoria(
        "Asesoria especializada",
        80000,
        "presencial"
    )

    print(asesoria.describir_servicio())

    costo = asesoria.calcular_costo(
        duracion=2,
        descuento=10,
        impuesto=19
    )

    print("Costo de la asesoria presencial:", costo)

    logging.info("Prueba 6: asesoria creada correctamente")

except Exception as error:
    print("Error:", error)
    logging.exception("Prueba 6: error al crear asesoria")


# PRUEBA 7: Creacion incorrecta de servicio
print("\nPRUEBA 7: Creacion de sala con capacidad invalida")

try:
    sala_invalida = ReservaSala(
        "Sala pequeña",
        40000,
        0
    )

except DatosInvalidosError as error:
    print("Error controlado correctamente:", error)
    logging.exception("Prueba 7: capacidad de sala invalida")

else:
    print("La sala fue creada correctamente.")

finally:
    print("Finalizo la prueba 7.")


# PRUEBA 8: Creacion y confirmacion de reserva
print("\nPRUEBA 8: Reserva confirmada")

try:
    reserva1 = Reserva(
        "RES001",
        cliente1,
        sala,
        2
    )

    reserva1.confirmar()

    print("Reserva confirmada correctamente.")
    print("Costo de la reserva:", reserva1.costo)

    logging.info("Prueba 8: reserva confirmada")

except Exception as error:
    print("Error:", error)
    logging.exception("Prueba 8: error al confirmar reserva")


# PRUEBA 9: Creacion y cancelacion de reserva
print("\nPRUEBA 9: Reserva cancelada")

try:
    reserva2 = Reserva(
        "RES002",
        cliente2,
        equipo,
        1
    )

    reserva2.cancelar()

    print("Reserva cancelada correctamente.")
    print("Estado:", reserva2.estado)

    logging.info("Prueba 9: reserva cancelada")

except Exception as error:
    print("Error:", error)
    logging.exception("Prueba 9: error al cancelar reserva")


# PRUEBA 10: Reserva con cliente invalido
print("\nPRUEBA 10: Reserva con cliente invalido")

try:
    reserva_invalida = Reserva(
        "RES003",
        None,
        sala,
        1
    )

except Exception as error:
    print("Error controlado correctamente:", error)
    logging.exception("Prueba 10: reserva con cliente invalido")

else:
    print("La reserva fue creada.")

finally:
    print("Finalizo la prueba 10.")


# PRUEBA 11: Reserva con servicio no disponible
print("\nPRUEBA 11: Servicio no disponible")

try:
    sala.disponible = False

    reserva3 = Reserva(
        "RES004",
        cliente1,
        sala,
        1
    )

    reserva3.confirmar()

except ReservaInvalidaError as error:
    print("Error controlado correctamente:", error)

    if error.__cause__:
        print("Causa original:", error.__cause__)

    logging.exception(
        "Prueba 11: reserva con servicio no disponible"
    )

else:
    print("La reserva fue confirmada.")

finally:
    sala.disponible = True
    print("Finalizo la prueba 11.")


# PRUEBA 12: Demostracion explicita del uso de raise
print("\nPRUEBA 12: Uso explicito de raise")

try:
    raise DatosInvalidosError(
        "Error generado intencionalmente para demostrar raise."
    )

except DatosInvalidosError as error:
    print("Excepcion generada correctamente:", error)

    logging.exception(
        "Prueba 12: demostracion del uso de raise"
    )

finally:
    print("Finalizo la prueba 12.")


# RESULTADO FINAL
print("\n========================================")
print("EL SISTEMA CONTINUA FUNCIONANDO")
print("PRUEBAS FINALIZADAS")
print("========================================")

logging.info("Todas las pruebas del sistema finalizaron.")
