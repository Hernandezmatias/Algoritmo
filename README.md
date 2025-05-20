class TrajeIronMan:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __repr__(self):
        return f"{self.modelo} ({self.pelicula}, {self.estado})"

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        # Permite iterar sobre la pila sin modificarla
        return reversed(self.items)

# Cargar ejemplos iniciales en la pila
pila_trajes = Pila()
pila_trajes.apilar(TrajeIronMan("Mark III", "Iron Man", "Dañado"))
pila_trajes.apilar(TrajeIronMan("Mark V", "Iron Man 2", "Destruido"))
pila_trajes.apilar(TrajeIronMan("Mark XLIV", "Avengers: Age of Ultron", "Dañado"))
pila_trajes.apilar(TrajeIronMan("Mark XLVI", "Captain America: Civil War", "Impecable"))
pila_trajes.apilar(TrajeIronMan("Mark XLVII", "Spider-Man: Homecoming", "Impecable"))
pila_trajes.apilar(TrajeIronMan("Mark L", "Avengers: Infinity War", "Destruido"))
pila_trajes.apilar(TrajeIronMan("Mark LXXXV", "Avengers: Endgame", "Impecable"))

# a. ¿Mark XLIV usado en alguna película? Mostrar nombres de películas.
print("a. ¿Mark XLIV (Hulkbuster) fue utilizado en alguna película?")
peliculas_hulkbuster = set()
for traje in pila_trajes:
    if traje.modelo == "Mark XLIV":
        peliculas_hulkbuster.add(traje.pelicula)
if peliculas_hulkbuster:
    print(f"Sí, en las películas: {', '.join(peliculas_hulkbuster)}")
else:
    print("No fue utilizado en ninguna película.")

# b. Mostrar modelos que quedaron dañados, sin perder información de la pila.
print("\nb. Modelos que quedaron dañados:")
for traje in pila_trajes:
    if traje.estado == "Dañado":
        print(f"{traje.modelo} ({traje.pelicula})")

# c. Eliminar modelos destruidos mostrando su nombre
print("\nc. Eliminando modelos destruidos:")
pila_aux = Pila()
while not pila_trajes.esta_vacia():
    traje = pila_trajes.desapilar()
    if traje.estado == "Destruido":
        print(f"Eliminado: {traje.modelo} ({traje.pelicula})")
    else:
        pila_aux.apilar(traje)
# Volver a dejar la pila original como estaba (sin los destruidos)
while not pila_aux.esta_vacia():
    pila_trajes.apilar(pila_aux.desapilar())

# d. Un modelo puede usarse en más de una película y viceversa.
# (Ya se cumple por la estructura y la carga de datos por separado)

# e. Agregar Mark LXXXV, sin repetir modelo en la misma película
nuevo_traje = TrajeIronMan("Mark LXXXV", "Avengers: Endgame", "Impecable")
repetido = any((traje.modelo == nuevo_traje.modelo and traje.pelicula == nuevo_traje.pelicula) for traje in pila_trajes)
if not repetido:
    pila_trajes.apilar(nuevo_traje)
    print("\ne. Mark LXXXV agregado a la pila.")
else:
    print("\ne. Mark LXXXV ya estaba en la pila para esa película, no se agregó.")

# f. Mostrar nombres de trajes usados en “Spider-Man: Homecoming” y “Capitan America: Civil War”
print("\nf. Trajes utilizados en Spider-Man: Homecoming y Captain America: Civil War:")
peliculas_buscar = ["Spider-Man: Homecoming", "Captain America: Civil War", "Capitan America: Civil War"]
for traje in pila_trajes:
    if traje.pelicula in peliculas_buscar:
        print(f"{traje.modelo} ({traje.pelicula})")
