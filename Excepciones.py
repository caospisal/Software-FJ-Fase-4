
# Excepciones personalizadas del sistema 

class SistemaFJError(Exception):
    """Excepcion base del sistema."""
    pass


class DatosInvalidosError(SistemaFJError):
    """Se produce cuando los datos ingresados no son validos."""
    pass


class ClienteDuplicadoError(SistemaFJError):
    """Se produce cuando un cliente ya se encuentra registrado."""
    pass


class ServicioNoDisponibleError(SistemaFJError):
    """Se produce cuando un servicio no esta disponible."""
    pass


class ReservaInvalidaError(SistemaFJError):
    """Se produce cuando una reserva tiene datos incorrectos."""
    pass


class OperacionNoPermitidaError(SistemaFJError):
    """Se produce cuando se intenta realizar una operacion no permitida."""
    pass
