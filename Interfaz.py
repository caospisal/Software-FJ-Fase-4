
import tkinter as tk
from tkinter import ttk, messagebox
import logging

from Entidades import Cliente
from Servicios import ReservaSala, AlquilerEquipo, Asesoria
from Reservas import Reserva
from Excepciones import SistemaFJError


# ==========================================
# CONFIGURACION DEL REGISTRO DE EVENTOS
# ==========================================

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# ==========================================
# CLASE PRINCIPAL DE LA APLICACION
# ==========================================

class AplicacionSoftwareFJ:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Software FJ - Sistema de Gestion")
        self.ventana.geometry("950x650")
        self.ventana.minsize(800, 550)
        self.ventana.configure(bg="#E9EEF5")

        # Listas para almacenar los objetos
        self.clientes = []
        self.servicios = []
        self.reservas = {}

        # Diccionarios para relacionar los objetos
        self.mapa_clientes = {}
        self.mapa_servicios = {}

        self.configurar_estilo()
        self.crear_interfaz()

        logging.info("Aplicacion Software FJ iniciada.")

    # ==========================================
    # CONFIGURACION VISUAL
    # ==========================================

    def configurar_estilo(self):

        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "TNotebook",
            background="#E9EEF5",
            borderwidth=0
        )

        estilo.configure(
            "TNotebook.Tab",
            padding=(20, 10),
            font=("Arial", 10, "bold")
        )

        estilo.configure(
            "Treeview",
            rowheight=28,
            font=("Arial", 9)
        )

        estilo.configure(
            "Treeview.Heading",
            font=("Arial", 9, "bold")
        )

        estilo.configure(
            "TButton",
            font=("Arial", 9),
            padding=6
        )

    # ==========================================
    # VENTANA PRINCIPAL
    # ==========================================

    def crear_interfaz(self):

        encabezado = tk.Frame(
            self.ventana,
            bg="#19385B",
            height=90
        )

        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            text="SOFTWARE FJ",
            font=("Arial", 22, "bold"),
            fg="white",
            bg="#19385B"
        ).pack(pady=(15, 2))

        tk.Label(
            encabezado,
            text="Sistema Integral de Gestion de Clientes, Servicios y Reservas",
            font=("Arial", 10),
            fg="#D5E3F5",
            bg="#19385B"
        ).pack()

        # Crear pestañas
        self.pestanas = ttk.Notebook(self.ventana)

        self.pestanas.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        self.pestana_clientes = ttk.Frame(self.pestanas)
        self.pestana_servicios = ttk.Frame(self.pestanas)
        self.pestana_reservas = ttk.Frame(self.pestanas)

        self.pestanas.add(
            self.pestana_clientes,
            text="Clientes"
        )

        self.pestanas.add(
            self.pestana_servicios,
            text="Servicios"
        )

        self.pestanas.add(
            self.pestana_reservas,
            text="Reservas"
        )

        # Construir cada modulo
        self.crear_modulo_clientes()
        self.crear_modulo_servicios()
        self.crear_modulo_reservas()

        tk.Label(
            self.ventana,
            text="Software FJ | Gestion empresarial",
            bg="#E9EEF5",
            fg="#536477",
            font=("Arial", 9)
        ).pack(pady=5)

    # ==========================================
    # MODULO DE CLIENTES
    # ==========================================

    def crear_modulo_clientes(self):

        marco = ttk.LabelFrame(
            self.pestana_clientes,
            text="Registrar nuevo cliente",
            padding=15
        )

        marco.pack(fill="x", padx=15, pady=15)

        self.id_cliente = tk.Entry(marco)
        self.nombre_cliente = tk.Entry(marco)
        self.correo_cliente = tk.Entry(marco)
        self.telefono_cliente = tk.Entry(marco)

        campos = [
            ("Identificacion:", self.id_cliente),
            ("Nombre completo:", self.nombre_cliente),
            ("Correo electronico:", self.correo_cliente),
            ("Telefono:", self.telefono_cliente)
        ]

        for i, (texto, entrada) in enumerate(campos):

            ttk.Label(
                marco,
                text=texto
            ).grid(
                row=i,
                column=0,
                sticky="w",
                pady=5
            )

            entrada.grid(
                row=i,
                column=1,
                sticky="ew",
                padx=10,
                pady=5
            )

        marco.columnconfigure(1, weight=1)

        ttk.Button(
            marco,
            text="Registrar cliente",
            command=self.registrar_cliente
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            pady=10
        )

        # Tabla de clientes
        tabla = ttk.LabelFrame(
            self.pestana_clientes,
            text="Clientes registrados",
            padding=10
        )

        tabla.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        columnas = (
            "identificacion",
            "nombre",
            "correo",
            "telefono"
        )

        self.tabla_clientes = ttk.Treeview(
            tabla,
            columns=columnas,
            show="headings"
        )

        titulos = [
            ("identificacion", "Identificacion"),
            ("nombre", "Nombre"),
            ("correo", "Correo"),
            ("telefono", "Telefono")
        ]

        for columna, titulo in titulos:

            self.tabla_clientes.heading(
                columna,
                text=titulo
            )

            self.tabla_clientes.column(
                columna,
                width=170
            )

        self.tabla_clientes.pack(
            fill="both",
            expand=True
        )

    def registrar_cliente(self):

        try:

            identificacion = self.id_cliente.get().strip()
            nombre = self.nombre_cliente.get().strip()
            correo = self.correo_cliente.get().strip()
            telefono = self.telefono_cliente.get().strip()

            # Verificar clientes duplicados
            for cliente in self.clientes:

                if cliente._identificacion == identificacion:

                    raise SistemaFJError(
                        "El cliente ya se encuentra registrado."
                    )

            # Crear objeto cliente
            cliente = Cliente(
                identificacion,
                nombre,
                correo,
                telefono
            )

            self.clientes.append(cliente)

            self.tabla_clientes.insert(
                "",
                "end",
                values=(
                    identificacion,
                    nombre,
                    correo,
                    telefono
                )
            )

            logging.info(
                "Cliente registrado: %s",
                identificacion
            )

            messagebox.showinfo(
                "Registro exitoso",
                "El cliente fue registrado correctamente."
            )

            # Limpiar campos
            self.id_cliente.delete(0, tk.END)
            self.nombre_cliente.delete(0, tk.END)
            self.correo_cliente.delete(0, tk.END)
            self.telefono_cliente.delete(0, tk.END)

            self.actualizar_clientes_reserva()

        except (SistemaFJError, ValueError) as error:

            logging.exception("Error al registrar cliente")

            messagebox.showerror(
                "Error de validacion",
                str(error)
            )

        except Exception as error:

            logging.exception("Error inesperado al registrar cliente")

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==========================================
    # MODULO DE SERVICIOS
    # ==========================================

    def crear_modulo_servicios(self):

        marco = ttk.LabelFrame(
            self.pestana_servicios,
            text="Registrar servicio",
            padding=15
        )

        marco.pack(
            fill="x",
            padx=15,
            pady=15
        )

        ttk.Label(
            marco,
            text="Tipo de servicio:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=5
        )

        self.tipo_servicio = ttk.Combobox(
            marco,
            values=[
                "Reserva de sala",
                "Alquiler de equipo",
                "Asesoria especializada"
            ],
            state="readonly"
        )

        self.tipo_servicio.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=10,
            pady=5
        )

        ttk.Label(
            marco,
            text="Nombre:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=5
        )

        self.nombre_servicio = tk.Entry(marco)

        self.nombre_servicio.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=10,
            pady=5
        )

        ttk.Label(
            marco,
            text="Precio por hora:"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=5
        )

        self.precio_servicio = tk.Entry(marco)

        self.precio_servicio.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=10,
            pady=5
        )

        ttk.Label(
            marco,
            text="Capacidad / Cantidad / Modalidad:"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            pady=5
        )

        self.dato_servicio = tk.Entry(marco)

        self.dato_servicio.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=10,
            pady=5
        )

        marco.columnconfigure(1, weight=1)

        ttk.Button(
            marco,
            text="Registrar servicio",
            command=self.registrar_servicio
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            pady=10
        )

        # Tabla de servicios
        tabla = ttk.LabelFrame(
            self.pestana_servicios,
            text="Servicios registrados",
            padding=10
        )

        tabla.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        columnas = (
            "tipo",
            "nombre",
            "precio",
            "detalle"
        )

        self.tabla_servicios = ttk.Treeview(
            tabla,
            columns=columnas,
            show="headings"
        )

        titulos = [
            ("tipo", "Tipo"),
            ("nombre", "Nombre"),
            ("precio", "Precio por hora"),
            ("detalle", "Detalle")
        ]

        for columna, titulo in titulos:

            self.tabla_servicios.heading(
                columna,
                text=titulo
            )

            self.tabla_servicios.column(
                columna,
                width=180
            )

        self.tabla_servicios.pack(
            fill="both",
            expand=True
        )

    def registrar_servicio(self):

        try:

            tipo = self.tipo_servicio.get()
            nombre = self.nombre_servicio.get().strip()
            precio = float(self.precio_servicio.get())
            dato = self.dato_servicio.get().strip()

            # Crear servicio segun su tipo
            if tipo == "Reserva de sala":

                servicio = ReservaSala(
                    nombre,
                    precio,
                    int(dato)
                )

                detalle = f"Capacidad: {dato} personas"

            elif tipo == "Alquiler de equipo":

                servicio = AlquilerEquipo(
                    nombre,
                    precio,
                    int(dato)
                )

                detalle = f"Cantidad: {dato}"

            elif tipo == "Asesoria especializada":

                servicio = Asesoria(
                    nombre,
                    precio,
                    dato
                )

                detalle = f"Modalidad: {dato}"

            else:

                raise SistemaFJError(
                    "Debe seleccionar un tipo de servicio."
                )

            self.servicios.append(servicio)

            self.tabla_servicios.insert(
                "",
                "end",
                values=(
                    tipo,
                    nombre,
                    f"${precio:,.2f}",
                    detalle
                )
            )

            logging.info(
                "Servicio registrado: %s",
                nombre
            )

            messagebox.showinfo(
                "Registro exitoso",
                "El servicio fue registrado correctamente."
            )

            self.nombre_servicio.delete(0, tk.END)
            self.precio_servicio.delete(0, tk.END)
            self.dato_servicio.delete(0, tk.END)

            self.actualizar_servicios_reserva()

        except (SistemaFJError, ValueError) as error:

            logging.exception("Error al registrar servicio")

            messagebox.showerror(
                "Error de validacion",
                str(error)
            )

        except Exception as error:

            logging.exception("Error inesperado al registrar servicio")

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==========================================
    # MODULO DE RESERVAS
    # ==========================================

    def crear_modulo_reservas(self):

        marco = ttk.LabelFrame(
            self.pestana_reservas,
            text="Crear nueva reserva",
            padding=15
        )

        marco.pack(
            fill="x",
            padx=15,
            pady=15
        )

        ttk.Label(
            marco,
            text="Cliente:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=5
        )

        self.seleccion_cliente = ttk.Combobox(
            marco,
            state="readonly"
        )

        self.seleccion_cliente.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=10,
            pady=5
        )

        ttk.Label(
            marco,
            text="Servicio:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=5
        )

        self.seleccion_servicio = ttk.Combobox(
            marco,
            state="readonly"
        )

        self.seleccion_servicio.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=10,
            pady=5
        )

        ttk.Label(
            marco,
            text="Duracion en horas:"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=5
        )

        self.duracion_reserva = tk.Entry(marco)

        self.duracion_reserva.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=10,
            pady=5
        )

        marco.columnconfigure(1, weight=1)

        ttk.Button(
            marco,
            text="Crear reserva",
            command=self.crear_reserva
        ).grid(
            row=3,
            column=0,
            pady=10
        )

        ttk.Button(
            marco,
            text="Confirmar seleccionada",
            command=self.confirmar_reserva
        ).grid(
            row=3,
            column=1,
            pady=10
        )

        ttk.Button(
            marco,
            text="Cancelar seleccionada",
            command=self.cancelar_reserva
        ).grid(
            row=3,
            column=2,
            pady=10
        )

        # Tabla de reservas
        tabla = ttk.LabelFrame(
            self.pestana_reservas,
            text="Reservas registradas",
            padding=10
        )

        tabla.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        columnas = (
            "codigo",
            "cliente",
            "servicio",
            "duracion",
            "estado",
            "costo"
        )

        self.tabla_reservas = ttk.Treeview(
            tabla,
            columns=columnas,
            show="headings"
        )

        titulos = [
            ("codigo", "Codigo"),
            ("cliente", "Cliente"),
            ("servicio", "Servicio"),
            ("duracion", "Horas"),
            ("estado", "Estado"),
            ("costo", "Costo")
        ]

        for columna, titulo in titulos:

            self.tabla_reservas.heading(
                columna,
                text=titulo
            )

            self.tabla_reservas.column(
                columna,
                width=120
            )

        self.tabla_reservas.pack(
            fill="both",
            expand=True
        )

    # ==========================================
    # ACTUALIZAR LISTA DE CLIENTES
    # ==========================================

    def actualizar_clientes_reserva(self):

        self.mapa_clientes = {}

        opciones = []

        for cliente in self.clientes:

            etiqueta = (
                f"{cliente._identificacion} - {cliente._nombre}"
            )

            opciones.append(etiqueta)

            self.mapa_clientes[etiqueta] = cliente

        self.seleccion_cliente["values"] = opciones

    # ==========================================
    # ACTUALIZAR LISTA DE SERVICIOS
    # ==========================================

    def actualizar_servicios_reserva(self):

        self.mapa_servicios = {}

        opciones = []

        for indice, servicio in enumerate(self.servicios):

            etiqueta = f"{indice + 1} - {servicio.nombre}"

            opciones.append(etiqueta)

            self.mapa_servicios[etiqueta] = servicio

        self.seleccion_servicio["values"] = opciones

    # ==========================================
    # CREAR RESERVA
    # ==========================================

    def crear_reserva(self):

        try:

            cliente = self.mapa_clientes.get(
                self.seleccion_cliente.get()
            )

            servicio = self.mapa_servicios.get(
                self.seleccion_servicio.get()
            )

            duracion = float(
                self.duracion_reserva.get()
            )

            codigo = f"RES{len(self.reservas) + 1:03d}"

            reserva = Reserva(
                codigo,
                cliente,
                servicio,
                duracion
            )

            self.reservas[codigo] = reserva

            self.actualizar_tabla_reservas()

            logging.info(
                "Reserva creada: %s",
                codigo
            )

            messagebox.showinfo(
                "Reserva creada",
                f"La reserva {codigo} fue creada en estado Pendiente."
            )

            self.duracion_reserva.delete(0, tk.END)

        except (SistemaFJError, ValueError, TypeError) as error:

            logging.exception("Error al crear reserva")

            messagebox.showerror(
                "Error de reserva",
                str(error)
            )

        except Exception as error:

            logging.exception("Error inesperado al crear reserva")

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==========================================
    # CONFIRMAR RESERVA
    # ==========================================

    def confirmar_reserva(self):

        seleccion = self.tabla_reservas.selection()

        if not seleccion:

            messagebox.showwarning(
                "Atencion",
                "Seleccione una reserva de la tabla."
            )

            return

        codigo = seleccion[0]
        reserva = self.reservas[codigo]

        try:

            costo = reserva.confirmar()

            logging.info(
                "Reserva confirmada: %s",
                codigo
            )

            self.actualizar_tabla_reservas()

            messagebox.showinfo(
                "Reserva confirmada",
                f"Reserva: {codigo}\nCosto total: ${costo:,.2f}"
            )

        except Exception as error:

            logging.exception("Error al confirmar reserva")

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==========================================
    # CANCELAR RESERVA
    # ==========================================

    def cancelar_reserva(self):

        seleccion = self.tabla_reservas.selection()

        if not seleccion:

            messagebox.showwarning(
                "Atencion",
                "Seleccione una reserva de la tabla."
            )

            return

        codigo = seleccion[0]
        reserva = self.reservas[codigo]

        try:

            mensaje = reserva.cancelar()

            logging.info(
                "Reserva cancelada: %s",
                codigo
            )

            self.actualizar_tabla_reservas()

            messagebox.showinfo(
                "Reserva cancelada",
                mensaje
            )

        except Exception as error:

            logging.exception("Error al cancelar reserva")

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==========================================
    # ACTUALIZAR TABLA DE RESERVAS
    # ==========================================

    def actualizar_tabla_reservas(self):

        for elemento in self.tabla_reservas.get_children():

            self.tabla_reservas.delete(elemento)

        for codigo, reserva in self.reservas.items():

            cliente = reserva.cliente
            servicio = reserva.servicio

            self.tabla_reservas.insert(
                "",
                "end",
                iid=codigo,
                values=(
                    codigo,
                    cliente._nombre,
                    servicio.nombre,
                    reserva.duracion,
                    reserva.estado,
                    f"${reserva.costo:,.2f}"
                )
            )


# ==========================================
# INICIAR APLICACION
# ==========================================

def iniciar_aplicacion():

    ventana = tk.Tk()

    AplicacionSoftwareFJ(ventana)

    ventana.mainloop()


if __name__ == "__main__":

    iniciar_aplicacion()
