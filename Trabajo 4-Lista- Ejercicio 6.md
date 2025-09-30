
class SuperHeroe:
    def __init__(self, nombre, anio, casa, biografia):
        self.nombre = nombre
        self.anio = anio
        self.casa = casa
        self.biografia = biografia
        self.next = None

class ListaSuperHeroes:
    def __init__(self):
        self.head = None

    def agregar(self, nombre, anio, casa, biografia):
        nuevo = SuperHeroe(nombre, anio, casa, biografia)
        nuevo.next = self.head
        self.head = nuevo

    # a. Eliminar el nodo de Linterna Verde
    def eliminar_linterna_verde(self):
        actual = self.head
        previo = None
        while actual:
            if actual.nombre.lower() == "linterna verde":
                if previo:
                    previo.next = actual.next
                else:
                    self.head = actual.next
                return True
            previo = actual
            actual = actual.next
        return False

    # b. Mostrar año de aparición de Wolverine
    def anio_wolverine(self):
        actual = self.head
        while actual:
            if actual.nombre.lower() == "wolverine":
                return actual.anio
            actual = actual.next
        return None

    # c. Cambiar la casa de Dr. Strange a Marvel
    def cambiar_casa_dr_strange(self):
        actual = self.head
        while actual:
            if actual.nombre.lower() == "dr. strange":
                actual.casa = "Marvel"
            actual = actual.next

    # d. Mostrar nombres que en la biografía tienen "traje" o "armadura"
    def nombres_traje_armadura(self):
        nombres = []
        actual = self.head
        while actual:
            bio = actual.biografia.lower()
            if "traje" in bio or "armadura" in bio:
                nombres.append(actual.nombre)
            actual = actual.next
        return nombres

    # e. Mostrar nombre y casa de los que aparecieron antes de 1963
    def nombre_casa_antes_1963(self):
        resultados = []
        actual = self.head
        while actual:
            if actual.anio < 1963:
                resultados.append((actual.nombre, actual.casa))
            actual = actual.next
        return resultados

    # f. Mostrar casa de Capitana Marvel y Mujer Maravilla
    def casa_capitana_mujer(self):
        casas = {}
        actual = self.head
        while actual:
            if actual.nombre.lower() in ["capitana marvel", "mujer maravilla"]:
                casas[actual.nombre] = actual.casa
            actual = actual.next
        return casas

    # g. Mostrar toda la info de Flash y Star-Lord
    def info_flash_starlord(self):
        resultados = []
        actual = self.head
        while actual:
            if actual.nombre.lower() in ["flash", "star-lord"]:
                resultados.append(vars(actual))
            actual = actual.next
        return resultados

    # h. Listar superhéroes que comienzan con B, M y S
    def listar_bms(self):
        letras = ['b', 'm', 's']
        resultados = []
        actual = self.head
        while actual:
            if actual.nombre[0].lower() in letras:
                resultados.append(actual.nombre)
            actual = actual.next
        return resultados

    # i. Contar cuántos superhéroes hay de cada casa
    def contar_por_casa(self):
        conteo = {}
        actual = self.head
        while actual:
            casa = actual.casa
            conteo[casa] = conteo.get(casa, 0) + 1
            actual = actual.next
        return conteo
