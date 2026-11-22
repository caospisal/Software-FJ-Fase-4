
# SOFTWARE FJ
## Sistema Integral de Gestión de Clientes, Servicios y Reservas

### Descripción del proyecto

Software FJ es una aplicación desarrollada en Python que permite gestionar clientes, servicios y reservas de una empresa dedicada a ofrecer espacios para reuniones, alquiler de equipos y asesorías especializadas.

El sistema fue desarrollado aplicando los principios de programación orientada a objetos y manejo de excepciones, con el propósito de garantizar una gestión organizada y un funcionamiento estable ante diferentes situaciones de error.

### Objetivo

Desarrollar una aplicación modular que permita administrar clientes, servicios y reservas mediante objetos y listas internas, incorporando validaciones, cálculos de costos y manejo de errores sin utilizar bases de datos.

### Funcionalidades principales

- Registro y validación de clientes.
- Gestión de reservas de salas.
- Alquiler de equipos.
- Registro de asesorías especializadas.
- Cálculo de costos según duración, cantidad, descuentos e impuestos.
- Confirmación y cancelación de reservas.
- Validación de datos y parámetros.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores en el archivo `logs.txt`.
- Interfaz gráfica desarrollada con Tkinter.

### Tecnologías utilizadas

- Python.
- Tkinter.
- Programación orientada a objetos.
- Manejo de excepciones.
- Archivos de registro (logs).

### Estructura del proyecto

```text
SOFTWARE_FJ/
│
├── Main.py
├── Entidades.py
├── Servicios.py
├── Reservas.py
├── Excepciones.py
├── Interfaz.py
├── Pruebas.py
├── logs.txt
└── README.md
```

### Ejecución del programa

1. Instalar Python en el equipo.
2. Descargar o clonar este repositorio.
3. Abrir la carpeta del proyecto en Visual Studio Code.
4. Ejecutar el archivo principal:

```bash
python Main.py
```

### Ejecución de pruebas

Para ejecutar las pruebas del sistema desde la terminal:

```bash
python Pruebas.py
```

El archivo de pruebas permite verificar el registro de clientes, creación de servicios, gestión de reservas y manejo de excepciones.

### Programación orientada a objetos

En el desarrollo se implementaron los siguientes conceptos:

- Abstracción.
- Herencia.
- Encapsulación.
- Polimorfismo.
- Métodos con parámetros opcionales para el cálculo de costos.

### Manejo de excepciones

El sistema incorpora excepciones personalizadas, bloques `try`, `except`, `else` y `finally`, además de encadenamiento de excepciones.

Los eventos y errores relevantes se registran en el archivo `logs.txt`.

### Información académica

**Universidad:** Universidad Nacional Abierta y a Distancia (UNAD).

**Programa:** Ingeniería de Sistemas.

**Curso:** Programación.

**Código:** 213023A_2204.

**Actividad:** Fase 4 - Prácticas simuladas.

**Proyecto:** Sistema Integral de Gestión de Clientes, Servicios y Reservas.

### Autor

Carlos Alberto Piñeros Salcedo.
