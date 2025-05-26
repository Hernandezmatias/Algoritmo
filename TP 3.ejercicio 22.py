from collections import deque

# Ejemplo de cola de personajes MCU
cola_mcu = deque([
    {'personaje': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'},
    {'personaje': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'},
    {'personaje': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'},
    {'personaje': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'},
    {'personaje': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'},
    {'personaje': 'Sam Wilson', 'superheroe': 'Falcon', 'genero': 'M'},
    {'personaje': 'Shuri', 'superheroe': 'Shuri', 'genero': 'F'},
])

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
def personaje_de_capitana_marvel(cola):
    for p in cola:
        if p['superheroe'] == 'Capitana Marvel':
            return p['personaje']
    return None

# b. Mostrar los nombres de los superhéroes femeninos
def superheroes_femeninos(cola):
    print("Superhéroes femeninos:")
    for p in cola:
        if p['genero'] == 'F':
            print(p['superheroe'])

# c. Mostrar los nombres de los personajes masculinos
def personajes_masculinos(cola):
    print("Personajes masculinos:")
    for p in cola:
        if p['genero'] == 'M':
            print(p['personaje'])

# d. Determinar el nombre del superhéroe del personaje Scott Lang
def superheroe_de_scott_lang(cola):
    for p in cola:
        if p['personaje'] == 'Scott Lang':
            return p['superheroe']
    return None

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con S
def nombres_con_S(cola):
    print("Datos de superhéroes/personajes que comienzan con S:")
    for p in cola:
        if p['superheroe'].startswith('S') or p['personaje'].startswith('S'):
            print(p)

# f. Determinar si Carol Danvers está en la cola e indicar su nombre de superhéroe
def buscar_carol_danvers(cola):
    for p in cola:
        if p['personaje'] == 'Carol Danvers':
            print(f"Carol Danvers está en la cola. Su nombre de superhéroe es: {p['superheroe']}")
            return
    print("Carol Danvers no está en la cola.")

# Ejecución de funciones:
print("a. Nombre del personaje de Capitana Marvel:")
print(personaje_de_capitana_marvel(cola_mcu))
print("\nb. Superhéroes femeninos:")
superheroes_femeninos(cola_mcu)
print("\nc. Personajes masculinos:")
personajes_masculinos(cola_mcu)
print("\nd. Nombre del superhéroe de Scott Lang:")
print(superheroe_de_scott_lang(cola_mcu))
print("\ne. Datos cuyos nombres inician con S:")
nombres_con_S(cola_mcu)
print("\nf. Búsqueda de Carol Danvers:")
buscar_carol_danvers(cola_mcu)
