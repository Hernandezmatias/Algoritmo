class Nodo:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe  # True para héroe, False para villano
        self.izq = None
        self.der = None

class ArbolABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        def _insertar(nodo, nombre, es_heroe):
            if not nodo:
                return Nodo(nombre, es_heroe)
            if nombre < nodo.nombre:
                nodo.izq = _insertar(nodo.izq, nombre, es_heroe)
            else:
                nodo.der = _insertar(nodo.der, nombre, es_heroe)
            return nodo
        self.raiz = _insertar(self.raiz, nombre, es_heroe)

    def barrido_inorden(self, filtro=None, descendente=False):
        res = []
        def _inorden(nodo):
            if nodo:
                if not descendente:
                    _inorden(nodo.izq)
                if not filtro or filtro(nodo):
                    res.append(nodo.nombre)
                if descendente:
                    _inorden(nodo.izq)
                    _inorden(nodo.der)
                else:
                    _inorden(nodo.der)
        _inorden(self.raiz)
        return sorted(res, reverse=descendente)

    def barrido_inorden_obj(self, filtro=None):
        res = []
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izq)
                if not filtro or filtro(nodo):
                    res.append(nodo)
                _inorden(nodo.der)
        _inorden(self.raiz)
        return res

    def contar_heroes(self):
        def _contar(nodo):
            if not nodo:
                return 0
            return _contar(nodo.izq) + int(nodo.es_heroe) + _contar(nodo.der)
        return _contar(self.raiz)

    def buscar_proximidad(self, nombre_busqueda, umbral=3):
        # Busca por distancia de Levenshtein menor a umbral
        def levenshtein(a, b):
            if not a: return len(b)
            if not b: return len(a)
            if a[0] == b[0]:
                return levenshtein(a[1:], b[1:])
            return 1 + min(levenshtein(a[1:], b), levenshtein(a, b[1:]), levenshtein(a[1:], b[1:]))
        encontrados = []
        def _buscar(nodo):
            if nodo:
                if levenshtein(nodo.nombre.lower(), nombre_busqueda.lower()) <= umbral:
                    encontrados.append(nodo)
                _buscar(nodo.izq)
                _buscar(nodo.der)
        _buscar(self.raiz)
        return encontrados

    def contar_nodos(self):
        def _contar(nodo):
            if not nodo:
                return 0
            return 1 + _contar(nodo.izq) + _contar(nodo.der)
        return _contar(self.raiz)

# --- Datos de ejemplo ---
arbol = ArbolABB()
datos = [
    ("Iron Man", True),
    ("Captain America", True),
    ("Captain Marvel", True),
    ("Thor", True),
    ("Loki", False),
    ("Thanos", False),
    ("Ultron", False),
    ("Doctor Strenge", True),  # mal escrito a propósito
    ("Hulk", True),
    ("Red Skull", False),
    ("Hawkeye", True),
    ("Wanda", True),
    ("Vision", True),
    ("Crossbones", False),
    ("Coulson", True)
]
for nombre, tipo in datos:
    arbol.insertar(nombre, tipo)

# b. listar villanos ordenados alfabéticamente
villanos = arbol.barrido_inorden(lambda n: not n.es_heroe)
print("Villanos:", villanos)

# c. superhéroes que empiezan con C
heroes_con_C = arbol.barrido_inorden(lambda n: n.es_heroe and n.nombre.startswith('C'))
print("Superhéroes que empiezan con C:", heroes_con_C)

# d. cuántos superhéroes hay
num_heroes = arbol.contar_heroes()
print("Cantidad de superhéroes:", num_heroes)

# e. corregir Doctor Strange (proximidad)
mal_cargado = arbol.buscar_proximidad("Doctor Strange")
if mal_cargado:
    mal_cargado[0].nombre = "Doctor Strange"
print("Corregido:", [n.nombre for n in mal_cargado])

# f. superhéroes ordenados descendente
heroes_desc = arbol.barrido_inorden(lambda n: n.es_heroe, descendente=True)
print("Superhéroes descendente:", heroes_desc)

# g. bosque de héroes y villanos
arbol_heroes = ArbolABB()
arbol_villanos = ArbolABB()
for nodo in arbol.barrido_inorden_obj():
    if nodo.es_heroe:
        arbol_heroes.insertar(nodo.nombre, True)
    else:
        arbol_villanos.insertar(nodo.nombre, False)

print("Nodos en árbol de héroes:", arbol_heroes.contar_nodos())
print("Nodos en árbol de villanos:", arbol_villanos.contar_nodos())
print("Héroes ordenados:", arbol_heroes.barrido_inorden())
print("Villanos ordenados:", arbol_villanos.barrido_inorden())