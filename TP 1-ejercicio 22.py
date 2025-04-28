from collections import deque

# Inicializamos la cola con datos de ejemplo
cola_mcu = deque([
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
])

# a. Determinar el nombre del personaje del superhéroe Capitana Marvel
def personaje_de_capitana_marvel(cola):
    for elemento in cola:
        if elemento["superheroe"] == "Capitana Marvel":
            return elemento["personaje"]
    return "No se encontró a Capitana Marvel en la cola."

# b. Mostrar los nombres de los superhéroes femeninos
def superheroes_femeninos(cola):
    return [elemento["superheroe"] for elemento in cola if elemento["genero"] == "F"]

# c. Mostrar los nombres de los personajes masculinos
def personajes_masculinos(cola):
    return [elemento["personaje"] for elemento in cola if elemento["genero"] == "M"]

# d. Determinar el nombre del superhéroe del personaje Scott Lang
def superheroe_de_scott_lang(cola):
    for elemento in cola:
        if elemento["personaje"] == "Scott Lang":
            return elemento["superheroe"]
    return "No se encontró a Scott Lang en la cola."

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
def datos_con_s(cola):
    return [elemento for elemento in cola if elemento["personaje"].startswith("S") or elemento["superheroe"].startswith("S")]

# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
def carol_danvers_en_cola(cola):
    for elemento in cola:
        if elemento["personaje"] == "Carol Danvers":
            return f"Carol Danvers está en la cola y su superhéroe es {elemento['superheroe']}."
    return "Carol Danvers no se encuentra en la cola."

# Llamadas a las funciones y muestra de resultados
print("a. Nombre del personaje de Capitana Marvel:", personaje_de_capitana_marvel(cola_mcu))
print("b. Superhéroes femeninos:", superheroes_femeninos(cola_mcu))
print("c. Personajes masculinos:", personajes_masculinos(cola_mcu))
print("d. Superhéroe del personaje Scott Lang:", superheroe_de_scott_lang(cola_mcu))
print("e. Datos de superhéroes o personajes cuyos nombres comienzan con 'S':", datos_con_s(cola_mcu))
print("f. Carol Danvers en la cola:", carol_danvers_en_cola(cola_mcu))