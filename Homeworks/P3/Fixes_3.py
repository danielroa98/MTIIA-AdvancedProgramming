from datetime import date, datetime

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
        """ Regresa la información de una persona. """
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


class Huesped(Persona):
    """
    Clase que representa a un huésped del hotel, hereda de Persona.

    Atributos adicionales:
        habitacion (int): Número de habitación.
        rfc (str): RFC del huésped.
        numero_cuenta (float): Número de cuenta para cargos.
        fecha_ingreso (str): Fecha de ingreso en formato 'YYYY-MM-DD'.
        hospedado_actualmente (bool): True si el huésped está actualmente hospedado.
        servicio_habitacion (dict): Diccionario con {producto: costo}.
        costo_diario_habitacion (float): Costo de la habitación por día.
    """

    def __init__(self,
                 nombre: str,
                 edad: int,
                 habitacion: int,
                 rfc: str,
                 numero_cuenta: float,
                 fecha_ingreso: str, # Formato esperado: 'YYYY-MM-DD'
                 hospedado_actualmente: bool,
                 servicio_habitacion: dict,
                 costo_diario_habitacion: float) -> None:
        super().__init__(nombre, edad)
        self.habitacion = habitacion
        self.rfc = rfc
        self.numero_cuenta = numero_cuenta
        try:
            # Validar el formato de la fecha de ingreso
            datetime.strptime(fecha_ingreso, '%Y-%m-%d')
            self.fecha_ingreso = fecha_ingreso
        except ValueError:
            raise ValueError("El formato de fecha_ingreso debe ser 'YYYY-MM-DD'")
        self.hospedado_actualmente = hospedado_actualmente
        self.servicio_habitacion = servicio_habitacion if servicio_habitacion is not None else {}
        self.costo_diario_habitacion = costo_diario_habitacion

    def mostrar_informacion_basica(self) -> str:
        """ Muestra la información básica del huésped. """
        info_persona = super().informacion  # Accede a la propiedad de la clase Persona
        return f"{info_persona}, Habitación: {self.habitacion}, RFC: {self.rfc}"

    def _calcular_dias_hospedado(self) -> int:
        """
        Calcula el número de días que el huésped ha estado hospedado
        basado en la fecha de ingreso y la fecha actual.
        Si no está hospedado actualmente, calcula los días hasta la fecha de salida (si se tuviera)
        o simplemente los días desde el ingreso si no se maneja fecha de salida explícita.
        Para este ejemplo, si no está hospedado, devolvemos 0 días para el cálculo de saldo pendiente.
        """
        if not self.hospedado_actualmente:
            # Podrías implementar una lógica para calcular días hasta una fecha de salida si la tuvieras
            # Por ahora, si no está hospedado, el costo por días de habitación ya no aumenta.
            # Para calcular un saldo final, se necesitaría la fecha de salida.
            # Vamos a asumir que si no está hospedado, los días a calcular para el costo de habitación son 0
            # o los días que estuvo hasta que dejó de estarlo.
            # Para simplificar, y como el método es "saldo hasta el día de hoy",
            # si ya no está hospedado, no se calculan más días de renta.
            # Si se quisiera calcular el total de una estancia pasada, se necesitaría la fecha_salida.
            # Vamos a interpretar que si `hospedado_actualmente` es False,
            # ya se hizo un checkout y los días ya están definidos por la estancia.
            # El método actual "saldo_hasta_el_dia_de_hoy" se enfocará en huéspedes activos.
            # Opcionalmente, se podría pasar `dias_hospedado` como argumento si la lógica es externa.
            # Para este ejercicio, calcularemos los días solo si está hospedado.
            return 0 # O manejarlo de otra forma si la lógica de negocio es distinta

        fecha_ingreso_dt = datetime.strptime(self.fecha_ingreso, '%Y-%m-%d').date()
        hoy = date.today()
        diferencia = hoy - fecha_ingreso_dt
        # Se cuenta el día de ingreso como el primer día completo
        return diferencia.days + 1 if diferencia.days >= 0 else 0


    def saldo_hasta_el_dia_de_hoy(self) -> float:
        """
        Calcula el saldo hasta el día de hoy.
        Considera el costo de la renta de la habitación por los días que lleva
        hospedado y los gastos del servicio a la habitación.
        """
        dias_hospedado = self._calcular_dias_hospedado()

        if dias_hospedado < 0: # Esta validación ya no sería estrictamente necesaria si _calcular_dias_hospedado maneja fechas futuras
            # Sin embargo, la dejamos como salvaguarda por si la lógica de cálculo de días cambia.
            # raise ValueError("Los días hospedado calculados son negativos, verificar fechas.")
            # En lugar de un error, podríamos asumir 0 para evitar que el programa falle.
            dias_hospedado = 0

        costo_total_habitacion = dias_hospedado * self.costo_diario_habitacion

        costo_total_servicios = 0.0
        if self.servicio_habitacion: # Verificar si el diccionario no está vacío
            for costo in self.servicio_habitacion.values():
                costo_total_servicios += costo

        saldo_total = costo_total_habitacion + costo_total_servicios
        return saldo_total

    def agregar_servicio(self, producto: str, costo: float) -> None:
        """Agrega un nuevo servicio o actualiza el costo de uno existente."""
        if costo < 0:
            raise ValueError("El costo del servicio no puede ser negativo.")
        self.servicio_habitacion[producto] = costo
        print(f"Servicio '{producto}' agregado/actualizado con costo: ${costo:.2f}")

# --- Ejemplo de Uso ---
if __name__ == "__main__":
    print("Bienvenido al Sistema de Registro de Huéspedes del Hotel")

    # Crear una instancia de Persona
    persona1 = Persona("Juan Pérez", 30)
    print("\nInformación de Persona:")
    print(persona1.informacion) # Usando la propiedad

    # Crear una instancia de Huesped
    # Para calcular los días, usaremos una fecha de ingreso anterior
    fecha_actual = date.today()
    # Supongamos que ingresó hace 5 días para el ejemplo
    # Para una prueba realista, puedes poner una fecha específica como '2024-03-01'

    # Vamos a simular que ingresó hace 2 días.
    # Para que funcione con la fecha actual, necesitarías que la fecha_ingreso sea en el pasado.
    # Por ejemplo, si hoy es 2024-03-10, una fecha_ingreso válida sería '2024-03-08'.

    # Obtener la fecha de hace 2 días para el ejemplo
    from datetime import timedelta
    fecha_ingreso_ejemplo = (fecha_actual - timedelta(days=2)).strftime('%Y-%m-%d')


    try:
        huesped1 = Huesped(
            nombre="Ana Gómez",
            edad=28,
            habitacion=101,
            rfc="GOMA280202ABC",
            numero_cuenta=12345.67,
            fecha_ingreso=fecha_ingreso_ejemplo, # Ejemplo: '2024-03-08' (ajusta según la fecha actual)
            hospedado_actualmente=True,
            servicio_habitacion={"Cena": 250.00, "Lavandería": 120.50},
            costo_diario_habitacion=1500.00
        )

        print("\nInformación de Huésped:")
        print(huesped1.mostrar_informacion_basica())

        print(f"Fecha de ingreso del huésped: {huesped1.fecha_ingreso}")
        dias_calculados = huesped1._calcular_dias_hospedado()
        print(f"Días hospedado calculados: {dias_calculados}") # Debería ser 3 (día de ingreso + 2 días más)

        print(f"Saldo actual del huésped: ${huesped1.saldo_hasta_el_dia_de_hoy():.2f}")

        # Agregar un nuevo servicio
        print("\nAgregando nuevo servicio...")
        huesped1.agregar_servicio("Desayuno Americano", 180.00)
        huesped1.agregar_servicio("Mini Bar: Refresco", 45.00)

        print(f"Servicios actualizados: {huesped1.servicio_habitacion}")
        print(f"Nuevo saldo actual del huésped: ${huesped1.saldo_hasta_el_dia_de_hoy():.2f}")

        # Ejemplo de huésped que ya no está hospedado
        fecha_ingreso_pasada = (fecha_actual - timedelta(days=10)).strftime('%Y-%m-%d')
        huesped2 = Huesped(
            nombre="Carlos López",
            edad=45,
            habitacion=205,
            rfc="LOLC450505XYZ",
            numero_cuenta=98765.43,
            fecha_ingreso=fecha_ingreso_pasada, # Ingresó hace 10 días
            hospedado_actualmente=False, # Ya no está hospedado
            servicio_habitacion={"Almuerzo": 200.00},
            costo_diario_habitacion=1200.00
        )
        print("\nInformación de Huésped (no hospedado actualmente):")
        print(huesped2.mostrar_informacion_basica())
        # Para este caso, _calcular_dias_hospedado() devuelve 0 según la lógica actual,
        # por lo que el costo de habitación sería 0 en el saldo "hasta hoy".
        # Si se quisiera el saldo final de su estancia, la lógica debería ser diferente
        # y probablemente usar una fecha de salida.
        dias_h2 = huesped2._calcular_dias_hospedado()
        print(f"Días calculados para costo de habitación (hospedado_actualmente=False): {dias_h2}")
        print(f"Saldo (considerando solo servicios si ya no está hospedado y días=0): ${huesped2.saldo_hasta_el_dia_de_hoy():.2f}")


        # Ejemplo de error en fecha
        # print("\nProbando error de formato de fecha:")
        # huesped_error = Huesped(
        #     "Error Test", 20, 303, "ERRT200101QWE", 100.0,
        #     "20-12-2023", True, {}, 1000.00
        # )

    except ValueError as e:
        print(f"\nError al crear el huésped: {e}")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")