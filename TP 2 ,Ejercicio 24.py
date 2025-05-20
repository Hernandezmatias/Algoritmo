class PersonajeMCU:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

    def __repr__(self):
        return f"{self.nombre} ({self.cantidad_peliculas} películas)"

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

    def ver_tope(self):
        return self.items[-1] if not self.esta_vacia() else None

    def __iter__(self):
        # Itera de cima a base
        return reversed(self.items)

    def __len__(self):
        return len(self.items)

# Ejemplo de carga de personajes
pila_personajes = Pila()
pila_personajes.apilar(PersonajeMCU("Iron Man", 10))
pila_personajes.apilar(PersonajeMCU("Captain America", 9))
pila_personajes.apilar(PersonajeMCU("Black Widow", 7))
pila_personajes.apilar(PersonajeMCU("Rocket Raccoon", 4))
pila_personajes.apilar(PersonajeMCU("Groot", 5))
pila_personajes.apilar(PersonajeMCU("Doctor Strange", 4))
pila_personajes.apilar(PersonajeMCU("Gamora", 5))
pila_personajes.apilar(PersonajeMCU("Drax", 5))
pila_personajes.apilar(PersonajeMCU("Captain Marvel", 3))
pila_personajes.apilar(PersonajeMCU("Hulk", 7))

# a. Posición de Rocket Raccoon y Groot (cima = 1)
def posicion_personaje(pila, nombre_buscado):
    for idx, personaje in enumerate(pila, 1):  # cima es posición 1
        if personaje.nombre == nombre_buscado:
            return idx
    return -1  # No encontrado

print("a. Posiciones de Rocket Raccoon y Groot (cima = 1):")
pos_rocket = posicion_personaje(pila_personajes, "Rocket Raccoon")
pos_groot = posicion_personaje(pila_personajes, "Groot")
print(f"Rocket Raccoon está en la posición: {pos_rocket}")
print(f"Groot está en la posición: {pos_groot}")

# b. Personajes en más de 5 películas
print("\nb. Personajes en más de 5 películas:")
for personaje in pila_personajes:
    if personaje.cantidad_peliculas > 5:
        print(f"{personaje.nombre}: {personaje.cantidad_peliculas} películas")

# c. ¿Cuántas películas participó Black Widow?
print("\nc. Cantidad de películas de Black Widow:")
for personaje in pila_personajes:
    if personaje.nombre == "Black Widow":
        print(f"Black Widow participó en {personaje.cantidad_peliculas} películas")
        break
else:
    print("Black Widow no está en la pila.")

# d. Personajes cuyos nombres empiezan con C, D y G
print("\nd. Personajes cuyos nombres empiezan con C, D y G:")
for personaje in pila_personajes:
    if personaje.nombre.startswith(("C", "D", "G")):
        print(personaje.nombre)
