import heapq
from collections import deque

class Grafo:
    """
    Clase para representar un grafo no dirigido con pesos en las aristas.
    Permite almacenar atributos adicionales en los nodos (tipo de equipo, ambiente, etc.).
    """
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



def setup_tarea_14():
    """Configura el grafo del hogar (ambientes y distancias en metros)."""
    g = Grafo()
    
    # a. Cargar nodos (ambientes)
    ambientes = ["Cocina", "Comedor", "Cochera", "Quincho", "Baño 1", "Baño 2", 
                 "Habitación 1", "Habitación 2", "Sala de Estar", "Terraza", "Patio"]
    for amb in ambientes:
        g.agregar_nodo(amb, tipo='ambiente')
        
    # b. Cargar aristas (distancias en metros). Se garantiza 3-5 aristas por ambiente.
    # Nodos con 5 aristas: Habitación 1, Comedor, Sala de Estar
    
    # Habitación 1 (5 aristas)
    g.agregar_arista("Habitación 1", "Sala de Estar", 4)
    g.agregar_arista("Habitación 1", "Baño 1", 2)
    g.agregar_arista("Habitación 1", "Habitación 2", 3)
    g.agregar_arista("Habitación 1", "Comedor", 5)
    g.agregar_arista("Habitación 1", "Cochera", 8)
    
    # Habitación 2 (3 aristas)
    g.agregar_arista("Habitación 2", "Baño 2", 2)
    g.agregar_arista("Habitación 2", "Comedor", 4)
    g.agregar_arista("Habitación 2", "Sala de Estar", 5)
    
    # Comedor (5 aristas)
    g.agregar_arista("Comedor", "Cocina", 2)
    g.agregar_arista("Comedor", "Sala de Estar", 1) # Pasillo corto
    g.agregar_arista("Comedor", "Cochera", 10)
    g.agregar_arista("Comedor", "Quincho", 7)
    g.agregar_arista("Comedor", "Terraza", 6)

    # Sala de Estar (5 aristas)
    # Ya conectada a H1, H2, Comedor. Agregamos 2 más.
    g.agregar_arista("Sala de Estar", "Baño 1", 3)
    g.agregar_arista("Sala de Estar", "Terraza", 3)
    g.agregar_arista("Sala de Estar", "Patio", 12) 

    # Nodos restantes (min 3 aristas cada uno)
    
    # Cocina (4 aristas)
    # Ya conectada a Comedor.
    g.agregar_arista("Cocina", "Baño 1", 6) 
    g.agregar_arista("Cocina", "Baño 2", 5)
    g.agregar_arista("Cocina", "Cochera", 7)

    # Baño 1 (3 aristas)
    # Ya conectada a H1, SE, C. OK.

    # Baño 2 (3 aristas)
    # Ya conectada a H2, C.
    g.agregar_arista("Baño 2", "Cochera", 9) 

    # Cochera (4 aristas)
    # Ya conectada a H1, CO, C, B2. OK.

    # Quincho (3 aristas)
    # Ya conectado a CO.
    g.agregar_arista("Quincho", "Cochera", 4)
    g.agregar_arista("Quincho", "Patio", 6)

    # Terraza (3 aristas)
    # Ya conectada a CO, SE.
    g.agregar_arista("Terraza", "Patio", 5)

    # Patio (3 aristas)
    # Ya conectada a SE, Q, T. OK.
    
    return g

def tarea_14_analisis_hogar(grafo):
    print("\n" + "=" * 60)
    print("TAREA 14: ANÁLISIS DE AMBIENTES DEL HOGAR (Grafo No Dirigido)")
    print("=" * 60)

    # a. y b. Nodos y Aristas cargadas
    print("a. y b. Grafo de ambientes cargado (Distancias en metros).")
    print(f"   - Total de ambientes (nodos): {len(grafo.nodos())}")
    
    # Comprobación de la restricción de aristas
    for nodo in grafo.nodos():
        num_aristas = len(grafo.adj[nodo])
        print(f"   - {nodo}: {num_aristas} aristas.")
    print("-" * 60)
    
    # c. Árbol de Expansión Mínima (MST) y metros de cable
    costo_mst, mst_aristas = prim_mst(grafo)
    
    print("c. Árbol de Expansión Mínima (MST):")
    print("   - MST Aristas (Ambiente 1, Ambiente 2, Metros):")
    for u, v, w in mst_aristas:
        print(f"     - {u} <-> {v}: {w}m")
        
    print(f"\n   -> Metros de cable necesarios para conectar todos los ambientes (Costo total del MST): {costo_mst} metros")
    print("-" * 60)
    
    # d. Camino más corto para cable de red (Habitación 1 a Sala de Estar)
    start_node = "Habitación 1"
    end_node = "Sala de Estar"
    
    costo, camino = dijkstra(grafo, start_node, end_node)
    
    print(f"d. Camino más corto desde '{start_node}' hasta '{end_node}' (para cable de red/Smart Tv):")
    print(f"   - Camino más corto (Ambientes): {camino}")
    print(f"   -> Metros de cable de red necesarios: {costo} metros")
    print("-" * 60)




if __name__ == "__main__":
    grafo_hogar = setup_tarea_14()
    tarea_14_analisis_hogar(grafo_hogar)