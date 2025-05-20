"""
Práctica 4, Ejercicio 2

Daniel Roa
00574499

Fecha de entrega: 26/05/2025

Implemente una clase Playlist que tenga una lista de sus canciones favoritas.
Use el método __len__ para devolver el número de canciones mediante el llamado
len(miLista). Utilice además el método __getitem__ para devolver una can-
ción de la lista de acuerdo al argumento recibido en el método. Finalmente
utilice __setitem__ para establecer una nueva canción en la posición indicada,
ambos pasados como argumentos del método.
"""


class Playlist:
    """Clase Playlist que representa una lista de reproducción de canciones."""

    def __init__(self, canciones: list):
        """Inicializa una lista de reproducción vacía."""
        self.canciones = canciones

    def __str__(self):
        """Función usada para imprimir la lista de reproducción. DEBUGGING."""
        return "Playlist contiene: " + ", ".join(str(c) for c in self.canciones)  # noqa

    def __len__(self):
        """Devuelve el número de canciones en la lista de reproducción."""
        return len(self.canciones)

    def __getitem__(self, index):
        """Devuelve la canción en la posición indicada."""
        return self.canciones[index]

    def __setitem__(self, index, cancion):
        """Establece la canción en la posición indicada."""
        self.canciones[index] = cancion


if "__name__" == "__main__":
    playlist1 = Playlist(
        [
            "Levedad",
            "Molde Perfecto",
            "fatal",
            "Parte del Sol (X Años)",
            "Consecuencias",
        ]
    )
    print(playlist1)
    print(f"La playlist tiene {len(playlist1)} canciones.")
    print(f"La canción en la posición 2 es: {playlist1[2]}")
    print(f"Antes de modificar: {playlist1[3]}")
    playlist1[3] = "¿En Qué Momento?"
    print(f"Después de modificar: {playlist1[3]}")

    playlist2 = Playlist(
        [
            "Splendido",
            "Nunca te amé",
            "Aire Soy",
            "Incendio",
            "Mejor Ya No",
            "Prohibido Besar",
        ]
    )
    print(playlist2)
    print(f"La playlist tiene {len(playlist2)} canciones.")
    print(f"La canción en la posición 3 es: {playlist2[3]}")
    print(f"Antes de modificar: {playlist2[4]}")
    playlist2[4] = "¿En Qué Momento?"
    print(f"Después de modificar: {playlist2[4]}")
