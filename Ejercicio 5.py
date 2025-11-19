import heapq
from collections import deque

class Grafo:
  

    def __init__(self):
        self.adj = {}       # Lista de adyacencia: {nodo: [(vecino, peso)]}
        self.nodes_data = {} # Atributos de los nodos: {nodo: {tipo: 'pc', ...}}

    def agregar_nodo(self, nodo, **kwargs):
        """Agrega un nodo al grafo con sus atributos."""
        if nodo not in self.adj:
            self.adj[nodo] = []
            self.nodes_data[nodo] = kwargs

    def agregar_arista(self, nodo1, nodo2, peso):
        """Agrega una arista no dirigida con peso."""
        self.agregar_nodo(nodo1)
        self.agregar_nodo(nodo2)
        # Añade la arista en ambas direcciones para un grafo no dirigido
        self.adj[nodo1].append((nodo2, peso))
        self.adj[nodo2].append((nodo1, peso))

    def get_tipo(self, nodo):
        """Obtiene el tipo de un nodo."""
        return self.nodes_data.get(nodo, {}).get('tipo')

    def nodos(self):
        """Devuelve todos los nodos del grafo."""
        return self.adj.keys()

def bfs(graph, start_node):
    """Búsqueda en Amplitud (Breadth-First Search)."""
    if start_node not in graph.nodos():
        return f"Nodo de inicio '{start_node}' no encontrado."
    visited = {start_node}
    queue = deque([start_node])
    traversal = []
    while queue:
        current = queue.popleft()
        traversal.append(current)
        for neighbor, _ in graph.adj.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal

def dfs(graph, start_node):
    """Búsqueda en Profundidad (Depth-First Search)."""
    if start_node not in graph.nodos():
        return f"Nodo de inicio '{start_node}' no encontrado."
    visited = set()
    traversal = []
    def dfs_recursive(current):
        visited.add(current)
        traversal.append(current)
        for neighbor, _ in graph.adj.get(current, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    dfs_recursive(start_node)
    return traversal

def dijkstra(graph, start_node, end_node):
    """Implementación del algoritmo de Dijkstra para encontrar el camino más corto."""
    if start_node not in graph.nodos() or end_node not in graph.nodos():
        return float('inf'), []
    distances = {node: float('inf') for node in graph.nodos()}
    distances[start_node] = 0
    predecessors = {node: None for node in graph.nodos()}
    priority_queue = [(0, start_node)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph.adj.get(current_node, []):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    path = []
    current = end_node
    while current:
        path.append(current)
        current = predecessors[current]
        if current == start_node:
             path.append(current)
             break
    path.reverse()
    if path and path[0] == start_node:
        return distances[end_node], path
    else:
        return float('inf'), []

def prim_mst(graph):
    """Implementación del algoritmo de Prim para el Árbol de Expansión Mínima (MST)."""
    if not graph.nodos():
        return 0, []
    start_node = next(iter(graph.nodos()))
    mst_set = {start_node}
    edges_to_process = []
    mst_edges = []
    total_cost = 0
    for neighbor, weight in graph.adj.get(start_node, []):
        heapq.heappush(edges_to_process, (weight, start_node, neighbor))
    while edges_to_process:
        weight, u, v = heapq.heappop(edges_to_process)
        if v not in mst_set:
            mst_set.add(v)
            mst_edges.append((u, v, weight))
            total_cost += weight
            for next_neighbor, next_weight in graph.adj.get(v, []):
                if next_neighbor not in mst_set:
                    heapq.heappush(edges_to_process, (next_weight, v, next_neighbor))
    if len(mst_set) != len(graph.nodos()):
        print("Advertencia: El grafo no está conectado. El MST es un 'bosque' (varios árboles).")
    return total_cost, mst_edges




def tarea_5_analisis_red(grafo, impresora_conectada_a='Router 01'):
    print("=" * 60)
    print("TAREA 5: ANÁLISIS DE ESQUEMA DE RED (Grafo No Dirigido)")
    print("=" * 60)

    # a. Carga del grafo con atributos de tipo (ya realizada en setup)
    print("a. Grafo cargado con los siguientes tipos de nodos:")
    for nodo, data in grafo.nodes_data.items():
        print(f"   - {nodo}: {data.get('tipo')}")
    print("-" * 60)
    
    # b. Barrido en profundidad y amplitud desde las tres notebook
    notebooks = ["Red Hat", "Debian", "Arch"]
    print("b. Barrido desde las tres Notebooks:")
    for nb in notebooks:
        print(f"   - BFS desde {nb}: {bfs(grafo, nb)}")
        print(f"   - DFS desde {nb}: {dfs(grafo, nb)}")
    print("-" * 60)

    # c. Camino más corto para enviar a imprimir
    impresora = "Impresora"
    nodos_imprimir = ["Manjaro", "Red Hat", "Fedora"]
    print(f"c. Camino más corto hasta la '{impresora}' (conectada a {impresora_conectada_a}):")
    
    resultados_c = {}
    for nodo in nodos_imprimir:
        costo, camino = dijkstra(grafo, nodo, impresora)
        resultados_c[nodo] = (costo, camino)
        print(f"   - Desde {nodo}: Costo={costo}, Camino={camino}")
    print("-" * 60)

    # d. Encontrar el Árbol de Expansión Mínima (MST)
    costo_mst, mst_aristas = prim_mst(grafo)
    print("d. Árbol de Expansión Mínima (MST):")
    print(f"   - Costo Total del MST: {costo_mst}")
    print(f"   - Aristas del MST (Nodo1, Nodo2, Peso): {mst_aristas}")
    print("-" * 60)

    # e. Camino más corto desde PC (no notebook) al servidor "Guaraní"
    servidor_guarani = "Guaraní"
    # Filtrar solo PCs
    pcs = [nodo for nodo, data in grafo.nodes_data.items() if data.get('tipo') == 'pc']
    print(f"e. Camino más corto desde las PCs (no Notebooks) hasta el servidor '{servidor_guarani}':")
    
    mejor_pc_e = None
    min_costo_e = float('inf')

    for pc in pcs:
        costo, camino = dijkstra(grafo, pc, servidor_guarani)
        print(f"   - Desde {pc}: Costo={costo}, Camino={camino}")
        if costo < min_costo_e:
            min_costo_e = costo
            mejor_pc_e = pc
            
    print(f"   -> La PC con el camino más corto es: {mejor_pc_e} con costo {min_costo_e}")
    print("-" * 60)

    # f. Camino más corto desde computadora del Switch 01 a "MongoDB"
    servidor_mongodb = "MongoDB"
    # Computadoras conectadas al Switch 01
    computadoras_switch01 = ["Manjaro", "Mint", "Red Hat", "Debian"] 
    print(f"f. Camino más corto desde las computadoras conectadas a 'Switch 01' hasta el servidor '{servidor_mongodb}':")
    
    mejor_comp_f = None
    min_costo_f = float('inf')
    
    for comp in computadoras_switch01:
        costo, camino = dijkstra(grafo, comp, servidor_mongodb)
        print(f"   - Desde {comp}: Costo={costo}, Camino={camino}")
        if costo < min_costo_f:
            min_costo_f = costo
            mejor_comp_f = comp
            
    print(f"   -> La computadora con el camino más corto es: {mejor_comp_f} con costo {min_costo_f}")
    print("-" * 60)

def setup_tarea_5():
    """Configura el grafo inicial de la red."""
    g = Grafo()
    
    # a. Cargar nodos con sus tipos
    pcs = ["Manjaro", "Mint", "Fedora", "Ubuntu", "Kali"]
    notebooks = ["Red Hat", "Debian", "Arch"]
    servidores = ["Guaraní", "MongoDB"]
    otros = {"Router 01": "router", "Router 02": "router", 
             "Switch 01": "switch", "Switch 02": "switch", "Impresora": "impresora"}

    for pc in pcs:
        g.agregar_nodo(pc, tipo='pc')
    for nb in notebooks:
        g.agregar_nodo(nb, tipo='notebook')
    for serv in servidores:
        g.agregar_nodo(serv, tipo='servidor')
    for nodo, tipo in otros.items():
        g.agregar_nodo(nodo, tipo=tipo)
        
    # Conexiones (Pesos son estimados como costo/latencia)
    # Switch 01 (S01)
    g.agregar_arista("Switch 01", "Manjaro", 1)
    g.agregar_arista("Switch 01", "Mint", 1)
    g.agregar_arista("Switch 01", "Red Hat", 1)
    g.agregar_arista("Switch 01", "Debian", 1)
    # Switch 02 (S02)
    g.agregar_arista("Switch 02", "Fedora", 1)
    g.agregar_arista("Switch 02", "Ubuntu", 1)
    g.agregar_arista("Switch 02", "Kali", 1)
    g.agregar_arista("Switch 02", "Arch", 1)
    
    # Router 01 (R01)
    g.agregar_arista("Router 01", "Switch 01", 2)
    g.agregar_arista("Router 01", "Switch 02", 3)
    g.agregar_arista("Router 01", "Guaraní", 5)
    g.agregar_arista("Router 01", "Router 02", 8)
    
    # Impresora (Conexión inicial)
    g.agregar_arista("Router 01", "Impresora", 10) # Peso estimado
    
    # Router 02 (R02)
    g.agregar_arista("Router 02", "MongoDB", 5)
    
    return g

def tarea_5_punto_g_cambio(g):
    """Implementa el punto 5.g: Cambiar conexión de impresora y resolver b."""
    print("g. Cambiar conexión de la impresora y resolver el punto c de nuevo:")
    
    # Eliminar arista Impresora-Router 01
    g.adj["Router 01"] = [a for a in g.adj["Router 01"] if a[0] != "Impresora"]
    g.adj["Impresora"] = [a for a in g.adj["Impresora"] if a[0] != "Router 01"]
    
    # Agregar arista Impresora-Router 02
    g.agregar_arista("Router 02", "Impresora", 6)
    
    print("   - Nueva conexión: Impresora -> Router 02 (Costo: 6)")
    
    # Resolver punto c de nuevo
    impresora = "Impresora"
    nodos_imprimir = ["Manjaro", "Red Hat", "Fedora"]
    print("\n   - Nuevo Camino más corto hasta la 'Impresora' (conectada a Router 02):")
    
    for nodo in nodos_imprimir:
        costo, camino = dijkstra(g, nodo, impresora)
        print(f"     - Desde {nodo}: Costo={costo}, Camino={camino}")
    print("-" * 60)



if __name__ == "__main__":
    # Tarea 5: Ejecución Inicial (Puntos a, b, c, d, e, f)
    grafo_red = setup_tarea_5()
    tarea_5_analisis_red(grafo_red, impresora_conectada_a='Router 01')
    
    # Tarea 5: Punto G (Reconfiguración y nuevo análisis)
    tarea_5_punto_g_cambio(grafo_red)