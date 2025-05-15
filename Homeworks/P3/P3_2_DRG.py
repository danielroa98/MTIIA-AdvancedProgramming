"""
Práctica 3, Ejercicio 2

Daniel Roa
00574499

Desarrollar un mini-sistema para el registro de huespedes de un hotel.
Para ello desarrolle una clase Persona que tenga los atributos nombre
y edad. Debe tener una propiedad que muestre la información de la persona.
Desarrolle además otra clase llamada Huesped que se construya a partir de
la clase Persona de manera que herede sus propiedades y métodos.
La clase Huesped debe tener además sus propiedades adicionales para la
información requerida:
• Habitación (int)
• RFC (string)
• Número de cuenta (float)
• Fecha de ingreso (string)
• Hospedado actualmente (booleano)
• Servicio a la habitación (Un diccionario donde la llave es el producto y
    el valor el costo del producto)

Además, la clase debe tener un par de métodos:
• Mostrar información básica del huesped
• Saldo hasta el día de hoy. Se debe considerar el costo de
    la renta de la habitación por los días que lleva hospedado y
    los gastos del servicio a la habitación (almacenados en el diccionario).
"""

from datetime import datetime, date, timedelta


class Persona:
    """
    Clase que representa a una persona.

    Atributos:
        nombre (str): Nombre de la persona.
        edad (int): Edad de la persona.
    """

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    @property
    def informacion(self) -> str:
        """str: Propiedad que devuelve la información de la persona (nombre y edad)."""
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


class Huesped(Persona):
    """
    Clase que representa a un huésped del hotel, hereda de Persona.

    Atributos:
        nombre (str): Nombre del huésped (heredado).
        edad (int): Edad del huésped (heredado).
        habitacion (int): Número de habitación.
        rfc (str): RFC del huésped.
        numero_cuenta (float): Número de cuenta para cargos.
        fecha_ingreso (str): Fecha de ingreso en formato 'YYYY-MM-DD'.
        hospedado_actualmente (bool): True si el huésped está actualmente hospedado.
        servicio_habitacion (dict): Diccionario con {producto: costo} de servicios.
        costo_diario_habitacion (float): Costo de la habitación por día.
    """

    def __init__(
        self,
        nombre: str,
        edad: int,
        habitacion: int,
        rfc: str,
        numero_cuenta: float,
        fecha_ingreso: str,
        hospedado_actualmente: bool,
        servicio_habitacion: dict,
        costo_diario_habitacion: float,
    ) -> None:
        """
        Inicializa una instancia de Huesped.

        Args:
            nombre: Nombre del huésped.
            edad: Edad del huésped.
            habitacion: Número de habitación.
            rfc: RFC del huésped.
            numero_cuenta: Número de cuenta para cargos.
            fecha_ingreso: Fecha de ingreso en formato 'YYYY-MM-DD'.
            hospedado_actualmente: Estado de hospedaje actual.
            servicio_habitacion: Diccionario de servicios y sus costos.
            costo_diario_habitacion: Costo diario de la habitación.

        Raises:
            ValueError: Si el formato de fecha_ingreso no es 'YYYY-MM-DD'.
        """
        super().__init__(nombre, edad)
        self.habitacion = habitacion
        self.rfc = rfc
        self.numero_cuenta = numero_cuenta
        try:
            datetime.strptime(fecha_ingreso, "%Y-%m-%d")
            self.fecha_ingreso = fecha_ingreso
        except ValueError:
            raise ValueError("El formato de fecha_ingreso debe ser 'YYYY-MM-DD'")
        self.hospedado_actualmente = hospedado_actualmente
        self.servicio_habitacion = (
            servicio_habitacion if servicio_habitacion is not None else {}
        )
        self.costo_diario_habitacion = costo_diario_habitacion

    def mostrar_info_huesped(self) -> str:
        """
        Devuelve una cadena con la información básica del huésped.

        Returns:
            str: Información básica del huésped (nombre, edad, habitación, RFC).
        """
        info_persona = super().informacion
        return f"{info_persona}, Habitación: {self.habitacion}, RFC: {self.rfc}"

    def _calcular_dias_hospedado(self) -> int:
        """
        Calcula el número de días que el huésped ha estado hospedado.

        El cálculo se basa en la fecha de ingreso y la fecha actual. El día de
        ingreso se cuenta como el primer día completo. Si el huésped no está
        actualmente hospedado o la fecha de ingreso es futura, devuelve 0.

        Returns:
            int: Número de días hospedado.
        """
        if not self.hospedado_actualmente:
            return 0

        try:
            fecha_ingreso_dt = datetime.strptime(self.fecha_ingreso, "%Y-%m-%d").date()
        except ValueError:
            return 0

        hoy = date.today()

        if fecha_ingreso_dt > hoy:
            return 0

        diferencia = hoy - fecha_ingreso_dt
        return diferencia.days + 1

    def saldo_actual(self) -> float:
        """
        Calcula el saldo total del huésped hasta el día de hoy.

        El saldo considera el costo de la renta de la habitación por los días
        hospedado y los gastos acumulados del servicio a la habitación.

        Returns:
            float: El saldo total calculado.
        """
        dias_hospedado = self._calcular_dias_hospedado()

        if (
            dias_hospedado < 0
        ):  # Salvaguarda, aunque _calcular_dias_hospedado debería prevenirlo.
            dias_hospedado = 0

        costo_total_habitacion = dias_hospedado * self.costo_diario_habitacion

        costo_total_servicios = 0.0
        if self.servicio_habitacion:
            for costo in self.servicio_habitacion.values():
                costo_total_servicios += costo

        saldo_total = costo_total_habitacion + costo_total_servicios
        return saldo_total

    def agregar_servicio(self, producto: str, costo: float) -> None:
        """
        Agrega un nuevo servicio a la habitación o actualiza el costo de uno existente.

        Args:
            producto: El nombre del producto o servicio.
            costo: El costo del producto o servicio.

        Raises:
            ValueError: Si el costo del servicio es negativo.
        """
        if costo < 0:
            raise ValueError("El costo del servicio no puede ser negativo.")
        self.servicio_habitacion[producto] = costo
        print(f"Servicio '{producto}' agregado/actualizado con costo: ${costo:.2f}")


if __name__ == "__main__":
    print("Bienvenido al Sistema de Registro de Huéspedes del Hotel")
    print(f"La fecha de hoy es: {date.today().strftime('%Y-%m-%d')}")

    fecha_ingreso_daniel = (date.today() - timedelta(days=1)).strftime(
        "%Y-%m-%d"
    )

    try:
        h1 = Huesped(
            nombre="Daniel Roa",
            edad=27,
            habitacion=1001,
            rfc="ROAD270101XYZ",
            numero_cuenta=1500.0,
            fecha_ingreso=fecha_ingreso_daniel,
            hospedado_actualmente=True,
            servicio_habitacion={"Pizza": 200.0, "Refresco": 50.0},
            costo_diario_habitacion=500.0,
        )
        print("\n--- Información Huésped Daniel ---")
        print(h1.mostrar_info_huesped())
        h1_dias = h1._calcular_dias_hospedado()
        print(f"Días hospedado (Daniel): {h1_dias}")
        print(f"Saldo actual (Daniel): ${h1.saldo_actual():.2f}")

        h1.agregar_servicio("Lavandería Express", 150.00)
        print(
            f"Servicios (Daniel) después de agregar: {h1.servicio_habitacion}"
        )
        print(f"Nuevo saldo (Daniel): ${h1.saldo_actual():.2f}")

    except ValueError as e:
        print(f"\nError al crear el huésped: {e}")

    # --- Ejemplo 2: Huésped Ana Gómez (ingresó hace 5 días) ---
    fecha_ingreso_ana = (date.today() - timedelta(days=4)).strftime("%Y-%m-%d")

    try:
        h2 = Huesped(
            nombre="Ana Gómez",
            edad=28,
            habitacion=101,
            rfc="GOMA280202ABC",
            numero_cuenta=12345.67,
            fecha_ingreso=fecha_ingreso_ana,
            hospedado_actualmente=True,
            servicio_habitacion={"Cena": 250.00, "Lavandería": 120.50},
            costo_diario_habitacion=1500.00,
        )

        print("\n--- Información Huésped Ana ---")
        print(h2.mostrar_info_huesped())
        h2_dias = h2._calcular_dias_hospedado()
        print(f"Días hospedado (Ana): {h2_dias}")
        print(f"Saldo actual (Ana): ${h2.saldo_actual():.2f}")

        h2.agregar_servicio("Desayuno Americano", 180.00)
        h2.agregar_servicio("Mini Bar: Refresco", 45.00)

        print(f"Servicios (Ana) actualizados: {h2.servicio_habitacion}")
        print(f"Nuevo saldo (Ana): ${h2.saldo_actual():.2f}")

    except ValueError as e:
        print(f"\nError al crear el huésped Ana: {e}")

    # --- Ejemplo 3: Huésped Carlos López (no hospedado actualmente) ---
    fecha_ingreso_carlos = (date.today() - timedelta(days=10)).strftime("%Y-%m-%d")

    try:
        h3 = Huesped(
            nombre="Carlos López",
            edad=45,
            habitacion=205,
            rfc="LOLC450505XYZ",
            numero_cuenta=98765.43,
            fecha_ingreso=fecha_ingreso_carlos,
            hospedado_actualmente=False,
            servicio_habitacion={"Almuerzo": 200.00, "Llamadas Telefónicas": 75.50},
            costo_diario_habitacion=1200.00,
        )
        print("\n--- Información Huésped Carlos (No hospedado) ---")
        print(h3.mostrar_info_huesped())
        h3_dias = h3._calcular_dias_hospedado()
        print(
            f"Días calculados para costo de habitación actual (Carlos): {h3_dias}"
        )
        print(
            f"Saldo pendiente (Carlos, solo servicios si días=0): ${h3.saldo_actual():.2f}"
        )

    except ValueError as e:
        print(f"\nError al crear el huésped Carlos: {e}")

    # --- Ejemplo 4: Intento de crear huésped con fecha futura ---
    fecha_futura = (date.today() + timedelta(days=5)).strftime("%Y-%m-%d")
    try:
        h4 = Huesped(
            nombre="Viajero Del Tiempo",
            edad=100,
            habitacion=777,
            rfc="VIDT1000101TTT",
            numero_cuenta=10000.00,
            fecha_ingreso=fecha_futura,
            hospedado_actualmente=True,
            servicio_habitacion={},
            costo_diario_habitacion=2000.00,
        )
        print("\n--- Información Huésped Futuro ---")
        print(h4.mostrar_info_huesped())
        h4_dias = h4._calcular_dias_hospedado()
        print(f"Días hospedado (Viajero Del Tiempo): {h4_dias}")
        print(
            f"Saldo actual (Viajero Del Tiempo): ${h4.saldo_actual():.2f}"
        )

    except ValueError as e:
        print(f"\nError al crear el huésped futuro: {e}")

    # --- Ejemplo 5: Error en formato de fecha ---
    print("\n--- Probando error de formato de fecha ---")
    try:
        huesped_error_fecha = Huesped(
            "Error Test",
            20,
            303,
            "ERRT200101QWE",
            100.0,
            "20-12-2023",
            True,
            {},
            1000.00,
        )
    except ValueError as e:
        print(f"Error capturado correctamente: {e}")
