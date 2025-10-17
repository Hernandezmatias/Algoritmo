class Nodo:
    def __init__(self, nombre, derrotado_por=None, descripcion="", capturada=None):
        self.nombre = nombre
        self.derrotado_por = derrotado_por if derrotado_por else []
        self.descripcion = descripcion
        self.capturada = capturada  # nombre del héroe o dios que la capturó
        self.izq = None
        self.der = None

class ArbolABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, derrotado_por=None, descripcion="", capturada=None):
        def _insertar(nodo, nombre, derrotado_por, descripcion, capturada):
            if not nodo:
                return Nodo(nombre, derrotado_por, descripcion, capturada)
            if nombre < nodo.nombre:
                nodo.izq = _insertar(nodo.izq, nombre, derrotado_por, descripcion, capturada)
            else:
                nodo.der = _insertar(nodo.der, nombre, derrotado_por, descripcion, capturada)
            return nodo
        self.raiz = _insertar(self.raiz, nombre, derrotado_por, descripcion, capturada)

    def inorden(self):
        res = []
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izq)
                res.append(nodo)
                _inorden(nodo.der)
        _inorden(self.raiz)
        return res

    def buscar(self, nombre):
        def _buscar(nodo, nombre):
            if not nodo:
                return None
            if nodo.nombre.lower() == nombre.lower():
                return nodo
            if nombre < nodo.nombre:
                return _buscar(nodo.izq, nombre)
            else:
                return _buscar(nodo.der, nombre)
        return _buscar(self.raiz, nombre)

    def buscar_coincidencia(self, texto):
        res = []
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izq)
                if texto.lower() in nodo.nombre.lower():
                    res.append(nodo)
                _inorden(nodo.der)
        _inorden(self.raiz)
        return res

    def eliminar(self, nombre):
        def _eliminar(nodo, nombre):
            if not nodo:
                return None
            if nombre < nodo.nombre:
                nodo.izq = _eliminar(nodo.izq, nombre)
            elif nombre > nodo.nombre:
                nodo.der = _eliminar(nodo.der, nombre)
            else:
                if not nodo.izq and not nodo.der:
                    return None
                if not nodo.izq:
                    return nodo.der
                if not nodo.der:
                    return nodo.izq
                # Nodo con dos hijos: buscar sucesor inorden
                sucesor = nodo.der
                while sucesor.izq:
                    sucesor = sucesor.izq
                nodo.nombre, nodo.derrotado_por, nodo.descripcion, nodo.capturada = \
                    sucesor.nombre, sucesor.derrotado_por, sucesor.descripcion, sucesor.capturada
                nodo.der = _eliminar(nodo.der, sucesor.nombre)
            return nodo
        self.raiz = _eliminar(self.raiz, nombre)

    def por_nivel(self):
        res = []
        if not self.raiz:
            return res
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            res.append(actual)
            if actual.izq:
                cola.append(actual.izq)
            if actual.der:
                cola.append(actual.der)
        return res

# --- Datos de la tabla ---
tabla = [
    # nombre, derrotado_por (lista), descripcion (vacío por ahora), capturada
    ("Ceto", [], "", None),
    ("Tifón", ["Zeus"], "", None),
    ("Equidna", ["Argos Panoptes"], "", None),
    ("Dino", [], "", None),
    ("Pefredo", [], "", None),
    ("Enio", [], "", None),
    ("Escila", [], "", None),
    ("Caribdis", [], "", None),
    ("Euríale", [], "", None),
    ("Esteno", [], "", None),
    ("Medusa", ["Perseo"], "", None),
    ("Ladón", ["Heracles"], "", None),
    ("Águila del Cáucaso", [], "", None),
    ("Quimera", ["Belerofonte"], "", None),
    ("Hidra de Lerna", ["Heracles"], "", None),
    ("León de Nemea", ["Heracles"], "", None),
    ("Esfinge", ["Edipo"], "", None),
    ("Dragón de la Cólquida", [], "", None),
    ("Cerbero", [], "", None),
    ("Cerda de Cromión", ["Teseo"], "", None),
    ("Ortro", ["Heracles"], "", None),
    ("Toro de Creta", ["Teseo"], "", None),
    ("Jabalí de Calidón", ["Atalanta"], "", None),
    ("Carcinos", [], "", None),
    ("Gerión", ["Heracles"], "", None),
    ("Minotauro de Creta", ["Teseo"], "", None),
    ("Harpías", [], "", None),
    ("Aves del Estínfalo", [], "", None),
    ("Sirenas", [], "", None),
    ("Pitón", ["Apolo"], "", None),
    ("Cierva de Cerinea", [], "", None),
    ("Jabalí de Erimanto", [], "", None),
    ("Talos", ["Medea"], "", None),
    ("Argos Panoptes", [], "", None),
    ("Cloto", [], "", None),
    ("Láquesis", [], "", None),
    ("Átropos", [], "", None),
    ("Basilisco", [], "", None),
]

arbol = ArbolABB()
for nombre, derrotado_por, descripcion, capturada in tabla:
    arbol.insertar(nombre, derrotado_por, descripcion, capturada)

# Inciso a: Inorden criaturas y quienes la derrotaron
print("a. Listado inorden de criaturas y sus vencedores:")
for nodo in arbol.inorden():
    print(f"{nodo.nombre}: Derrotado por {', '.join(nodo.derrotado_por) if nodo.derrotado_por else 'Nadie'}")

# Inciso b: Cargar descripción (ejemplo)
arbol.buscar("Talos").descripcion = "Gigante de bronce que protegía Creta."

# Inciso c: Mostrar toda la información de Talos
talos = arbol.buscar("Talos")
if talos:
    print(f"c. Talos info: {talos.nombre}, Derrotado por: {talos.derrotado_por}, Desc: {talos.descripcion}, Capturada: {talos.capturada}")

# Inciso d: 3 héroes/dioses que más criaturas derrotaron
from collections import Counter
cont = Counter()
for nodo in arbol.inorden():
    for heroe in nodo.derrotado_por:
        cont[heroe] += 1
print("d. Top 3 héroes/dioses por criaturas derrotadas:")
for heroe, cantidad in cont.most_common(3):
    print(f"{heroe}: {cantidad}")

# Inciso e: Criaturas derrotadas por Heracles
print("e. Criaturas derrotadas por Heracles:")
for nodo in arbol.inorden():
    if "Heracles" in nodo.derrotado_por:
        print(nodo.nombre)

# Inciso f: Criaturas no derrotadas
print("f. Criaturas no derrotadas:")
for nodo in arbol.inorden():
    if not nodo.derrotado_por:
        print(nodo.nombre)

# Inciso g: Campo capturada ya implementado

# Inciso h: Modificar capturada por Heracles en ciertas criaturas
for criatura in ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]:
    nodo = arbol.buscar(criatura)
    if nodo:
        nodo.capturada = "Heracles"

# Inciso i: Búsqueda por coincidencia
print("i. Buscar criaturas con 'Cer':")
for nodo in arbol.buscar_coincidencia("Cer"):
    print(nodo.nombre)

# Inciso j: Eliminar Basilisco y Sirenas
arbol.eliminar("Basilisco")
arbol.eliminar("Sirenas")

# Inciso k: Modificar Aves del Estínfalo (Heracles derrotó varias)
aves = arbol.buscar("Aves del Estínfalo")
if aves:
    aves.derrotado_por.append("Heracles")
    aves.descripcion += " Heracles derrotó a varias."

# Inciso l: Cambiar nombre de Ladón a Dragón Ladón
ladon = arbol.buscar("Ladón")
if ladon:
    # Guardar datos de Ladón, eliminarlo, e insertar con nuevo nombre
    derrotado_por, descripcion, capturada = ladon.derrotado_por, ladon.descripcion, ladon.capturada
    arbol.eliminar("Ladón")
    arbol.insertar("Dragón Ladón", derrotado_por, descripcion, capturada)

# Inciso m: Listado por nivel
print("m. Listado por nivel:")
for nodo in arbol.por_nivel():
    print(nodo.nombre)

# Inciso n: Criaturas capturadas por Heracles
print("n. Criaturas capturadas por Heracles:")
for nodo in arbol.inorden():
    if nodo.capturada == "Heracles":
        print(nodo.nombre)