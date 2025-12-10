"""Implementación del DFS
Implementación recursiva:
Implementación iterativa (con pila):


Dijkstra: encuentra caminos más cortos en grafos ponderados.
Implementación en Python (simplificada):


Floyd-Warshall


Bellman-Ford. Implementación (Python):


El algoritmo de Kruskal. Implementación (Python):
# Implementación de Kruskal en Python 


El algoritmo de Prim . Implementación (Python):"""


"""----------------------------------    GRAFOS    ----------------------------------"""

#Grafos no dirigidos. Algoritmo: BFS (Breadth-First Search) para recorrer niveles
from collections import deque 

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft() 

        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor) 

# Ejemplo
g = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}
bfs(g, 1) 



#Algoritmo: DFS (Depth-First Search) recursivo
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set() 

    if node not in visited:
        print(node)
        visited.add(node) 

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited) 

# Ejemplo
dfs(g, 1) 







#Grafos dirigidos. Algoritmo: Topological Sort (ordenamiento topológico) Sólo funciona si el grafo es acíclico (DAG).
from collections import defaultdict 

def topo_sort(graph):
    visited = set()
    order = [] 

    def dfs(v):
        visited.add(v)
        for nei in graph[v]:
            if nei not in visited:
                dfs(nei)
        order.append(v) 

    for node in graph:
        if node not in visited:
            dfs(node) 

    return order[::-1]  # Invertido 

# Ejemplo
g2 = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
} 

print(topo_sort(g2))











#Grafos ponderados. Algoritmo: Dijkstra (ruta más corta desde un nodo)
import heapq 

def dijkstra(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    pq = [(0, start)] 

    while pq:
        current_dist, node = heapq.heappop(pq) 

        if current_dist > dist[node]:
            continue 

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight 

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor)) 

    return dist 

# Ejemplo
g3 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
} 

print(dijkstra(g3, 'A')) 








#Grafos ponderados con pesos negativos. Algoritmo: Bellman–Ford
def bellman_ford(edges, n_nodes, start):
    dist = [float("inf")] * n_nodes
    dist[start] = 0 

    for _ in range(n_nodes - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w 

    return dist 

# Ejemplo
edges = [
    (0, 1, 5),
    (0, 2, 4),
    (1, 3, 3),
    (2, 1, 6),
    (3, 2, -2)
] 

print(bellman_ford(edges, 4, 0)) 








#Grafos para detectar componentes  Algoritmo: Union–Find (Disjoint Set)
#Detecta componentes conectadas y ciclos.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n)) 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x] 

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pb] = pa 

# Ejemplo
dsu = DSU(5)
dsu.union(0, 1)
dsu.union(1, 2)
print(dsu.find(2)) 








#Grafos para encontrar Árboles de Expansión Mínima (MST)
#Algoritmo Kruskal
def kruskal(edges, n_nodes):
    dsu = DSU(n_nodes)
    mst = []
    edges = sorted(edges, key=lambda x: x[2]) 

    for u, v, w in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, w)) 

    return mst 

# Ejemplo
edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4)
] 

print(kruskal(edges, 4)) 











#Algoritmo Prim
import heapq 

def prim(graph, start):
    visited = set()
    pq = [(0, start)]
    mst_weight = 0 

    while pq:
        weight, node = heapq.heappop(pq) 

        if node in visited:
            continue 

        visited.add(node)
        mst_weight += weight 

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (w, neighbor)) 

    return mst_weight 

# Ejemplo
g4 = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)]
} 

print(prim(g4, 0))









#Grafo dirigido
#Código completo (Grafo dirigido + CRUD + algoritmos)
from collections import deque, defaultdict
import heapq 

class DirectedGraph:
    """
    Grafo dirigido representado como:
      self.adj: dict[node] -> list of (neighbor, weight)
    Soporta nodos de tipo hashable (int, str, etc).
    """ 

    def __init__(self):
        self.adj = {}  # mapa nodo -> lista de (vecino, peso) 

    # -------------------
    # CRUD: NODOS
    # -------------------
    def add_node(self, node):
        """Crear/asegurar existencia del nodo."""
        if node not in self.adj:
            self.adj[node] = [] 

    def get_nodes(self):
        """Listar nodos."""
        return list(self.adj.keys()) 

    def remove_node(self, node):
        """Eliminar un nodo y todas las aristas entrantes y salientes."""
        if node not in self.adj:
            raise KeyError(f"Node {node} not found")
        # borrar aristas entrantes
        for u in list(self.adj.keys()):
            self.adj[u] = [(v,w) for (v,w) in self.adj[u] if v != node]
        # borrar el nodo
        del self.adj[node] 

    # -------------------
    # CRUD: ARISTAS
    # -------------------
    def add_edge(self, u, v, weight=1):
        """Añadir arista dirigida u -> v con peso (por defecto 1). Crea nodos si no existen."""
        self.add_node(u)
        self.add_node(v)
        # si ya existe la arista, la actualizamos
        for i, (nei, w) in enumerate(self.adj[u]):
            if nei == v:
                self.adj[u][i] = (v, weight)
                return
        self.adj[u].append((v, weight)) 

    def get_edges(self):
        """Listar aristas como (u, v, w)."""
        edges = []
        for u in self.adj:
            for v, w in self.adj[u]:
                edges.append((u, v, w))
        return edges 

    def get_edge(self, u, v):
        """Obtener peso de la arista u->v o None si no existe."""
        if u not in self.adj:
            return None
        for nei, w in self.adj[u]:
            if nei == v:
                return w
        return None 

    def remove_edge(self, u, v):
        """Eliminar arista u->v."""
        if u not in self.adj:
            raise KeyError(f"Node {u} not found")
        self.adj[u] = [(nei,w) for (nei,w) in self.adj[u] if nei != v] 

    def update_edge_weight(self, u, v, new_weight):
        """Actualizar peso de arista u->v."""
        if u not in self.adj:
            raise KeyError(f"Node {u} not found")
        found = False
        for i, (nei, w) in enumerate(self.adj[u]):
            if nei == v:
                self.adj[u][i] = (v, new_weight)
                found = True
                break
        if not found:
            raise KeyError(f"Edge {u}->{v} not found") 

    # -------------------
    # ALGORITMOS
    # -------------------
    def bfs(self, start):
        """Breadth-first search: retorna lista con orden de visita."""
        if start not in self.adj:
            raise KeyError(f"Node {start} not found")
        visited = set([start])
        q = deque([start])
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v, _ in self.adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return order 

    def dfs(self, start):
        """DFS iterativo (retorna orden de llegada)."""
        if start not in self.adj:
            raise KeyError(f"Node {start} not found")
        visited = set()
        stack = [start]
        order = []
        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            order.append(u)
            # push neighbors in reverse para simular recursivo
            for v, _ in reversed(self.adj[u]):
                if v not in visited:
                    stack.append(v)
        return order 

    def _dfs_cycle_util(self, node, visited, rec_stack):
        """Utilitario para detección de ciclos (DFS recursivo)."""
        visited.add(node)
        rec_stack.add(node)
        for nei, _ in self.adj[node]:
            if nei not in visited:
                if self._dfs_cycle_util(nei, visited, rec_stack):
                    return True
            elif nei in rec_stack:
                return True
        rec_stack.remove(node)
        return False 

    def has_cycle(self):
        """Detecta si hay ciclos en el grafo dirigido."""
        visited = set()
        rec_stack = set()
        for node in self.adj:
            if node not in visited:
                if self._dfs_cycle_util(node, visited, rec_stack):
                    return True
        return False 

    def topological_sort(self):
        """
        Ordenamiento topológico (Kahn).
        Lanza ValueError si el grafo tiene ciclos.
        """
        # calcular in-degrees
        indeg = {u: 0 for u in self.adj}
        for u in self.adj:
            for v, _ in self.adj[u]:
                indeg[v] = indeg.get(v, 0) + 1 

        q = deque([u for u in indeg if indeg[u] == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in self.adj.get(u, []):
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v) 

        if len(topo) != len(indeg):
            raise ValueError("Graph has at least one cycle; topological sort not possible")
        return topo 

    def dijkstra(self, start):
        """
        Dijkstra: caminos más cortos desde start (asume pesos >= 0).
        Retorna dict node -> distance, y predecessor dict para reconstrucción.
        """
        if start not in self.adj:
            raise KeyError(f"Node {start} not found") 

        dist = {u: float("inf") for u in self.adj}
        prev = {u: None for u in self.adj}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev 

    def bellman_ford(self, start):
        """
        Bellman-Ford: funciona con pesos negativos.
        Retorna (dist, prev). Si detecta ciclo negativo lanza ValueError.
        """
        nodes = list(self.adj.keys())
        idx = {node:i for i,node in enumerate(nodes)}
        n = len(nodes)
        dist = {u: float("inf") for u in nodes}
        prev = {u: None for u in nodes}
        if start not in self.adj:
            raise KeyError(f"Node {start} not found")
        dist[start] = 0 

        edges = self.get_edges()  # (u,v,w)
        for _ in range(n-1):
            updated = False
            for u, v, w in edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    updated = True
            if not updated:
                break 

        # check negative cycles
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle") 

        return dist, prev 

    def kosaraju_scc(self):
        """
        Kosaraju para componentes fuertemente conectadas.
        Retorna lista de listas: cada sublista es una SCC.
        """
        visited = set()
        stack = [] 

        def dfs1(u):
            visited.add(u)
            for v, _ in self.adj[u]:
                if v not in visited:
                    dfs1(v)
            stack.append(u) 

        for u in self.adj:
            if u not in visited:
                dfs1(u) 

        # construir grafo transpuesto
        transpose = DirectedGraph()
        for u in self.adj:
            transpose.add_node(u)
        for u in self.adj:
            for v, w in self.adj[u]:
                transpose.add_edge(v, u, w)  # invertir arista 

        visited.clear()
        sccs = []
        while stack:
            u = stack.pop()
            if u not in visited:
                comp = []
                def dfs2(x):
                    visited.add(x)
                    comp.append(x)
                    for y,_ in transpose.adj[x]:
                        if y not in visited:
                            dfs2(y)
                dfs2(u)
                sccs.append(comp)
        return sccs 

    # -------------------
    # UTILIDADES
    # -------------------
    def __repr__(self):
        return f"DirectedGraph(nodes={len(self.adj)}, edges={len(self.get_edges())})" 

#Ejemplo de uso — CRUD + ejecución de algoritmos
if __name__ == "__main__":
    g = DirectedGraph() 

    # --- CRUD: crear nodos y aristas ---
    g.add_node("A")
    g.add_node("B")
    g.add_edge("A", "B", weight=3)
    g.add_edge("A", "C", weight=1)
    g.add_edge("B", "C", weight=7)
    g.add_edge("C", "D", weight=2)
    g.add_edge("D", "B", weight=-4)  # arista con peso negativo (prueba Bellman-Ford)
    g.add_node("E")  # nodo aislado 

    print("Nodos:", g.get_nodes())
    print("Aristas:", g.get_edges()) 

    # Leer arista
    print("Peso A->B:", g.get_edge("A", "B")) 

    # Actualizar peso
    g.update_edge_weight("A", "B", 5)
    print("Peso A->B actualizado:", g.get_edge("A", "B")) 

    # Eliminar arista
    g.remove_edge("B", "C")
    print("Aristas tras eliminar B->C:", g.get_edges()) 

    # --- Algoritmos ---
    print("BFS desde A:", g.bfs("A"))
    print("DFS desde A:", g.dfs("A"))
    print("¿Tiene ciclo?", g.has_cycle()) 

    # Topological sort (podría lanzar ValueError si hay ciclo)
    try:
        topo = g.topological_sort()
        print("Topological order:", topo)
    except ValueError as e:
        print("Topological sort error:", e) 

    # Dijkstra (requiere pesos no negativos; aquí hay negativos así que no es apropiado, usamos Bellman-Ford)
    try:
        dist, prev = g.dijkstra("A")
        print("Dijkstra distancias desde A:", dist)
    except Exception as e:
        print("Dijkstra error (posible pesos negativos):", e) 

    # Bellman-Ford
    try:
        dist_bf, prev_bf = g.bellman_ford("A")
        print("Bellman-Ford distancias desde A:", dist_bf)
    except ValueError as e:
        print("Bellman-Ford error:", e) 

    # SCCs
    print("Componentes fuertemente conectadas (SCC):", g.kosaraju_scc()) 

    # Eliminar nodo
    g.remove_node("E")
    print("Nodos tras eliminar E:", g.get_nodes())



















#Grafo no dirigido. Código completo — Grafo No Dirigido (CRUD + algoritmos)
from collections import deque
import heapq 

class UndirectedGraph:
    """
    Grafo no dirigido representado como:
      self.adj: dict[node] -> list of (neighbor, weight)
    Los nodos pueden ser cualquier tipo 'hashable' (int, str, ...).
    Las aristas se almacenan en ambas direcciones: u->v y v->u.
    """ 

    def __init__(self):
        self.adj = {} 

    # -------------------
    # CRUD: NODOS
    # -------------------
    def add_node(self, node):
        """Crear/asegurar existencia del nodo."""
        if node not in self.adj:
            self.adj[node] = [] 

    def get_nodes(self):
        """Listar nodos."""
        return list(self.adj.keys()) 

    def remove_node(self, node):
        """Eliminar un nodo y todas sus aristas incidentes."""
        if node not in self.adj:
            raise KeyError(f"Node {node} not found")
        # eliminar aristas entrantes en otros nodos
        for u in list(self.adj.keys()):
            self.adj[u] = [(v,w) for (v,w) in self.adj[u] if v != node]
        # borrar el nodo
        del self.adj[node] 

    # -------------------
    # CRUD: ARISTAS
    # -------------------
    def add_edge(self, u, v, weight=1):
        """Añadir arista no dirigida entre u y v (crea nodos si no existen)."""
        self.add_node(u)
        self.add_node(v) 

        # añadimos/actualizamos u -> v
        updated = False
        for i, (nei, w) in enumerate(self.adj[u]):
            if nei == v:
                self.adj[u][i] = (v, weight)
                updated = True
                break
        if not updated:
            self.adj[u].append((v, weight)) 

        # añadimos/actualizamos v -> u
        updated = False
        for i, (nei, w) in enumerate(self.adj[v]):
            if nei == u:
                self.adj[v][i] = (u, weight)
                updated = True
                break
        if not updated:
            self.adj[v].append((u, weight)) 

    def get_edges(self):
        """Listar aristas como (u, v, w), pero evitando duplicados (u<v)."""
        edges = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u]:
                key = tuple(sorted((u, v), key=lambda x: str(x)))
                if key not in seen:
                    edges.append((u, v, w))
                    seen.add(key)
        return edges 

    def get_edge(self, u, v):
        """Obtener peso de la arista u-v o None si no existe."""
        if u not in self.adj:
            return None
        for nei, w in self.adj[u]:
            if nei == v:
                return w
        return None 

    def remove_edge(self, u, v):
        """Eliminar la arista u-v en ambas direcciones."""
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        self.adj[u] = [(nei,w) for (nei,w) in self.adj[u] if nei != v]
        self.adj[v] = [(nei,w) for (nei,w) in self.adj[v] if nei != u] 

    def update_edge_weight(self, u, v, new_weight):
        """Actualizar peso de la arista u-v."""
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        found = False
        for i, (nei, w) in enumerate(self.adj[u]):
            if nei == v:
                self.adj[u][i] = (v, new_weight)
                found = True
                break
        for i, (nei, w) in enumerate(self.adj[v]):
            if nei == u:
                self.adj[v][i] = (u, new_weight)
                found = True
                break
        if not found:
            raise KeyError(f"Edge {u}-{v} not found") 

    # -------------------
    # ALGORITMOS
    # -------------------
    def bfs(self, start):
        """BFS: retorna orden de visita y distancia (en número de aristas) desde start."""
        if start not in self.adj:
            raise KeyError("Start node not in graph")
        visited = {start}
        q = deque([start])
        order = []
        dist = {start: 0}
        while q:
            u = q.popleft()
            order.append(u)
            for v, _ in self.adj[u]:
                if v not in visited:
                    visited.add(v)
                    dist[v] = dist[u] + 1
                    q.append(v)
        return order, dist 

    def dfs(self, start):
        """DFS iterativo: retorna orden de visita."""
        if start not in self.adj:
            raise KeyError("Start node not in graph")
        visited = set()
        stack = [start]
        order = []
        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            order.append(u)
            # iterar vecinos en orden para reproducibilidad
            for v, _ in reversed(self.adj[u]):
                if v not in visited:
                    stack.append(v)
        return order 

    def connected_components(self):
        """Devuelve lista de componentes conectadas (cada una como lista de nodos)."""
        visited = set()
        comps = []
        for node in self.adj:
            if node not in visited:
                comp = []
                stack = [node]
                while stack:
                    u = stack.pop()
                    if u in visited:
                        continue
                    visited.add(u)
                    comp.append(u)
                    for v, _ in self.adj[u]:
                        if v not in visited:
                            stack.append(v)
                comps.append(comp)
        return comps 

    def has_cycle(self):
        """
        Detecta ciclo en grafo no dirigido usando DFS y control del 'parent'.
        Retorna True si hay ciclo.
        """
        visited = set() 

        def dfs(u, parent):
            visited.add(u)
            for v, _ in self.adj[u]:
                if v == parent:
                    continue
                if v in visited:
                    return True
                if dfs(v, u):
                    return True
            return False 

        for node in self.adj:
            if node not in visited:
                if dfs(node, None):
                    return True
        return False 

    def dijkstra(self, start):
        """
        Dijkstra: caminos más cortos desde start (pesos >= 0).
        Retorna (dist, prev) donde prev permite reconstruir caminos.
        """
        if start not in self.adj:
            raise KeyError("Start node not in graph")
        dist = {u: float('inf') for u in self.adj}
        prev = {u: None for u in self.adj}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev 

    def bellman_ford(self, start):
        """
        Bellman-Ford: caminos más cortos con posibilidad de pesos negativos.
        IMPORTANTE: en grafos no dirigidos, una arista negativa entre u-v
        crea un ciclo negativo u->v->u si se considera como dos aristas dirigidas.
        Por eso, NUNCA uses Bellman-Ford con aristas negativas en grafo no dirigido
        salvo que lo transformes correctamente.
        Aquí se implementa suponiendo que el grafo es tratado como dirigido
        por cada dirección (u->v y v->u) — si hay arista negativa en práctica
        eso detectará ciclos negativos.
        """
        if start not in self.adj:
            raise KeyError("Start node not in graph")
        nodes = list(self.adj.keys())
        dist = {u: float('inf') for u in nodes}
        prev = {u: None for u in nodes}
        dist[start] = 0
        # construir lista de aristas dirigidas (u->v y v->u)
        edges = []
        for u in self.adj:
            for v, w in self.adj[u]:
                edges.append((u, v, w)) 

        n = len(nodes)
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    updated = True
            if not updated:
                break 

        # detectar ciclos negativos
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle") 

        return dist, prev 

    def is_bipartite(self):
        """Comprueba si el grafo es bipartito (2-colorable) con BFS."""
        color = {}
        for start in self.adj:
            if start in color:
                continue
            q = deque([start])
            color[start] = 0
            while q:
                u = q.popleft()
                for v, _ in self.adj[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False, {}
        return True, color 

    # -------------------
    # MST: Kruskal + Prim
    # -------------------
    class _DSU:
        def __init__(self, items):
            self.parent = {x: x for x in items}
            self.rank = {x: 0 for x in items}
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.rank[ra] < self.rank[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
            return True 

    def kruskal_mst(self):
        """Kruskal: retorna lista de aristas (u,v,w) del MST y peso total."""
        edges = self.get_edges()
        edges_sorted = sorted(edges, key=lambda x: x[2])
        dsu = UndirectedGraph._DSU(self.adj.keys())
        mst = []
        total = 0
        for u, v, w in edges_sorted:
            if dsu.union(u, v):
                mst.append((u, v, w))
                total += w
        return mst, total 

    def prim_mst(self, start=None):
        """Prim: retorna lista de aristas del MST y peso total. start optional."""
        if not self.adj:
            return [], 0
        if start is None:
            start = next(iter(self.adj))
        visited = set([start])
        edges = []
        pq = []
        for v,w in self.adj[start]:
            heapq.heappush(pq, (w, start, v))
        mst = []
        total = 0
        while pq and len(visited) < len(self.adj):
            w, u, v = heapq.heappop(pq)
            if v in visited:
                continue
            visited.add(v)
            mst.append((u, v, w))
            total += w
            for to, wt in self.adj[v]:
                if to not in visited:
                    heapq.heappush(pq, (wt, v, to))
        # Si no visitamos todos, el grafo no es conexo; devolvemos lo que haya.
        return mst, total 

    # -------------------
    # UTILIDAD
    # -------------------
    def reconstruct_path(self, prev, start, goal):
        """Reconstruye camino desde start hasta goal usando dict prev (o None si no hay)."""
        if prev.get(goal) is None and start != goal:
            return None
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            if cur == start:
                break
            cur = prev[cur]
        path.reverse()
        if path[0] == start:
            return path
        return None 

    def __repr__(self):
        return f"UndirectedGraph(nodes={len(self.adj)}, edges={len(self.get_edges())})" 

#Ejemplo de uso (CRUD + ejecución de algoritmos)
if __name__ == "__main__":
    g = UndirectedGraph() 

    # --- CRUD: Crear nodos y aristas ---
    g.add_node("A")
    g.add_node("B")
    g.add_edge("A", "B", weight=4)
    g.add_edge("A", "C", weight=2)
    g.add_edge("B", "C", weight=1)
    g.add_edge("B", "D", weight=5)
    g.add_edge("C", "D", weight=8)
    g.add_edge("C", "E", weight=10)
    g.add_edge("D", "E", weight=2) 

    print("Nodos:", g.get_nodes())
    print("Aristas:", g.get_edges()) 

    # Leer y actualizar una arista
    print("Peso A-C:", g.get_edge("A", "C"))
    g.update_edge_weight("A", "C", 3)
    print("Peso A-C actualizado:", g.get_edge("A", "C")) 

    # Eliminar arista y nodo
    g.remove_edge("C", "E")
    g.add_node("F")
    g.add_edge("E", "F", weight=7)
    print("Aristas tras cambios:", g.get_edges()) 

    # --- Algoritmos ---
    order_bfs, dist_bfs = g.bfs("A")
    print("BFS desde A:", order_bfs)
    print("Distancias (saltos) desde A:", dist_bfs) 

    print("DFS desde A:", g.dfs("A")) 

    print("Componentes conectadas:", g.connected_components())
    print("¿Tiene ciclo?", g.has_cycle()) 

    is_bip, coloring = g.is_bipartite()
    print("¿Bipartito?", is_bip, "Coloring (si True):", coloring) 

    # Dijkstra: caminos mínimos (pesos >= 0)
    dist, prev = g.dijkstra("A")
    print("Dijkstra distancias desde A:", dist)
    print("Camino A -> E:", g.reconstruct_path(prev, "A", "E")) 

    # Kruskal y Prim (MST)
    mst_kruskal, total_k = g.kruskal_mst()
    print("MST Kruskal:", mst_kruskal, "Peso total:", total_k) 

    mst_prim, total_p = g.prim_mst("A")
    print("MST Prim:", mst_prim, "Peso total:", total_p)








#Grafo ponderado. Código (guardar como weighted_graph.py o pegar en tu script)
from collections import deque
import heapq 

class WeightedGraph:
    """
    Grafo ponderado que puede ser dirigido (directed=True) o no dirigido.
    Representación: adj: dict[node] -> list of (neighbor, weight)
    Nodos: cualquier hashable (int, str, ...)
    """ 

    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed 

    # -------------------
    # CRUD NODOS
    # -------------------
    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = [] 

    def get_nodes(self):
        return list(self.adj.keys()) 

    def remove_node(self, node):
        if node not in self.adj:
            raise KeyError(f"Node {node} not found")
        # eliminar aristas incidentes
        for u in list(self.adj.keys()):
            self.adj[u] = [(v,w) for (v,w) in self.adj[u] if v != node]
        del self.adj[node] 

    # -------------------
    # CRUD ARISTAS
    # -------------------
    def add_edge(self, u, v, weight=1):
        """Añade arista u->v con peso. Si no dirigido, añade v->u con mismo peso."""
        self.add_node(u)
        self.add_node(v)
        # actualizar si ya existe
        updated = False
        for i, (nei, w) in enumerate(self.adj[u]):
            if nei == v:
                self.adj[u][i] = (v, weight)
                updated = True
                break
        if not updated:
            self.adj[u].append((v, weight)) 

        if not self.directed:
            updated = False
            for i, (nei, w) in enumerate(self.adj[v]):
                if nei == u:
                    self.adj[v][i] = (u, weight)
                    updated = True
                    break
            if not updated:
                self.adj[v].append((u, weight)) 

    def get_edges(self):
        """Lista de aristas (u,v,w). En no dirigido evita duplicados (u<=v)."""
        edges = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u]:
                if self.directed:
                    edges.append((u, v, w))
                else:
                    key = tuple(sorted((u, v), key=lambda x: str(x)))
                    if key in seen:
                        continue
                    seen.add(key)
                    edges.append((u, v, w))
        return edges 

    def get_edge(self, u, v):
        if u not in self.adj:
            return None
        for nei, w in self.adj[u]:
            if nei == v:
                return w
        return None 

    def update_edge_weight(self, u, v, new_weight):
        if u not in self.adj:
            raise KeyError(f"Node {u} not found")
        found = False
        for i,(nei,w) in enumerate(self.adj[u]):
            if nei == v:
                self.adj[u][i] = (v, new_weight)
                found = True
                break
        if not found:
            raise KeyError(f"Edge {u}->{v} not found")
        if not self.directed:
            # actualizar la otra dirección
            for i,(nei,w) in enumerate(self.adj[v]):
                if nei == u:
                    self.adj[v][i] = (u, new_weight)
                    break 

    def remove_edge(self, u, v):
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        self.adj[u] = [(nei,w) for (nei,w) in self.adj[u] if nei != v]
        if not self.directed:
            self.adj[v] = [(nei,w) for (nei,w) in self.adj[v] if nei != u] 

    # -------------------
    # UTILIDADES
    # -------------------
    def __repr__(self):
        return f"WeightedGraph(directed={self.directed}, nodes={len(self.adj)}, edges={len(self.get_edges())})" 

    # reconstruir camino a partir de diccionario prev (usado por Dijkstra/Bellman-Ford)
    @staticmethod
    def reconstruct_path(prev, start, goal):
        if start == goal:
            return [start]
        if prev.get(goal) is None:
            return None
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            if cur == start:
                break
            cur = prev[cur]
        path.reverse()
        return path if path[0] == start else None 

    # -------------------
    # ALGORITMOS DE CAMINOS
    # -------------------
    def dijkstra(self, start):
        """
        Dijkstra: caminos mínimos desde start (requiere pesos >= 0).
        Retorna (dist, prev) dicts.
        Complejidad: O(E log V)
        """
        if start not in self.adj:
            raise KeyError("Start node not found")
        dist = {u: float('inf') for u in self.adj}
        prev = {u: None for u in self.adj}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d,u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v,w in self.adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev 

    def bellman_ford(self, start):
        """
        Bellman-Ford: caminos mínimos con posibilidad de pesos negativos.
        Devuelve (dist, prev). Lanza ValueError si hay ciclo negativo alcanzable.
        Complejidad: O(V * E)
        Nota: en grafos no dirigidos, aristas negativas pueden crear ciclo negativo trivial.
        """
        if start not in self.adj:
            raise KeyError("Start node not found")
        nodes = list(self.adj.keys())
        dist = {u: float('inf') for u in nodes}
        prev = {u: None for u in nodes}
        dist[start] = 0 

        edges = []
        for u in self.adj:
            for v,w in self.adj[u]:
                # en grafo no dirigido, esto incluye ambas direcciones; ok para BF check
                edges.append((u,v,w)) 

        n = len(nodes)
        for _ in range(n-1):
            updated = False
            for u,v,w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    updated = True
            if not updated:
                break 

        # detectar ciclo negativo
        for u,v,w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle")
        return dist, prev 

    def floyd_warshall(self):
        """
        Floyd-Warshall: todas las parejas de caminos más cortos.
        Retorna (dist, next_node) donde next_node[u][v] es el siguiente nodo desde u hacia v.
        Complejidad: O(n^3). Útil para grafos pequeños/medianos.
        """
        nodes = list(self.adj.keys())
        idx = {node:i for i,node in enumerate(nodes)}
        n = len(nodes)
        dist = [[float('inf')]*n for _ in range(n)]
        nxt = [[None]*n for _ in range(n)] 

        for i,node in enumerate(nodes):
            dist[i][i] = 0
            nxt[i][i] = node 

        for u in self.adj:
            i = idx[u]
            for v,w in self.adj[u]:
                j = idx[v]
                dist[i][j] = w
                nxt[i][j] = v 

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        nxt[i][j] = nxt[i][k] 

        # transformar dist y nxt a dicts con claves por nodo
        dist_dict = {u: {} for u in nodes}
        next_dict = {u: {} for u in nodes}
        for i,u in enumerate(nodes):
            for j,v in enumerate(nodes):
                val = dist[i][j]
                dist_dict[u][v] = val
                next_dict[u][v] = nxt[i][j]
        return dist_dict, next_dict 

    # -------------------
    # MST (solo tiene sentido para grafos no dirigidos)
    # -------------------
    class _DSU:
        def __init__(self, items):
            self.parent = {x:x for x in items}
            self.rank = {x:0 for x in items}
        def find(self,x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self,a,b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.rank[ra] < self.rank[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
            return True 

    def kruskal_mst(self):
        """Kruskal: devuelve (mst_edges, total_weight). Solo para grafos no dirigidos."""
        if self.directed:
            raise ValueError("Kruskal MST only for undirected graphs")
        edges = self.get_edges()
        edges_sorted = sorted(edges, key=lambda x: x[2])
        dsu = WeightedGraph._DSU(self.get_nodes())
        mst = []
        total = 0
        for u,v,w in edges_sorted:
            if dsu.union(u,v):
                mst.append((u,v,w))
                total += w
        return mst, total 

    def prim_mst(self, start=None):
        """Prim: devuelve (mst_edges, total_weight). Solo para grafos no dirigidos."""
        if self.directed:
            raise ValueError("Prim MST only for undirected graphs")
        if not self.adj:
            return [], 0
        if start is None:
            start = next(iter(self.adj))
        visited = set([start])
        pq = []
        for v,w in self.adj[start]:
            heapq.heappush(pq, (w, start, v))
        mst = []
        total = 0
        while pq and len(visited) < len(self.adj):
            w,u,v = heapq.heappop(pq)
            if v in visited:
                continue
            visited.add(v)
            mst.append((u,v,w))
            total += w
            for to,wt in self.adj[v]:
                if to not in visited:
                    heapq.heappush(pq, (wt, v, to))
        return mst, total 

        # -------------------
    # Extra: topological shortest path for DAGs (solo si directed=True y DAG)
    # -------------------
    def shortest_paths_in_dag(self, start):
        """
        Si el grafo es dirigido y acíclico (DAG), calcula caminos más cortos desde start
        en O(V + E) usando orden topológico. Lanza ValueError si no es DAG o si graph no dirigido.
        """
        if not self.directed:
            raise ValueError("Method applicable only to directed DAGs")
        # calcular indegrees y Kahn para topological order
        indeg = {u:0 for u in self.adj}
        for u in self.adj:
            for v,w in self.adj[u]:
                indeg[v] = indeg.get(v,0) + 1
        q = deque([u for u in indeg if indeg[u] == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v,w in self.adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        if len(topo) != len(self.adj):
            raise ValueError("Graph is not a DAG (contains cycles)") 

        dist = {u: float('inf') for u in self.adj}
        prev = {u: None for u in self.adj}
        if start not in self.adj:
            raise KeyError("Start node not found")
        dist[start] = 0
        for u in topo:
            if dist[u] != float('inf'):
                for v,w in self.adj[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        prev[v] = u
        return dist, prev 

#Ejemplo de uso (rápido)
if __name__ == "__main__":
    # grafo dirigido con pesos (ejemplo de rutas)
    g = WeightedGraph(directed=True)
    g.add_edge("A","B", 2)
    g.add_edge("A","C", 5)
    g.add_edge("B","C", 1)
    g.add_edge("C","D", 3)
    g.add_edge("B","D", 7) 

    print(g)
    dist, prev = g.dijkstra("A")
    print("Dijkstra dist desde A:", dist)
    print("Camino A->D:", WeightedGraph.reconstruct_path(prev, "A", "D")) 

    # Bellman-Ford (soporta negativos)
    g2 = WeightedGraph(directed=True)
    g2.add_edge(0,1,4)
    g2.add_edge(0,2,5)
    g2.add_edge(1,2,-6)
    g2.add_edge(2,3,2)
    dist2, prev2 = g2.bellman_ford(0)
    print("Bellman-Ford dist:", dist2)
    print("Camino 0->3:", WeightedGraph.reconstruct_path(prev2, 0, 3)) 

    # Floyd-Warshall (todas parejas)
    g3 = WeightedGraph(directed=False)
    g3.add_edge("A","B",3)
    g3.add_edge("B","C",4)
    g3.add_edge("A","C",10)
    dist_all, next_node = g3.floyd_warshall()
    print("Floyd dist A->C:", dist_all["A"]["C"])
    # MST (porque g3 es no dirigido)
    mst, total = g3.kruskal_mst()
    print("MST (Kruskal):", mst, "total:", total)












#Grafo no ponderado. Código: unweighted_graph.py
from collections import deque, defaultdict 

class UnweightedGraph:
    """
    Grafo no ponderado (opción directed).
    Representación: adj: dict[node] -> set(neighbors)
    Nodos pueden ser cualquier hashable (int, str, ...).
    """ 

    def __init__(self, directed: bool = False):
        self.adj = {}         # nodo -> set(vecinos)
        self.directed = directed 

    # -------------------
    # CRUD: NODOS
    # -------------------
    def add_node(self, node):
        """Crear/asegurar existencia del nodo."""
        if node not in self.adj:
            self.adj[node] = set() 

    def get_nodes(self):
        """Listar nodos."""
        return list(self.adj.keys()) 

    def remove_node(self, node):
        """Eliminar nodo y todas sus aristas incidentes."""
        if node not in self.adj:
            raise KeyError(f"Node {node} not found")
        # eliminar aristas hacia node
        for u in list(self.adj.keys()):
            if node in self.adj[u]:
                self.adj[u].remove(node)
        # borrar nodo
        del self.adj[node] 

    # -------------------
    # CRUD: ARISTAS
    # -------------------
    def add_edge(self, u, v):
        """Añadir arista u-v (o u->v si directed=True). Crea nodos si no existen."""
        self.add_node(u)
        self.add_node(v)
        self.adj[u].add(v)
        if not self.directed:
            self.adj[v].add(u) 

    def has_edge(self, u, v) -> bool:
        """True si existe u->v (o u-v en no dirigido)."""
        return u in self.adj and v in self.adj[u] 

    def get_edges(self):
        """Listar aristas. En no dirigido evita duplicados (orden lexicográfico para consistencia)."""
        edges = []
        seen = set()
        for u in self.adj:
            for v in self.adj[u]:
                if self.directed:
                    edges.append((u, v))
                else:
                    key = tuple(sorted((u, v), key=lambda x: str(x)))
                    if key not in seen:
                        edges.append((key[0], key[1]))
                        seen.add(key)
        return edges 

    def remove_edge(self, u, v):
        """Eliminar arista u->v (y v->u si no dirigido)."""
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        if v in self.adj[u]:
            self.adj[u].remove(v)
        if not self.directed:
            if u in self.adj[v]:
                self.adj[v].remove(u) 

    # -------------------
    # ALGORITMOS
    # -------------------
    def bfs(self, start):
        """
        BFS desde start en grafo no ponderado.
        Retorna: (order, dist, prev)
        - order: lista nodos en orden de visita
        - dist: dict nodo -> distancia en número de aristas (inf si no alcanzable)
        - prev: dict para reconstruir caminos (prev[v] = predecessor de v)
        Complejidad: O(V + E)
        """
        if start not in self.adj:
            raise KeyError("Start node not in graph")
        dist = {u: float('inf') for u in self.adj}
        prev = {u: None for u in self.adj}
        order = []
        q = deque([start])
        dist[start] = 0 

        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                if dist[v] == float('inf'):
                    dist[v] = dist[u] + 1
                    prev[v] = u
                    q.append(v)
        return order, dist, prev 

    def shortest_path(self, start, goal):
        """Reconstruye el camino (lista) minimal en número de saltos entre start y goal usando BFS."""
        _, dist, prev = self.bfs(start)
        if dist.get(goal, float('inf')) == float('inf'):
            return None  # no alcanzable
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            if cur == start:
                break
            cur = prev[cur]
        path.reverse()
        return path 

    def dfs(self, start):
        """
        DFS iterativo desde start.
        Retorna orden de visita.
        Complejidad: O(V + E)
        """
        if start not in self.adj:
            raise KeyError("Start node not in graph")
        visited = set()
        stack = [start]
        order = []
        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            order.append(u)
            # agregar vecinos en orden estable (reversed para simular recursivo)
            for v in sorted(self.adj[u], key=lambda x: str(x), reverse=True):
                if v not in visited:
                    stack.append(v)
        return order 

    def connected_components(self):
        """Lista de componentes conectadas (cada componente = lista de nodos). Sólo tiene sentido en grafo no dirigido."""
        if self.directed:
            raise ValueError("Use strongly_connected_components for directed graphs")
        visited = set()
        comps = []
        for node in self.adj:
            if node not in visited:
                comp = []
                q = deque([node])
                visited.add(node)
                while q:
                    u = q.popleft()
                    comp.append(u)
                    for v in self.adj[u]:
                        if v not in visited:
                            visited.add(v)
                            q.append(v)
                comps.append(comp)
        return comps 

    def has_cycle(self):
        """
        Detectar ciclo.
        - Si no dirigido: DFS con parent-check.
        - Si dirigido: DFS con rec_stack (detección clásica).
        Retorna True si hay ciclo.
        """
        visited = set() 

        if not self.directed:
            def dfs(u, parent):
                visited.add(u)
                for v in self.adj[u]:
                    if v == parent:
                        continue
                    if v in visited:
                        return True
                    if dfs(v, u):
                        return True
                return False 

            for node in self.adj:
                if node not in visited:
                    if dfs(node, None):
                        return True
            return False 

        else:
            rec_stack = set()
            def dfs_dir(u):
                visited.add(u)
                rec_stack.add(u)
                for v in self.adj[u]:
                    if v not in visited:
                        if dfs_dir(v):
                            return True
                    elif v in rec_stack:
                        return True
                rec_stack.remove(u)
                return False 

            for node in self.adj:
                if node not in visited:
                    if dfs_dir(node):
                        return True
            return False 

    def is_bipartite(self):
        """
        Comprueba si el grafo es bipartito (2-colorable).
        Retorna (True/False, color_dict)
        color_dict: nodo -> 0/1 si es bipartito, dict vacío si no lo es.
        Sólo sentido en grafos no dirigidos para la interpretación clásica.
        """
        color = {}
        for start in self.adj:
            if start in color:
                continue
            q = deque([start])
            color[start] = 0
            while q:
                u = q.popleft()
                for v in self.adj[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False, {}
        return True, color 

    # -------------------
    # UTILIDADES: DSU (Union-Find) - útil para componentes y detectar ciclos por aristas
    # -------------------
    class _DSU:
        def __init__(self):
            self.parent = {}
            self.rank = {} 

        def make_set(self, x):
            if x not in self.parent:
                self.parent[x] = x
                self.rank[x] = 0 

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x] 

        def union(self, x, y):
            rx, ry = self.find(x), self.find(y)
            if rx == ry:
                return False
            if self.rank[rx] < self.rank[ry]:
                rx, ry = ry, rx
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
            return True 

    def is_tree(self):
        """
        Comprueba si el grafo no dirigido es un árbol:
        - conexo y |E| = |V| - 1
        """
        if self.directed:
            raise ValueError("is_tree defined for undirected graphs only")
        n = len(self.adj)
        m = len(self.get_edges())
        if n == 0:
            return False
        if m != n - 1:
            return False
        # comprobar conectividad
        comps = self.connected_components()
        return len(comps) == 1 

    def __repr__(self):
        return f"UnweightedGraph(directed={self.directed}, nodes={len(self.adj)}, edges={len(self.get_edges())})"

#Ejemplo de uso (archivo example_unweighted.py)
if __name__ == "__main__":
    g = UnweightedGraph(directed=False) 

    # CRUD: nodos y aristas
    g.add_node("A")
    g.add_node("B")
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("E", "F")   # componente separada 

    print(g)               # resumen
    print("Nodos:", g.get_nodes())
    print("Aristas:", g.get_edges()) 

    # BFS: orden, distancias y reconstrucción de camino
    order, dist, prev = g.bfs("A")
    print("BFS desde A orden:", order)
    print("Distancias desde A:", dist)
    print("Camino A -> D:", g.shortest_path("A", "D")) 

    # DFS
    print("DFS desde A:", g.dfs("A")) 

    # Componentes conectadas
    print("Componentes conectadas:", g.connected_components()) 

    # Ciclos
    print("¿Tiene ciclo?", g.has_cycle()) 

    # Bipartito
    print("¿Bipartito?", g.is_bipartite()) 

    # Tree check
    print("¿Es árbol?", g.is_tree()) 

    # Eliminar arista / nodo
    g.remove_edge("C", "D")
    print("Aristas tras remover C-D:", g.get_edges())
    g.remove_node("E")
    print("Nodos tras remover E:", g.get_nodes())







#Grafo conexo. Código — connected_graph.py
from collections import deque
import heapq 

class ConnectedGraph:
    """
    Grafo (principalmente pensado como no dirigido / conexo).
    Representación:
      self.adj: dict[node] -> dict[neighbor] = weight
    Nodos pueden ser hashables (int, str, ...).
    Si trabajas sin pesos, usa weight=1 por defecto.
    """ 

    def __init__(self):
        self.adj = {} 

    # -------------------
    # CRUD: NODOS
    # -------------------
    def add_node(self, u):
        """Crear nodo si no existe."""
        if u not in self.adj:
            self.adj[u] = {} 

    def get_nodes(self):
        return list(self.adj.keys()) 

    def remove_node(self, u):
        """Eliminar nodo y todas las aristas incidentes."""
        if u not in self.adj:
            raise KeyError(f"Node {u} not found")
        for v in list(self.adj[u].keys()):
            # quitar referencia desde v
            if v in self.adj:
                self.adj[v].pop(u, None)
        del self.adj[u] 

    # -------------------
    # CRUD: ARISTAS
    # -------------------
    def add_edge(self, u, v, weight=1):
        """Añade arista no dirigida u-v con peso (por defecto 1). Crea nodos si hace falta."""
        self.add_node(u)
        self.add_node(v)
        self.adj[u][v] = weight
        self.adj[v][u] = weight 

    def update_edge_weight(self, u, v, new_weight):
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        if v not in self.adj[u]:
            raise KeyError(f"Edge {u}-{v} not found")
        self.adj[u][v] = new_weight
        self.adj[v][u] = new_weight 

    def remove_edge(self, u, v):
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        self.adj[u].pop(v, None)
        self.adj[v].pop(u, None) 

    def get_edges(self):
        """Lista de aristas (u, v, weight) con u <= v (por consistencia)."""
        edges = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u].items():
                key = tuple(sorted((u, v), key=lambda x: str(x)))
                if key not in seen:
                    edges.append((key[0], key[1], w))
                    seen.add(key)
        return edges 

    def get_edge_weight(self, u, v):
        return self.adj.get(u, {}).get(v, None) 

    # -------------------
    # BÁSICOS: BFS, DFS, conectividad
    # -------------------
    def bfs(self, start):
        """BFS: devuelve (order, dist, prev). Dist: en número de aristas."""
        if start not in self.adj:
            raise KeyError("Start node not found")
        dist = {u: float('inf') for u in self.adj}
        prev = {u: None for u in self.adj}
        q = deque([start])
        dist[start] = 0
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                if dist[v] == float('inf'):
                    dist[v] = dist[u] + 1
                    prev[v] = u
                    q.append(v)
        return order, dist, prev 

    def dfs(self, start):
        """DFS iterativo: devuelve orden de visita."""
        if start not in self.adj:
            raise KeyError("Start node not found")
        visited = set()
        stack = [start]
        order = []
        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            order.append(u)
            # push vecinos en orden para reproducibilidad
            for v in sorted(self.adj[u], key=lambda x: str(x), reverse=True):
                if v not in visited:
                    stack.append(v)
        return order 

    def is_connected(self):
        """Comprueba si el grafo es conexo (asume grafo no vacío)."""
        if not self.adj:
            return True
        start = next(iter(self.adj))
        _, dist, _ = self.bfs(start)
        return all(d != float('inf') for d in dist.values()) 

    def connected_components(self):
        """Devuelve lista de componentes conectadas (cada una como lista de nodos)."""
        visited = set()
        comps = []
        for node in self.adj:
            if node in visited:
                continue
            comp = []
            q = deque([node])
            visited.add(node)
            while q:
                u = q.popleft()
                comp.append(u)
                for v in self.adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
            comps.append(comp)
        return comps 

    # -------------------
    # PUENTES y PUNTOS DE ARTICULACIÓN (Tarjan)
    # -------------------
    def bridges(self):
        """
        Tarjan para puentes (aristas cuya eliminación incrementa #componentes).
        Retorna lista de (u,v) con u < v (por consistencia).
        Complejidad O(V+E).
        """
        time = 0
        disc = {}
        low = {}
        visited = set()
        res = [] 

        def dfs(u, parent):
            nonlocal time
            visited.add(u)
            disc[u] = low[u] = time
            time += 1
            for v in self.adj[u]:
                if v == parent:
                    continue
                if v not in visited:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        a, b = sorted((u, v), key=lambda x: str(x))
                        res.append((a, b))
                else:
                    low[u] = min(low[u], disc[v]) 

        for node in self.adj:
            if node not in visited:
                dfs(node, None)
        return res 

    def articulation_points(self):
        """
        Tarjan para puntos de articulación (articulation points / cut vertices).
        Retorna un set de nodos cuya eliminación incrementa #componentes.
        Complejidad O(V+E).
        """
        time = 0
        disc = {}
        low = {}
        visited = set()
        ap = set() 

        def dfs(u, parent):
            nonlocal time
            visited.add(u)
            disc[u] = low[u] = time
            time += 1
            children = 0
            for v in self.adj[u]:
                if v == parent:
                    continue
                if v not in visited:
                    children += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    # caso root
                    if parent is None and children > 1:
                        ap.add(u)
                    # caso no-root
                    if parent is not None and low[v] >= disc[u]:
                        ap.add(u)
                else:
                    low[u] = min(low[u], disc[v]) 

        for node in self.adj:
            if node not in visited:
                dfs(node, None)
        return ap 

    # -------------------
    # CAMINOS MÍNIMOS
    # -------------------
    def shortest_path_unweighted(self, start, goal):
        """Camino mínimo en número de aristas (BFS). Devuelve lista de nodos o None."""
        _, dist, prev = self.bfs(start)
        if dist.get(goal, float('inf')) == float('inf'):
            return None
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            if cur == start:
                break
            cur = prev[cur]
        path.reverse()
        return path 

    def dijkstra(self, start):
        """Dijkstra: distancias y prev (usa weights). Complejidad O(E log V)."""
        if start not in self.adj:
            raise KeyError("Start node not found")
        dist = {u: float('inf') for u in self.adj}
        prev = {u: None for u in self.adj}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.adj[u].items():
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev 

    # -------------------
    # MST: Kruskal (solo si el grafo es conexo y hay pesos)
    # -------------------
    class _DSU:
        def __init__(self, items):
            self.parent = {x: x for x in items}
            self.rank = {x: 0 for x in items}
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.rank[ra] < self.rank[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
            return True 

    def kruskal_mst(self):
        """
        Kruskal: devuelve (mst_edges, total_weight).
        Requiere que graph sea conectado para que MST cubra todos los nodos.
        """
        edges = self.get_edges()
        edges_sorted = sorted(edges, key=lambda x: x[2])
        dsu = ConnectedGraph._DSU(self.get_nodes())
        mst = []
        total = 0
        for u, v, w in edges_sorted:
            if dsu.union(u, v):
                mst.append((u, v, w))
                total += w
        return mst, total 

    # -------------------
    # UTILIDADES
    # -------------------
    def __repr__(self):
        return f"ConnectedGraph(nodes={len(self.adj)}, edges={len(self.get_edges())})" 

#Ejemplo de uso (práctico)
if __name__ == "__main__":
    g = ConnectedGraph() 

    # --- CRUD: crear nodos y aristas (con pesos porque usaremos MST y Dijkstra) ---
    g.add_edge("A", "B", weight=4)
    g.add_edge("A", "C", weight=2)
    g.add_edge("B", "C", weight=1)
    g.add_edge("B", "D", weight=5)
    g.add_edge("C", "D", weight=8)
    g.add_edge("C", "E", weight=10)
    g.add_edge("D", "E", weight=2) 

    print(g)
    print("Nodos:", g.get_nodes())
    print("Aristas:", g.get_edges()) 

    # Comprobar conectividad
    print("¿Conexo?", g.is_connected())               # True 

    # BFS/DFS
    order_bfs, dist_bfs, prev_bfs = g.bfs("A")
    print("BFS desde A orden:", order_bfs)
    print("Distancias en saltos desde A:", dist_bfs)
    print("DFS desde A:", g.dfs("A")) 

    # Camino mínimo en saltos (no ponderado)
    print("Camino mínimo (saltos) A -> E:", g.shortest_path_unweighted("A", "E")) 

    # Dijkstra (ponderado)
    dist, prev = g.dijkstra("A")
    print("Dijkstra distancias desde A:", dist)
    # reconstruir camino A->E
    def reconstruct(prev, start, goal):
        if prev[goal] is None and start != goal:
            return None
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            if cur == start:
                break
            cur = prev[cur]
        path.reverse()
        return path
    print("Camino ponderado A -> E:", reconstruct(prev, "A", "E")) 

    # Puentes y puntos de articulación
    print("Puentes:", g.bridges())
    print("Puntos de articulación:", g.articulation_points()) 

    # MST (Kruskal)
    mst, total = g.kruskal_mst()
    print("MST (Kruskal):", mst, "peso total:", total) 

    # Modificaciones (CRUD)
    g.add_node("F")
    g.add_edge("E", "F", weight=3)
    print("Tras añadir F:", g.get_nodes())
    print("¿Conexo ahora?", g.is_connected())







#Grafo completo. Código — complete_graph.py
from collections import deque
import heapq
from itertools import permutations 

class CompleteGraph:
    """
    Grafo (por defecto) completo: al añadir un nodo se conecta con todos los existentes.
    Representación interna:
      - self.nodes: set de nodos
      - self.adj: dict[node] -> dict[neighbor] = weight
        (si una arista no está presente en adj[u], se considera ausente; sin embargo,
        al crear/añadir nodo por defecto se crea arista con weight por defecto)
    directed: si True, las aristas son dirigidas (comportamiento no clásico de 'clique' pero soportado).
    """ 

    def __init__(self, directed: bool = False, default_weight=1):
        self.directed = directed
        self.default_weight = default_weight
        self.nodes = set()
        self.adj = {}  # nodo -> { vecino: peso, ... } 

    # -------------------
    # CRUD: NODOS
    # -------------------
    def add_node(self, u):
        """Añade el nodo y —si ya hay otros nodos— crea aristas entre u y todos los demás con peso por defecto."""
        if u in self.nodes:
            return
        # crear estructura
        self.nodes.add(u)
        self.adj[u] = {}
        # conectar con todos los demás
        for v in list(self.nodes):
            if v == u:
                continue
            # por defecto añadir u-v y (si no dirigido) v-u
            self.adj[u][v] = self.default_weight
            if not self.directed:
                self.adj[v][u] = self.default_weight
            else:
                # en dirigido, también podemos querer la arista inversa por defecto
                self.adj[v].setdefault(u, self.default_weight) 

    def get_nodes(self):
        return list(self.nodes) 

    def remove_node(self, u):
        """Elimina el nodo y todas sus aristas incidentes."""
        if u not in self.nodes:
            raise KeyError(f"Node {u} not found")
        # eliminar referencias en vecinos
        for v in list(self.adj.get(u, {}).keys()):
            if v in self.adj:
                self.adj[v].pop(u, None)
        # eliminar entrada
        self.adj.pop(u, None)
        self.nodes.remove(u) 

    # -------------------
    # CRUD: ARISTAS
    # -------------------
    def add_edge(self, u, v, weight=None):
        """
        Añade/actualiza arista u-v (si u o v no existen, se crean nodos).
        Para grafos no dirigidos asegura ambas direcciones.
        """
        if weight is None:
            weight = self.default_weight
        if u not in self.nodes:
            self.add_node(u)
        if v not in self.nodes:
            self.add_node(v)
        self.adj[u][v] = weight
        if not self.directed:
            self.adj[v][u] = weight 

    def get_edges(self):
        """Devuelve lista de aristas (u, v, weight). Evita duplicados en no dirigido."""
        edges = []
        seen = set()
        for u in self.nodes:
            for v, w in self.adj[u].items():
                if self.directed:
                    edges.append((u, v, w))
                else:
                    key = tuple(sorted((u, v), key=lambda x: str(x)))
                    if key not in seen:
                        edges.append((key[0], key[1], w))
                        seen.add(key)
        return edges 

    def get_edge_weight(self, u, v):
        """Devuelve peso de arista u->v o None si no existe."""
        return self.adj.get(u, {}).get(v, None) 

    def remove_edge(self, u, v):
        """
        Elimina la arista u-v (y v-u si no dirigido). Esto puede convertir el grafo en no completo.
        """
        if u not in self.nodes or v not in self.nodes:
            raise KeyError("One or both nodes not found")
        self.adj[u].pop(v, None)
        if not self.directed:
            self.adj[v].pop(u, None) 

    def update_edge_weight(self, u, v, new_weight):
        """Actualiza peso de arista existente; si no existe, lanza KeyError."""
        if self.get_edge_weight(u, v) is None:
            raise KeyError(f"Edge {u}->{v} not found")
        self.adj[u][v] = new_weight
        if not self.directed:
            self.adj[v][u] = new_weight 

    # -------------------
    # UTILIDADES
    # -------------------
    def is_complete(self):
        """Comprueba si el grafo es completo: cada par distinto tiene arista (en ambas direcciones si no dirigido)."""
        n = len(self.nodes)
        if self.directed:
            # en un grafo dirigido completo habría n*(n-1) aristas (u->v para u!=v)
            total_needed = n * (n - 1)
            return sum(len(self.adj[u]) for u in self.nodes) == total_needed
        else:
            # en no dirigido: n*(n-1)/2 aristas únicas
            total_needed = n * (n - 1) // 2
            return len(self.get_edges()) == total_needed 

    def adjacency_matrix(self):
        """Devuelve matriz de adyacencia (dict de dicts) con 1/0 si existe arista (ignorando pesos)."""
        nodes = sorted(self.nodes, key=lambda x: str(x))
        mat = {u: {v: (1 if v in self.adj[u] else 0) for v in nodes} for u in nodes}
        return mat 

    def degree(self, u):
        """Grado (saliente) de u. En no dirigido es grado clásico."""
        if u not in self.nodes:
            raise KeyError("Node not found")
        return len(self.adj[u]) 

    # -------------------
    # ALGORITMOS CLÁSICOS (adaptados)
    # -------------------
    def bfs(self, start):
        """BFS: orden de visita, dist (saltos), prev. Si faltan aristas, funciona como grafo general."""
        if start not in self.nodes:
            raise KeyError("Start node not found")
        dist = {u: float('inf') for u in self.nodes}
        prev = {u: None for u in self.nodes}
        order = []
        q = deque([start])
        dist[start] = 0
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj.get(u, {}):
                if dist[v] == float('inf'):
                    dist[v] = dist[u] + 1
                    prev[v] = u
                    q.append(v)
        return order, dist, prev 

    def dfs(self, start):
        """DFS iterativo: devuelve orden de visita."""
        if start not in self.nodes:
            raise KeyError("Start node not found")
        visited = set()
        stack = [start]
        order = []
        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            order.append(u)
            # iterar vecinos en orden estable
            for v in sorted(self.adj[u], key=lambda x: str(x), reverse=True):
                if v not in visited:
                    stack.append(v)
        return order 

    def shortest_path(self, start, goal):
        """Camino mínimo en número de saltos (BFS). En grafo completo típicamente es directo u->v."""
        _, dist, prev = self.bfs(start)
        if dist.get(goal, float('inf')) == float('inf'):
            return None
        # reconstruir camino
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            if cur == start:
                break
            cur = prev[cur]
        path.reverse()
        return path 

    def dijkstra(self, start):
        """Dijkstra usando pesos; en grafo completo directo será la arista si existe."""
        if start not in self.nodes:
            raise KeyError("Start node not found")
        dist = {u: float('inf') for u in self.nodes}
        prev = {u: None for u in self.nodes}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.adj[u].items():
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev 

    def any_spanning_tree(self):
        """
        Construye un spanning tree trivial: estrella centrada en un nodo arbitrario.
        Para grafos completos siempre existe y es óptimo como árbol de expansión si se quiere kolay.
        Retorna lista de aristas (u,v,weight).
        """
        if not self.nodes:
            return []
        center = next(iter(self.nodes))
        tree = []
        for v in self.nodes:
            if v == center:
                continue
            w = self.adj[center].get(v, self.default_weight)
            tree.append((center, v, w))
        return tree 

    # -------------------
    # HAMILTONIANAS (específico para grafos completos)
    # -------------------
    def has_hamiltonian_cycle(self):
        """En grafos completos con n >= 3 siempre hay ciclo hamiltoniano."""
        return len(self.nodes) >= 3 

    def count_hamiltonian_cycles_undirected(self):
        """
        Cuenta (aproximadamente) número de ciclos hamiltonianos no dirigidos en una clique K_n:
            (n-1)! / 2
        (devuelve 0 si n < 3)
        """
        n = len(self.nodes)
        if n < 3:
            return 0
        import math
        return math.factorial(n - 1) // 2 

    def generate_hamiltonian_cycle_example(self):
        """
        Genera un ejemplo concreto de ciclo Hamiltoniano (lista de nodos cerrada) usando permutaciones.
        En grafos completos siempre es posible; para n grande no es recomendable generar todas las permutaciones.
        """
        nodes = list(self.nodes)
        n = len(nodes)
        if n < 3:
            return None
        # fijar nodes[0] como inicio para evitar duplicados en no dirigido
        start = nodes[0]
        for perm in permutations(nodes[1:]):
            cycle = [start] + list(perm) + [start]
            return cycle  # devolvemos el primer ciclo encontrado (es válido)
        return None 

    # -------------------
    # REPRESENTACIÓN
    # -------------------
    def __repr__(self):
        return f"CompleteGraph(directed={self.directed}, n={len(self.nodes)}, complete={self.is_complete()})" 

#Ejemplo de uso
if __name__ == "__main__":
    g = CompleteGraph(directed=False, default_weight=1) 

    # CRUD: nodos y aristas
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    print("Nodos:", g.get_nodes())
    print("¿Es completo?", g.is_complete())
    print("Aristas (un ejemplo):", g.get_edges()[:6]) 

    # Actualizar peso de una arista
    g.update_edge_weight("A", "B", 5)
    print("Peso A-B:", g.get_edge_weight("A", "B")) 

    # Eliminar una arista (convierte en no completamente completo)
    g.remove_edge("C", "D")
    print("¿Es completo ahora?", g.is_complete()) 

    # Algoritmos
    print("BFS desde A:", g.bfs("A")[0])
    print("DFS desde A:", g.dfs("A"))
    print("Camino A -> D (mínimo en saltos):", g.shortest_path("A", "D")) 

    # Dijkstra (en grafo completo normalmente el camino mínimo es directo si arista existe)
    dist, prev = g.dijkstra("A")
    print("Dijkstra distancias desde A:", dist) 

    # Spanning tree fácil (estrella)
    print("Spanning tree (estrella):", g.any_spanning_tree()) 

    # Hamiltoniano
    print("¿Tiene ciclo Hamiltoniano?", g.has_hamiltonian_cycle())
    print("Ejemplo ciclo Hamiltoniano:", g.generate_hamiltonian_cycle_example())
    print("Número teórico de ciclos Hamiltonianos (K_n):", g.count_hamiltonian_cycles_undirected())










#Grafo ciclico. BipartiteGraph
from collections import deque, defaultdict 

class CyclicGraph:
    """
    Grafo para trabajar con ciclos. Puede ser dirigido o no dirigido.
    Representación: adj: dict[node] -> set(neighbor)
    Nodos: cualquier hashable (int, str, ...)
    """ 

    def __init__(self, directed: bool = False):
        self.adj = {}
        self.directed = directed 

    # -------------------
    # CRUD nodos/aristas
    # -------------------
    def add_node(self, u):
        if u not in self.adj:
            self.adj[u] = set() 

    def get_nodes(self):
        return list(self.adj.keys()) 

    def remove_node(self, u):
        if u not in self.adj:
            raise KeyError("Node not found")
        # eliminar aristas incidentes
        for v in list(self.adj.keys()):
            if u in self.adj[v]:
                self.adj[v].remove(u)
        del self.adj[u] 

    def add_edge(self, u, v):
        """Añade u->v (o arista no dirigida u-v si directed=False)."""
        self.add_node(u); self.add_node(v)
        self.adj[u].add(v)
        if not self.directed:
            self.adj[v].add(u) 

    def has_edge(self, u, v):
        return u in self.adj and v in self.adj[u] 

    def remove_edge(self, u, v):
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        self.adj[u].discard(v)
        if not self.directed:
            self.adj[v].discard(u) 

    def get_edges(self):
        edges = []
        seen = set()
        for u in self.adj:
            for v in self.adj[u]:
                if self.directed:
                    edges.append((u, v))
                else:
                    key = tuple(sorted((u, v), key=lambda x: str(x)))
                    if key not in seen:
                        edges.append(key)
                        seen.add(key)
        return edges 

    
    # -------------------
    # BFS / DFS básicos
    # -------------------
    def bfs(self, start):
        if start not in self.adj:
            raise KeyError("Start node not in graph")
        q = deque([start])
        dist = {start: 0}
        prev = {start: None}
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    prev[v] = u
                    q.append(v)
        return order, dist, prev

    def dfs(self, start):
        if start not in self.adj:
            raise KeyError("Start node not in graph")
        visited = set()
        stack = [start]
        order = []
        while stack:
            u = stack.pop()
            if u in visited: 
                continue
            visited.add(u)
            order.append(u)
            for v in sorted(self.adj[u], key=lambda x: str(x), reverse=True):
                if v not in visited:
                    stack.append(v)
        return order

    # -------------------
    # Detección de ciclos
    # -------------------
    def has_cycle(self):
        """
        Detecta si existe al menos un ciclo.
        - Si directed: DFS con rec_stack
        - Si undirected: DFS con parent-check
        """
        visited = set()

        if self.directed:
            rec_stack = set()
            def dfs(u):
                visited.add(u)
                rec_stack.add(u)
                for v in self.adj[u]:
                    if v not in visited:
                        if dfs(v):
                            return True
                    elif v in rec_stack:
                        return True
                rec_stack.remove(u)
                return False
            for node in self.adj:
                if node not in visited:
                    if dfs(node):
                        return True
            return False
        else:
            def dfs(u, parent):
                visited.add(u)
                for v in self.adj[u]:
                    if v == parent:
                        continue
                    if v in visited:
                        return True
                    if dfs(v, u):
                        return True
                return False
            for node in self.adj:
                if node not in visited:
                    if dfs(node, None):
                        return True
            return False

    def find_one_cycle(self):
        """
        Devuelve una lista con nodos que forman un ciclo encontrado (en orden),
        o None si no existe. Para grafos dirigidos devuelve el ciclo dirigido.
        Implementación basada en DFS y parent tracking.
        """
        if self.directed:
            visited = set()
            parent = {}
            rec_stack = []

            def dfs(u):
                visited.add(u)
                rec_stack.append(u)
                for v in self.adj[u]:
                    if v not in visited:
                        parent[v] = u
                        found = dfs(v)
                        if found:
                            return found
                    elif v in rec_stack:
                        # ciclo desde v hasta u en rec_stack
                        idx = rec_stack.index(v)
                        return rec_stack[idx:] + [v]  # cerrar ciclo
                rec_stack.pop()
                return None

            for s in self.adj:
                if s not in visited:
                    parent[s] = None
                    cyc = dfs(s)
                    if cyc:
                        return cyc
            return None

        else:
            visited = set()
            parent = {}

            def dfs(u, p):
                visited.add(u)
                parent[u] = p
                for v in self.adj[u]:
                    if v == p:
                        continue
                    if v not in visited:
                        cyc = dfs(v, u)
                        if cyc:
                            return cyc
                    else:
                        # found back edge u-v (v visited and v != parent) -> build cycle
                        path = [v, u]
                        cur = u
                        while parent[cur] is not None and parent[cur] != v:
                            cur = parent[cur]
                            path.append(cur)
                        path.append(v)
                        return path[::-1]
                return None

            for node in self.adj:
                if node not in visited:
                    cyc = dfs(node, None)
                    if cyc:
                        return cyc
            return None

    # -------------------
    # Enumerar ciclos simples (limitar longitud por seguridad)
    # -------------------
    def enumerate_simple_cycles(self, max_length=8):
        """
        Genera ciclos simples (sin repetir nodos) hasta max_length.
        WARNING: exponencial en número de ciclos; usar max_length pequeño.
        Retorna lista de ciclos (cada ciclo es lista cerrada: ... start).
        """
        cycles = set()
        path = []

        def backtrack(start, u, visited):
            if len(path) > max_length:
                return
            for v in self.adj[u]:
                if v == start and len(path) >= 2:
                    cyc = tuple(path + [start])
                    # normalizar rotación para evitar duplicados (dir undirected care)
                    norm = self._normalize_cycle(cyc)
                    cycles.add(norm)
                elif v not in visited and v > start:  # pruning to avoid duplicates (lexicographic)
                    visited.add(v)
                    path.append(v)
                    backtrack(start, v, visited)
                    path.pop()
                    visited.remove(v)

        nodes = sorted(self.adj.keys(), key=lambda x: str(x))
        for i, start in enumerate(nodes):
            path = [start]
            backtrack(start, start, set([start]))

        # reconstruir listas desde tuples
        return [list(c) for c in cycles]

    def _normalize_cycle(self, cyc):
        """
        Normaliza un ciclo (tuple) para compararlo: rota hasta obtener la mínima tupla lexicográfica
        y si es dirigido, mantener orientación.
        """
        n = len(cyc) - 1  # last equals first
        best = None
        for r in range(n):
            rot = tuple(cyc[r:r+n] + cyc[r:r+1])
            if best is None or rot < best:
                best = rot
        return best

    # -------------------
    # Utilidades
    # -------------------
    def __repr__(self):
        return f"CyclicGraph(directed={self.directed}, nodes={len(self.adj)}, edges={len(self.get_edges())})"

#Ejemplo de uso CyclicGraph
if __name__ == "__main__":
    g = CyclicGraph(directed=False)
    # CRUD
    g.add_edge("A","B")
    g.add_edge("B","C")
    g.add_edge("C","D")
    g.add_edge("D","A")  # ahora hay ciclo A-B-C-D-A
    g.add_edge("C","E")  # rama

    print(g)
    print("Nodos:", g.get_nodes())
    print("Aristas:", g.get_edges())

    # Detección de ciclo
    print("¿Tiene ciclo?", g.has_cycle())
    print("Un ciclo encontrado:", g.find_one_cycle())

    # Enumerar ciclos simples (limitar longitud)
    ciclos = g.enumerate_simple_cycles(max_length=6)
    print("Ciclos simples (limitados):", ciclos)

#Ejemplo de uso
if __name__ == "__main__":
    g = CyclicGraph(directed=False)
    # CRUD
    g.add_edge("A","B")
    g.add_edge("B","C")
    g.add_edge("C","D")
    g.add_edge("D","A")  # ahora hay ciclo A-B-C-D-A
    g.add_edge("C","E")  # rama

    print(g)
    print("Nodos:", g.get_nodes())
    print("Aristas:", g.get_edges())

    # Detección de ciclo
    print("¿Tiene ciclo?", g.has_cycle())
    print("Un ciclo encontrado:", g.find_one_cycle())

    # Enumerar ciclos simples (limitar longitud)
    ciclos = g.enumerate_simple_cycles(max_length=6)
    print("Ciclos simples (limitados):", ciclos)