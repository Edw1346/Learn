#Eucilidiano. Código — euclidean_graph.py
import math
import heapq
from collections import deque
from typing import Any, Dict, List, Tuple, Optional, Set

Point = Tuple[float, float]
Edge = Tuple[Any, Any, float]  # (u, v, weight)

def euclid(a: Point, b: Point) -> float:
    dx = a[0] - b[0]; dy = a[1] - b[1]
    return math.hypot(dx, dy)

class EuclideanGraph:
    """
    Grafo Euclidiano:
      - nodes: dict[node_id] -> (x, y)
      - adj: dict[node_id] -> dict[neighbor_id] = weight (euclidean distance)
    Puedes construir el grafo de distintas formas: complete graph, k-NN, radius graph, o manual.
    """

    def __init__(self, directed: bool = False):
        self.directed = directed
        self.nodes: Dict[Any, Point] = {}
        self.adj: Dict[Any, Dict[Any, float]] = {}  # peso (distancia)
    
    # -------------------
    # CRUD NODOS
    # -------------------
    def add_node(self, node_id: Any, x: float, y: float) -> None:
        """Añade nodo con coordenadas (x,y). Si existe, actualiza coordenadas (y marca invalida el adjacency)."""
        self.nodes[node_id] = (float(x), float(y))
        if node_id not in self.adj:
            self.adj[node_id] = {}
        else:
            # si cambiaron coordenadas, aristas previas pueden quedar inconsistentes;
            # dejamos las aristas pero el usuario puede reconstruir grafo si lo desea.
            pass

    def get_nodes(self) -> List[Any]:
        return list(self.nodes.keys())

    def remove_node(self, node_id: Any) -> None:
        if node_id not in self.nodes:
            raise KeyError("Node not found")
        del self.nodes[node_id]
        # eliminar aristas incidentes
        self.adj.pop(node_id, None)
        for u in list(self.adj.keys()):
            self.adj[u].pop(node_id, None)

    # -------------------
    # CRUD ARISTAS (manual)
    # -------------------
    def add_edge(self, u: Any, v: Any, weight: Optional[float] = None) -> None:
        """
        Añade arista u->v con peso dado o con la distancia euclidiana si weight=None.
        Si no dirigido, añade v->u con mismo peso.
        """
        if u not in self.nodes or v not in self.nodes:
            raise KeyError("Both nodes must exist")
        if weight is None:
            weight = euclid(self.nodes[u], self.nodes[v])
        self.adj.setdefault(u, {})[v] = float(weight)
        if not self.directed:
            self.adj.setdefault(v, {})[u] = float(weight)

    def remove_edge(self, u: Any, v: Any) -> None:
        if u not in self.adj:
            raise KeyError("Node not found")
        self.adj[u].pop(v, None)
        if not self.directed:
            self.adj.get(v, {}).pop(u, None)

    def get_edges(self) -> List[Edge]:
        edges: List[Edge] = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u].items():
                if self.directed:
                    edges.append((u, v, w))
                else:
                    key = tuple(sorted((u, v), key=lambda x: str(x)))
                    if key in seen:
                        continue
                    seen.add(key)
                    edges.append((key[0], key[1], w))
        return edges

    # -------------------
    # CONSTRUCTORS: complete, k-NN, radius
    # -------------------
    def build_complete(self, symmetric: bool = True) -> None:
        """Construye grafo completo (nodo conectado a todos) con pesos = distancia euclidiana."""
        self.adj = {u: {} for u in self.nodes}
        ids = list(self.nodes.keys())
        n = len(ids)
        for i in range(n):
            for j in range(i+1, n):
                u, v = ids[i], ids[j]
                d = euclid(self.nodes[u], self.nodes[v])
                self.adj[u][v] = d
                if symmetric:
                    self.adj[v][u] = d
        if self.directed and not symmetric:
            # if directed keep only u->v for i<j (this is rare), but keep consistent
            pass

    def build_knn(self, k: int = 5, symmetric: bool = True) -> None:
        """
        Construye k-Nearest Neighbors graph: para cada nodo conecta a sus k vecinos más cercanos.
        Si symmetric=True, garantiza que la arista sea bidireccional si cualquiera lo considera vecino (mutual).
        """
        if k <= 0:
            raise ValueError("k must be >= 1")
        ids = list(self.nodes.keys())
        n = len(ids)
        # calcular distancia completa O(n^2)
        neighbors = {u: [] for u in ids}
        for i in range(n):
            for j in range(n):
                if i == j: continue
                u, v = ids[i], ids[j]
                d = euclid(self.nodes[u], self.nodes[v])
                neighbors[u].append((d, v))
        # escoger k más cercanos
        self.adj = {u: {} for u in ids}
        for u in ids:
            neighbors[u].sort(key=lambda x: x[0])
            for t in neighbors[u][:min(k, len(neighbors[u]))]:
                d, v = t
                self.adj[u][v] = d
                if symmetric:
                    # add symmetric edge
                    self.adj[v].setdefault(u, d)
        # si symmetric=False, el grafo puede quedar dirigido

    def build_radius(self, r: float, symmetric: bool = True) -> None:
        """Conecta todos los pares con distancia <= r."""
        if r < 0:
            raise ValueError("radius must be non-negative")
        self.adj = {u: {} for u in self.nodes}
        ids = list(self.nodes.keys())
        n = len(ids)
        for i in range(n):
            for j in range(i+1, n):
                u, v = ids[i], ids[j]
                d = euclid(self.nodes[u], self.nodes[v])
                if d <= r:
                    self.adj[u][v] = d
                    if symmetric:
                        self.adj[v][u] = d

    # -------------------
    # ALGORITMOS: Dijkstra (heap)
    # -------------------
    def dijkstra(self, source: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
        if source not in self.nodes:
            raise KeyError("Source node not found")
        dist = {u: float('inf') for u in self.nodes}
        prev: Dict[Any, Optional[Any]] = {u: None for u in self.nodes}
        dist[source] = 0.0
        pq = [(0.0, source)]
        while pq:
            d,u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v,w in self.adj.get(u, {}).items():
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev

    # -------------------
    # MST: Kruskal (usa todas las aristas si grafo completo) O(E log E)
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

    def kruskal_mst(self) -> Tuple[List[Edge], float]:
        """Construye MST (lista de aristas y peso total). Considera las aristas presentes en self.adj."""
        edges = self.get_edges()
        # Si el grafo es parcial, edges viene de adj; si quieres MST del grafo completo, usa build_complete() antes.
        edges_sorted = sorted(edges, key=lambda x: x[2])
        dsu = EuclideanGraph._DSU()
        for u in self.nodes:
            dsu.make_set(u)
        mst = []
        total = 0.0
        for u,v,w in edges_sorted:
            if dsu.union(u, v):
                mst.append((u,v,w))
                total += w
            if len(mst) == max(0, len(self.nodes) - 1):
                break
        return mst, total

    # -------------------
    # TSP heuristics: nearest-neighbor + 2-opt improvement
    # -------------------
    def tsp_nearest_neighbor(self, start: Optional[Any] = None) -> List[Any]:
        """Heurística greedy: empieza en start (o cualquiera) y siempre va al vecino no visitado más cercano."""
        if not self.nodes:
            return []
        ids = list(self.nodes.keys())
        if start is None:
            start = ids[0]
        tour = [start]
        visited = {start}
        cur = start
        while len(visited) < len(self.nodes):
            # escoger vecino más cercano entre nodos no visitados (usar distancia euclidiana directo)
            best = None
            bestd = float('inf')
            for v in self.nodes:
                if v in visited:
                    continue
                d = euclid(self.nodes[cur], self.nodes[v])
                if d < bestd:
                    bestd = d; best = v
            tour.append(best)
            visited.add(best)
            cur = best
        return tour

    def tsp_2opt(self, tour: List[Any]) -> List[Any]:
        """2-opt local improvement over tour (lista de nodos). Retorna tour mejorado (no cerrada)."""
        if not tour:
            return tour
        n = len(tour)
        improved = True
        def tour_length(t):
            s = 0.0
            for i in range(n-1):
                s += euclid(self.nodes[t[i]], self.nodes[t[i+1]])
            s += euclid(self.nodes[t[-1]], self.nodes[t[0]])  # close
            return s
        while improved:
            improved = False
            for i in range(1, n-1):
                for j in range(i+1, n):
                    a, b = tour[i-1], tour[i]
                    c, d = tour[j], tour[(j+1) % n]
                    # current edges: a-b and c-d ; swapped: a-c and b-d
                    delta = (euclid(self.nodes[a], self.nodes[c]) + euclid(self.nodes[b], self.nodes[d])- euclid(self.nodes[a], self.nodes[b]) - euclid(self.nodes[c], self.nodes[d]))
                    if delta < -1e-9:
                        # perform 2-opt: reverse segment [i..j]
                        tour[i:j+1] = reversed(tour[i:j+1])
                        improved = True
            # loop until no improvement
        return tour

    # -------------------
    # UTILIDADES
    # -------------------
    def nearest_neighbor_global(self) -> Tuple[Any, float]:
        """Devuelve (node, dist) del punto más cercano a otro punto (par de vecinos más cercanos)."""
        best = None
        bestd = float('inf')
        ids = list(self.nodes.keys())
        n = len(ids)
        for i in range(n):
            for j in range(i+1, n):
                u, v = ids[i], ids[j]
                d = euclid(self.nodes[u], self.nodes[v])
                if d < bestd:
                    bestd = d; best = (u, v)
        return best, bestd

    def neighbors_of(self, u: Any) -> Dict[Any, float]:
        """Devuelve diccionario de vecinos y distancias (según adj actual)."""
        return dict(self.adj.get(u, {}))

    def __repr__(self) -> str:
        return f"EuclideanGraph(V={len(self.nodes)}, E={len(self.get_edges())}, directed={self.directed})"

#Ejemplo de uso
if __name__ == "__main__":
    G = EuclideanGraph(directed=False)

    # CRUD: añadir nodos (id puede ser número o string)
    G.add_node("A", 0.0, 0.0)
    G.add_node("B", 1.0, 0.0)
    G.add_node("C", 1.0, 1.0)
    G.add_node("D", 0.0, 1.0)
    G.add_node("E", 0.5, 0.5)

    # Construir k-NN graph (k=2)
    G.build_knn(k=2, symmetric=True)
    print(G)
    print("Aristas (k-NN):", G.get_edges())

    # Caminos: Dijkstra desde A
    dist, prev = G.dijkstra("A")
    print("Distancias desde A:", dist)
    # reconstruir camino A->C
    def reconstruct(prev, s, t):
        if prev[t] is None and s != t: return None
        path = []
        cur = t
        while cur is not None:
            path.append(cur)
            if cur == s: break
            cur = prev[cur]
        return list(reversed(path))
    print("Camino A->C:", reconstruct(prev, "A", "C"))

    # MST: primero construye grafo completo si quieres MST sobre todos los pares
    G.build_complete()
    mst, total = G.kruskal_mst()
    print("MST (kruskal sobre grafo completo):", mst, "peso total:", total)

    # TSP heurística
    tour = G.tsp_nearest_neighbor(start="A")
    print("TSP NN tour:", tour)
    tour2 = G.tsp_2opt(tour)
    print("TSP 2-opt improved:", tour2)

    # Par de puntos más cercanos global
    pair, d = G.nearest_neighbor_global()
    print("Par más cercano:", pair, "dist:", d)















#Simple
# simple_graph.py
from collections import deque
import heapq
from typing import Any, Dict, List, Optional, Tuple, Set

INF = float('inf')

class SimpleGraph:
    """
    Grafo simple: sin lazos ni aristas paralelas.
    - directed: True -> aristas dirigidas u->v
    - weighted: True -> aristas llevan peso (float). Si weighted=False se trata como no ponderado.
    Representación interna: adj[u] = {v: weight} (weight = 1.0 si no ponderado)
    """

    def __init__(self, directed: bool = False, weighted: bool = False):
        self.directed = directed
        self.weighted = weighted
        self.adj: Dict[Any, Dict[Any, float]] = {}  # adjacency map

    # -------------------
    # CRUD NODOS
    # -------------------
    def add_node(self, u: Any) -> None:
        if u not in self.adj:
            self.adj[u] = {}

    def get_nodes(self) -> List[Any]:
        return list(self.adj.keys())

    def remove_node(self, u: Any) -> None:
        if u not in self.adj:
            raise KeyError("Node not found")
        # eliminar aristas entrantes
        for v in list(self.adj.keys()):
            self.adj[v].pop(u, None)
        # eliminar el nodo
        del self.adj[u]

    # -------------------
    # CRUD ARISTAS
    # -------------------
    def add_edge(self, u: Any, v: Any, weight: Optional[float] = None) -> None:
        """
        Añade arista u->v (o u-v si no dirigido).
        - No permite lazos (u==v) ni aristas paralelas (si ya existe se actualiza el peso).
        - Si weighted==False se ignora `weight` y se usa 1.0.
        """
        if u == v:
            raise ValueError("SimpleGraph does not allow self-loops")
        self.add_node(u); self.add_node(v)
        if not self.weighted:
            w = 1.0
        else:
            if weight is None:
                raise ValueError("Weighted graph requires weight for edges")
            w = float(weight)
        # evitar paralelelas: simplemente sustituir si existe (actualiza peso)
        self.adj[u][v] = w
        if not self.directed:
            self.adj[v][u] = w

    def has_edge(self, u: Any, v: Any) -> bool:
        return u in self.adj and v in self.adj[u]

    def remove_edge(self, u: Any, v: Any) -> None:
        if u not in self.adj:
            raise KeyError("Node not found")
        self.adj[u].pop(v, None)
        if not self.directed:
            self.adj[v].pop(u, None)

    def get_edges(self) -> List[Tuple[Any, Any, float]]:
        """Devuelve lista de aristas. En no dirigido devuelve cada arista una sola vez."""
        edges = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u].items():
                if self.directed:
                    edges.append((u, v, w))
                else:
                    key = tuple(sorted((u, v), key=lambda x: str(x)))
                    if key in seen:
                        continue
                    seen.add(key)
                    edges.append((key[0], key[1], w))
        return edges

    # -------------------
    # RECORRIDOS: BFS / DFS
    # -------------------
    def bfs(self, start: Any) -> Tuple[List[Any], Dict[Any,int], Dict[Any,Optional[Any]]]:
        """BFS (distancias en saltos)."""
        if start not in self.adj:
            raise KeyError("Start node not in graph")
        dist = {u: -1 for u in self.adj}
        prev = {u: None for u in self.adj}
        q = deque([start])
        dist[start] = 0
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    prev[v] = u
                    q.append(v)
        return order, dist, prev

    def dfs(self, start: Any) -> List[Any]:
        """DFS iterativo (pre-order)."""
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
            # empujar vecinos en orden estable para reproducibilidad
            for v in sorted(self.adj[u], key=lambda x: str(x), reverse=True):
                if v not in visited:
                    stack.append(v)
        return order

    # -------------------
    # CAMINO MÁS CORTO (no ponderado: BFS, ponderado: Dijkstra)
    # -------------------
    def shortest_path_unweighted(self, start: Any, goal: Any) -> Optional[List[Any]]:
        """Camino mínimo en número de aristas (BFS)."""
        if start not in self.adj or goal not in self.adj:
            raise KeyError("Start or goal not in graph")
        _, dist, prev = self.bfs(start)
        if dist[goal] == -1:
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

    def dijkstra(self, source: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
        """Dijkstra con heap; requiere weighted=True si quieres pesos reales."""
        if source not in self.adj:
            raise KeyError("Source not in graph")
        dist = {u: INF for u in self.adj}
        prev = {u: None for u in self.adj}
        dist[source] = 0.0
        pq = [(0.0, source)]
        while pq:
            d,u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v,w in self.adj[u].items():
                weight = w if self.weighted else 1.0
                nd = d + weight
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev

    # -------------------
    # CONECTIVIDAD / COMPONENTES / IS_TREE
    # -------------------
    def connected_components(self) -> List[List[Any]]:
        """Componentes conectadas (para directed devuelve componentes débilmente conectadas)."""
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
                if self.directed:
                    # seguir aristas entrantes para weak connectivity
                    for x in self.adj:
                        for y in self.adj[x]:
                            if y == u and x not in visited:
                                visited.add(x)
                                q.append(x)
            comps.append(comp)
        return comps

    def is_connected(self) -> bool:
        if not self.adj:
            return True
        return len(self.connected_components()) == 1

    def is_tree(self) -> bool:
        """Sólo válido para grafos no dirigidos: árbol <=> conexo y |E| = |V| - 1"""
        if self.directed:
            raise ValueError("is_tree is defined for undirected graphs only")
        n = len(self.adj)
        m = len(self.get_edges())
        return self.is_connected() and m == max(0, n - 1)

    # -------------------
    # DETECCIÓN DE CICLOS
    # -------------------
    def has_cycle(self) -> bool:
        """Detecta si existe al menos un ciclo. Dirigido: DFS con recursion stack; no dirigido: DFS con parent check."""
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
            def dfs(u, p):
                visited.add(u)
                for v in self.adj[u]:
                    if v == p:
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

    # -------------------
    # BIPARTITO
    # -------------------
    def is_bipartite(self) -> Tuple[bool, Optional[Tuple[Set[Any], Set[Any]]]]:
        """Comprueba 2-colorabilidad (solo definido para grafos no dirigidos conceptualmente)."""
        color: Dict[Any,int] = {}
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
                        return False, None
        left = {u for u,c in color.items() if c == 0}
        right = {u for u,c in color.items() if c == 1}
        return True, (left, right)

    # -------------------
    # MST (Kruskal) - solo para no dirigido y weighted=True
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

    def kruskal_mst(self) -> Tuple[List[Tuple[Any, Any, float]], float]:
        """Devuelve (mst_edges, total_weight). Requiere undirected y weighted."""
        if self.directed:
            raise ValueError("Kruskal MST only for undirected graphs")
        if not self.weighted:
            raise ValueError("Kruskal requires weighted=True")
        edges = self.get_edges()
        edges_sorted = sorted(edges, key=lambda x: x[2])
        dsu = SimpleGraph._DSU()
        for u in self.adj:
            dsu.make_set(u)
        mst = []
        total = 0.0
        for u,v,w in edges_sorted:
            if dsu.union(u, v):
                mst.append((u, v, w))
                total += w
            if len(mst) == max(0, len(self.adj) - 1):
                break
        return mst, total

    # -------------------
    # UTIL
    # -------------------
    def degree(self, u: Any) -> int:
        if u not in self.adj:
            raise KeyError("Node not found")
        return len(self.adj[u])

    def __repr__(self):
        return f"SimpleGraph(directed={self.directed}, weighted={self.weighted}, V={len(self.adj)}, E={len(self.get_edges())})"

# -------------------
# EJEMPLO DE USO
# -------------------
if __name__ == "__main__":
    # grafo simple no dirigido no ponderado
    g = SimpleGraph(directed=False, weighted=False)
    g.add_edge("A","B")
    g.add_edge("B","C")
    g.add_edge("C","D")
    g.add_edge("D","A")   # forma ciclo A-B-C-D-A
    g.add_edge("C","E")
    print(g)
    print("Nodos:", g.get_nodes())
    print("Aristas:", g.get_edges())
    print("BFS desde A:", g.bfs("A")[0])
    print("DFS desde A:", g.dfs("A"))
    print("¿Tiene ciclo?", g.has_cycle())
    print("¿Es bipartito?", g.is_bipartite())

    # camino no ponderado A -> E
    print("Camino A->E (unweighted):", g.shortest_path_unweighted("A","E"))

    # grafo ponderado (undirected)
    gw = SimpleGraph(directed=False, weighted=True)
    gw.add_edge("A","B", 2.0)
    gw.add_edge("B","C", 1.5)
    gw.add_edge("A","C", 4.0)
    print(gw)
    dist, prev = gw.dijkstra("A")
    print("Dijkstra dist desde A:", dist)
    mst, total = gw.kruskal_mst()
    print("MST (Kruskal):", mst, "peso total:", total)













#Grafos de flujo. Código — flow_graph.py
from collections import deque
from typing import Any, Dict, List, Optional, Tuple

class FlowEdge:
    __slots__ = ("to","rev","cap","flow")
    def __init__(self, to: Any, rev: int, cap: float):
        self.to = to          # destination node
        self.rev = rev        # index of reverse edge in adj[to]
        self.cap = float(cap) # capacity
        self.flow = 0.0       # current flow (0 <= flow <= cap)

    def residual_capacity(self) -> float:
        return self.cap - self.flow

    def __repr__(self):
        return f"Edge(to={self.to}, cap={self.cap}, flow={self.flow}, rev={self.rev})"

class FlowGraph:
    """
    Grafo de flujo dirigido con capacidades no negativas.
    Representación: adj: dict[node] -> list[FlowEdge]
    CRUD:
      - add_node(node)
      - add_edge(u, v, cap)  # directed u -> v with capacity cap (creates residual edge v->u)
      - remove_edge(u,v)     # removes all direct edges u->v (and their residuals)
      - remove_node(node)    # removes node and incident edges
      - get_nodes(), get_edges()
    Algoritmos:
      - max_flow_edmonds_karp(s, t)
      - max_flow_dinic(s, t)
      - min_cut(s, t)  # after running any max-flow (returns (S_set, T_set))
      - flow_decomposition(s, t)  # returns list of (path, flow_value) using current flows
    Nota: después de ejecutar max_flow, las aristas almacenan 'flow'.
    """

    def __init__(self):
        self.adj: Dict[Any, List[FlowEdge]] = {}

    # -------------------
    # CRUD NODOS / ARISTAS
    # -------------------
    def add_node(self, u: Any) -> None:
        if u not in self.adj:
            self.adj[u] = []

    def get_nodes(self) -> List[Any]:
        return list(self.adj.keys())

    def add_edge(self, u: Any, v: Any, cap: float) -> None:
        """
        Añade arista dirigida u -> v con capacidad cap >= 0.
        Crea nodo si no existe.
        Añade también arista residual v -> u con capacidad 0 (y rev indices correctos).
        """
        if cap < 0:
            raise ValueError("Capacity must be non-negative")
        self.add_node(u); self.add_node(v)
        # forward edge index will be len(self.adj[u])
        fwd = FlowEdge(v, len(self.adj[v]), cap)
        bwd = FlowEdge(u, len(self.adj[u]), 0.0)
        self.adj[u].append(fwd)
        self.adj[v].append(bwd)

    def remove_edge(self, u: Any, v: Any) -> None:
        """
        Elimina todas las aristas directas u->v (y sus correspondientes edges residuales)
        Nota: reindexar rev es costoso; implementamos simplificación: reconstruir listas de adyacencia
        eliminando aristas entre u<->v y luego recomputar rev indices globalmente.
        """
        if u not in self.adj or v not in self.adj:
            return
        # eliminar cualquier edge con to==v en adj[u] and to==u in adj[v] that share mirroring is complicated
        # Simplificamos: reconstruimos la estructura entera sin las aristas directas u->v (cap>0 or any)
        edges_to_keep = []
        for a in self.adj:
            for e in self.adj[a]:
                edges_to_keep.append((a, e.to, e.cap, e.flow))
        # filter out edges that are u->v (direct edge) or the residual v->u with cap == 0 initially
        new_edges = [(a,b,c,f) for (a,b,c,f) in edges_to_keep if not (a==u and b==v)]
        # rebuild graph from scratch (flows reset)
        self.adj = {}
        for a,b,c,f in new_edges:
            self.add_edge(a,b,c)
        # flows lost; this is simplest and consistent

    def remove_node(self, node: Any) -> None:
        if node not in self.adj:
            return
        # remove node and any edge incident to it by rebuilding edges that don't touch node
        edges_to_keep = []
        for a in self.adj:
            for e in self.adj[a]:
                if a == node or e.to == node:
                    continue
                edges_to_keep.append((a, e.to, e.cap))
        self.adj = {}
        for a,b,c in edges_to_keep:
            self.add_edge(a,b,c)

    def get_edges(self) -> List[Tuple[Any, Any, float, float]]:
        """Devuelve lista de (u, v, capacity, flow) para aristas con capacity>0 (forward edges)"""
        edges = []
        for u in self.adj:
            for e in self.adj[u]:
                # convention: forward edges are those that originally had cap > 0.
                if e.cap > 0:
                    edges.append((u, e.to, e.cap, e.flow))
        return edges

    # -------------------
    # UTIL: reset flows (set flow to 0) keeping capacities
    # -------------------
    def reset_flows(self) -> None:
        for u in self.adj:
            for e in self.adj[u]:
                e.flow = 0.0

    # -------------------
    # Residual graph helpers
    # -------------------
    def _bfs_level(self, s: Any, t: Any, level: Dict[Any,int]) -> bool:
        """BFS para construir level graph (Dinic). Devuelve True si t alcanzable."""
        for node in self.adj:
            level[node] = -1
        q = deque()
        q.append(s)
        level[s] = 0
        while q:
            u = q.popleft()
            for e in self.adj[u]:
                if e.residual_capacity() > 1e-12 and level[e.to] < 0:
                    level[e.to] = level[u] + 1
                    q.append(e.to)
        return level.get(t, -1) >= 0

    def _dfs_blocking(self, u: Any, t: Any, f: float, level: Dict[Any,int], it: Dict[Any,int]) -> float:
        """DFS sobre level graph para Dinic (envía hasta f)."""
        if u == t:
            return f
        edges = self.adj[u]
        i = it.get(u, 0)
        while i < len(edges):
            e = edges[i]
            if e.residual_capacity() > 1e-12 and level.get(e.to, -1) == level[u] + 1:
                # intentar empujar
                pushed = self._dfs_blocking(e.to, t, min(f, e.residual_capacity()), level, it)
                if pushed > 0:
                    e.flow += pushed
                    # acceso a reverse edge
                    rev_edge = self.adj[e.to][e.rev]
                    rev_edge.flow -= pushed
                    it[u] = i  # actualizar iterador
                    return pushed
            i += 1
        it[u] = i
        return 0.0

    # -------------------
    # Edmonds-Karp (BFS augmenting path) O(E * maxflow) worst-case
    # -------------------
    def max_flow_edmonds_karp(self, s: Any, t: Any) -> float:
        if s not in self.adj or t not in self.adj:
            raise KeyError("Source or sink not in graph")
        self.reset_flows()
        total_flow = 0.0
        while True:
            # BFS to find shortest augmenting path (by edges) and store parent edge reference
            parent = {node: (None, None) for node in self.adj}  # node -> (prev_node, edge_index_in_prev_adj)
            q = deque([s])
            parent[s] = (s, -1)
            found = False
            while q and not found:
                u = q.popleft()
                for idx, e in enumerate(self.adj[u]):
                    if e.residual_capacity() > 1e-12 and parent[e.to][0] is None:
                        parent[e.to] = (u, idx)
                        if e.to == t:
                            found = True
                            break
                        q.append(e.to)
            if not found:
                break
            # compute bottleneck
            path = []
            cur = t
            bottleneck = float('inf')
            while cur != s:
                pu, idx = parent[cur]
                e = self.adj[pu][idx]
                bottleneck = min(bottleneck, e.residual_capacity())
                path.append((pu, idx))
                cur = pu
            # augment
            for pu, idx in reversed(path):
                e = self.adj[pu][idx]
                e.flow += bottleneck
                self.adj[e.to][e.rev].flow -= bottleneck
            total_flow += bottleneck
        return total_flow

    # -------------------
    # Dinic (O(E * sqrt(V)) for unit networks, typically faster in practice)
    # -------------------
    def max_flow_dinic(self, s: Any, t: Any) -> float:
        if s not in self.adj or t not in self.adj:
            raise KeyError("Source or sink not in graph")
        self.reset_flows()
        flow = 0.0
        level: Dict[Any,int] = {}
        while self._bfs_level(s, t, level):
            it: Dict[Any,int] = {node: 0 for node in self.adj}
            pushed = self._dfs_blocking(s, t, float('inf'), level, it)
            while pushed and pushed > 0:
                flow += pushed
                pushed = self._dfs_blocking(s, t, float('inf'), level, it)
        return flow

    # -------------------
    # Min-cut (S,T partition) after running any max-flow algorithm
    # -------------------
    def min_cut(self, s: Any, t: Any) -> Tuple[set, set]:
        """
        Devuelve (S, T) partición donde S son vértices alcanzables desde s en grafo residual.
        Debe llamarse después de ejecutar max_flow_* (o puedes ejecutar BFS sobre residual luego).
        """
        # BFS on residual graph from s following edges with residual_capacity > 0
        visited = set()
        q = deque([s])
        visited.add(s)
        while q:
            u = q.popleft()
            for e in self.adj[u]:
                if e.residual_capacity() > 1e-12 and e.to not in visited:
                    visited.add(e.to)
                    q.append(e.to)
        S = set(visited)
        T = set(self.adj.keys()) - S
        return S, T

    # -------------------
    # Flow decomposition: represent flow as collection of s-t simple paths (and possibly cycles)
    # -------------------
    def flow_decomposition(self, s: Any, t: Any) -> List[Tuple[List[Any], float]]:
        """
        Devuelve lista de (path_list_of_nodes, flow_value) que suman el flujo total,
        usando las aristas con flow>0 (forward flows). Consume los flujos temporalmente (trabaja sobre copia).
        Algoritmo: repetidamente buscar path s->t in graph of edges with flow>0, bottleneck = min flow on path, subtract.
        Complejidad: O(E * #paths) worst-case.
        """
        # Build adjacency of positive-flow edges (mutable copy)
        pos_adj: Dict[Any, List[Tuple[Any, float]]] = {}
        for u in self.adj:
            pos_adj[u] = []
            for e in self.adj[u]:
                # forward edge is one with capacity > 0 originally and flow > 0
                if e.cap > 0 and e.flow > 1e-12:
                    pos_adj[u].append((e.to, e.flow))
        decomposed = []
        # DFS to find any s->t path with positive flow
        def find_path():
            stack = [(s, [s])]
            visited = set([s])
            while stack:
                u, path = stack.pop()
                if u == t:
                    return path
                for v, f in pos_adj.get(u, []):
                    if f > 1e-12 and v not in visited:
                        visited.add(v)
                        stack.append((v, path + [v]))
            return None
        while True:
            path = find_path()
            if path is None:
                break
            # compute bottleneck
            bottleneck = float('inf')
            for i in range(len(path)-1):
                u = path[i]; v = path[i+1]
                # find flow on edge u->v in pos_adj
                for idx, (nei, f) in enumerate(pos_adj[u]):
                    if nei == v:
                        bottleneck = min(bottleneck, f)
                        break
            if bottleneck == float('inf'):
                break
            # subtract bottleneck along path
            for i in range(len(path)-1):
                u = path[i]; v = path[i+1]
                # update pos_adj entry
                for idx, (nei, f) in enumerate(pos_adj[u]):
                    if nei == v:
                        newf = f - bottleneck
                        if newf <= 1e-12:
                            pos_adj[u].pop(idx)
                        else:
                            pos_adj[u][idx] = (nei, newf)
                        break
            decomposed.append((path, bottleneck))
        return decomposed

    # -------------------
    # Representación
    # -------------------
    def __repr__(self) -> str:
        n = len(self.adj)
        e = sum(1 for u in self.adj for ed in self.adj[u] if ed.cap > 0)
        return f"FlowGraph(V={n}, E_forward={e})"

#Ejemplo de uso (completo)
if __name__ == "__main__":
    # Construcción de una red de ejemplo (clásica)
    G = FlowGraph()
    # nodos: s, a, b, c, d, t
    for node in ["s","a","b","c","d","t"]:
        G.add_node(node)

    # Añadir aristas (u, v, capacidad)
    G.add_edge("s", "a", 10)
    G.add_edge("s", "b", 10)
    G.add_edge("a", "c", 4)
    G.add_edge("a", "d", 8)
    G.add_edge("b", "d", 9)
    G.add_edge("c", "t", 10)
    G.add_edge("d", "c", 6)
    G.add_edge("d", "t", 10)

    print("Grafo:", G)
    print("Nodos:", G.get_nodes())
    print("Aristas (u,v,cap,flow):", G.get_edges())

    # Ejecutar Edmonds-Karp
    maxf_ek = G.max_flow_edmonds_karp("s", "t")
    print("\nMax flow (Edmonds-Karp):", maxf_ek)
    print("Aristas tras EK:", G.get_edges())

    # Obtener min-cut (S,T)
    S, T = G.min_cut("s", "t")
    print("Min-cut S:", S, "T:", T)

    # Decomposición del flujo en caminos s->t
    decomp = G.flow_decomposition("s", "t")
    print("Flow decomposition (path,flow):")
    for p, f in decomp:
        print(" ", p, f)

    # Si quieres usar Dinic en vez de Edmonds-Karp:
    # reinicia y añade aristas de nuevo (o reconstruye)
    G2 = FlowGraph()
    for node in ["s","a","b","c","d","t"]:
        G2.add_node(node)
    G2.add_edge("s", "a", 10)
    G2.add_edge("s", "b", 10)
    G2.add_edge("a", "c", 4)
    G2.add_edge("a", "d", 8)
    G2.add_edge("b", "d", 9)
    G2.add_edge("c", "t", 10)
    G2.add_edge("d", "c", 6)
    G2.add_edge("d", "t", 10)

    maxf_dn = G2.max_flow_dinic("s", "t")
    print("\nMax flow (Dinic):", maxf_dn)
    print("Aristas tras Dinic:", G2.get_edges())
















#Grafos de equipados 
# labeled_graph.py
from collections import deque, defaultdict, Counter
import heapq
from typing import Any, Dict, List, Optional, Tuple, Set, Callable

INF = float('inf')

class LabeledGraph:
    """
    Grafo etiquetado (dirigido o no).
    - nodos: adj: dict[node] -> dict[neighbor] -> edge_id
    - edges: edge_id -> (u, v, attrs: dict)
    - node_attrs: node -> dict (etiquetas/atributos arbitrarios)
    - Permite consultas por etiqueta, extracción de subgrafo por etiqueta, recorridos que filtran por etiquetas,
      algoritmos que usan etiquetas (label propagation, Weisfeiler-Lehman relabeling, Dijkstra con coste derivado de etiquetas).
    """

    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj: Dict[Any, Dict[Any, List[int]]] = defaultdict(lambda: defaultdict(list))
        # adj[u][v] = list of edge_ids (so soporta múltiples aristas entre u and v)
        self.node_attrs: Dict[Any, Dict[str, Any]] = {}
        self.edges: Dict[int, Tuple[Any, Any, Dict[str, Any]]] = {}  # id -> (u, v, attrs)
        self._edge_counter = 0

    # -------------------------
    # CRUD: NODOS
    # -------------------------
    def add_node(self, node: Any, attrs: Optional[Dict[str, Any]] = None) -> None:
        """Agregar nodo con atributos (labels) opcionales."""
        if node not in self.node_attrs:
            self.node_attrs[node] = dict(attrs) if attrs else {}
            # ensure adjacency presence
            _ = self.adj[node]
        else:
            # merge/update attrs
            if attrs:
                self.node_attrs[node].update(attrs)

    def get_nodes(self) -> List[Any]:
        return list(self.node_attrs.keys())

    def get_node_attrs(self, node: Any) -> Dict[str, Any]:
        return dict(self.node_attrs[node])

    def update_node_attrs(self, node: Any, attrs: Dict[str, Any]) -> None:
        if node not in self.node_attrs:
            raise KeyError("Node not found")
        self.node_attrs[node].update(attrs)

    def remove_node(self, node: Any) -> None:
        if node not in self.node_attrs:
            return
        # eliminar aristas incidentes
        for nbr in list(self.adj[node].keys()):
            # remove all edges node->nbr
            for eid in list(self.adj[node][nbr]):
                self.remove_edge_by_id(eid)
        # si no dirigido, también las entradas inversas quedan removidas por remove_edge_by_id
        # pero para seguridad iteramos vecinos que point to node
        for u in list(self.adj.keys()):
            if node in self.adj[u]:
                # remove all edges u->node
                for eid in list(self.adj[u][node]):
                    self.remove_edge_by_id(eid)
        # finalmente eliminar nodo
        self.adj.pop(node, None)
        self.node_attrs.pop(node, None)

    # -------------------------
    # CRUD: ARISTAS (con atributos / etiquetas)
    # -------------------------
    def add_edge(self, u: Any, v: Any, attrs: Optional[Dict[str, Any]] = None) -> int:
        """
        Añadir arista u->v con atributos (por ejemplo {'label': 'friend', 'weight': 2.0}).
        Devuelve edge_id. Soporta aristas paralelas (varias ids entre mismos nodos).
        """
        self.add_node(u)
        self.add_node(v)
        eid = self._edge_counter
        self._edge_counter += 1
        self.edges[eid] = (u, v, dict(attrs) if attrs else {})
        self.adj[u][v].append(eid)
        if not self.directed:
            # mirror entry in adjacency for convenience (but edge id same)
            self.adj[v][u].append(eid)
        return eid

    def get_edges(self) -> List[Tuple[int, Any, Any, Dict[str, Any]]]:
        """Lista de (edge_id, u, v, attrs) (cada arista forward aparece una vez)."""
        return [(eid, u, v, dict(attrs)) for eid, (u, v, attrs) in self.edges.items()]

    def get_edge_attrs(self, eid: int) -> Dict[str, Any]:
        if eid not in self.edges:
            raise KeyError("Edge id not found")
        return dict(self.edges[eid][2])

    def update_edge_attrs(self, eid: int, attrs: Dict[str, Any]) -> None:
        if eid not in self.edges:
            raise KeyError("Edge id not found")
        u, v, a = self.edges[eid]
        a.update(attrs)
        self.edges[eid] = (u, v, a)

    def remove_edge_by_id(self, eid: int) -> None:
        if eid not in self.edges:
            return
        u, v, _ = self.edges.pop(eid)
        # eliminar eid de adj[u][v] y adj[v][u] si existe
        if v in self.adj[u]:
            self.adj[u][v] = [x for x in self.adj[u][v] if x != eid]
            if not self.adj[u][v]:
                del self.adj[u][v]
        if not self.directed:
            if u in self.adj[v]:
                self.adj[v][u] = [x for x in self.adj[v][u] if x != eid]
                if not self.adj[v][u]:
                    del self.adj[v][u]

    def remove_edge(self, u: Any, v: Any) -> None:
        """Eliminar todas las aristas entre u y v."""
        if u not in self.adj or v not in self.adj[u]:
            return
        for eid in list(self.adj[u][v]):
            self.remove_edge_by_id(eid)

    # -------------------------
    # CONSULTAS / FILTROS POR ETIQUETAS
    # -------------------------
    def nodes_with_attr(self, key: str, value: Optional[Any] = None) -> List[Any]:
        """Devuelve nodos que tienen atributo key; si value no es None, igual a value."""
        res = []
        for n, attrs in self.node_attrs.items():
            if key in attrs:
                if value is None or attrs[key] == value:
                    res.append(n)
        return res

    def edges_with_attr(self, key: str, value: Optional[Any] = None) -> List[int]:
        """Devuelve edge_ids cuya attrs contienen key (y opcionalmente igual a value)."""
        res = []
        for eid, (u, v, attrs) in self.edges.items():
            if key in attrs:
                if value is None or attrs[key] == value:
                    res.append(eid)
        return res

    def subgraph_nodes(self, nodes: List[Any]) -> 'LabeledGraph':
        """Devuelve subgrafo inducido por lista de nodos (copia de nodos, attrs y aristas entre ellos)."""
        H = LabeledGraph(directed=self.directed)
        for n in nodes:
            if n in self.node_attrs:
                H.add_node(n, dict(self.node_attrs[n]))
        for eid, (u, v, attrs) in self.edges.items():
            if u in H.node_attrs and v in H.node_attrs:
                H.add_edge(u, v, dict(attrs))
        return H

    def subgraph_by_node_attr(self, key: str, value: Optional[Any] = None) -> 'LabeledGraph':
        nodes = self.nodes_with_attr(key, value)
        return self.subgraph_nodes(nodes)

    # -------------------------
    # RECORRIDOS (BFS/DFS) con opción de filtro por etiqueta / predicado
    # -------------------------
    def bfs(self, start: Any, node_pred: Optional[Callable[[Any, Dict[str,Any]], bool]] = None,
            edge_pred: Optional[Callable[[int, Dict[str,Any]], bool]] = None) -> Tuple[List[Any], Dict[Any,int], Dict[Any,Optional[Any]]]:
        """
        BFS que recorre solo nodos/edges que cumplen predicate:
          node_pred(node, node_attrs) -> True/False
          edge_pred(edge_id, edge_attrs) -> True/False
        Retorna (orden, dist, prev_node)
        """
        if start not in self.node_attrs:
            raise KeyError("Start node not found")
        dist = {n: -1 for n in self.node_attrs}
        prev = {n: None for n in self.node_attrs}
        q = deque()
        if node_pred is None or node_pred(start, self.node_attrs[start]):
            q.append(start)
            dist[start] = 0
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v, eids in list(self.adj[u].items()):
                # check node predicate for v
                if v not in self.node_attrs:
                    continue
                if node_pred and not node_pred(v, self.node_attrs[v]):
                    continue
                # check at least one edge passes
                ok = False
                for eid in eids:
                    if edge_pred is None or edge_pred(eid, self.edges[eid][2]):
                        ok = True
                        break
                if not ok:
                    continue
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    prev[v] = u
                    q.append(v)
        return order, dist, prev

    def dfs(self, start: Any, node_pred: Optional[Callable[[Any, Dict[str,Any]], bool]] = None,
            edge_pred: Optional[Callable[[int, Dict[str,Any]], bool]] = None) -> List[Any]:
        """DFS iterativo con los mismos predicados que BFS."""
        if start not in self.node_attrs:
            raise KeyError("Start node not found")
        visited = set()
        stack = []
        if node_pred is None or node_pred(start, self.node_attrs[start]):
            stack.append(start)
        order = []
        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            order.append(u)
            for v, eids in reversed(list(self.adj[u].items())):
                if v not in self.node_attrs:
                    continue
                if node_pred and not node_pred(v, self.node_attrs[v]):
                    continue
                ok = False
                for eid in eids:
                    if edge_pred is None or edge_pred(eid, self.edges[eid][2]):
                        ok = True; break
                if ok and v not in visited:
                    stack.append(v)
        return order

    # -------------------------
    # DIJKSTRA generalizado (cost function puede usar atributos)
    # -------------------------
    def dijkstra(self, source: Any, cost_fn: Optional[Callable[[int, Dict[str,Any]], float]] = None) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
        """
        Dijkstra donde el coste de usar una arista se obtiene por cost_fn(edge_id, edge_attrs) -> float >= 0.
        Si cost_fn es None, se usa edge_attrs.get('weight', 1.0).
        Retorna (dist, prev)
        """
        if source not in self.node_attrs:
            raise KeyError("Source node not found")
        dist = {n: INF for n in self.node_attrs}
        prev = {n: None for n in self.node_attrs}
        dist[source] = 0.0
        pq = [(0.0, source)]
        while pq:
            d,u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, eids in self.adj[u].items():
                # choose minimal cost among parallel edges
                best = INF
                best_eid = None
                for eid in eids:
                    _,_,attrs = self.edges[eid]
                    if cost_fn:
                        c = cost_fn(eid, attrs)
                    else:
                        c = attrs.get('weight', 1.0)
                    if c < best:
                        best = c
                        best_eid = eid
                if best == INF:
                    continue
                nd = d + best
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev

    # -------------------------
    # LABEL PROPAGATION (algoritmo sencillo para detectar comunidades/propagación)
    # -------------------------
    def label_propagation(self, max_iter: int = 100) -> Dict[Any, Any]:
        """
        Algoritmo Raghavan et al. (simple):
         - Inicializa label[node] = node o atributo 'label' si existe.
         - Iterativamente cada nodo adopta la etiqueta mayoritaria entre sus vecinos (romper empates por orden).
         - Repetir hasta convergencia o max_iter.
        Retorna dict node -> label (community id).
        """
        labels = {}
        # init
        for n in self.node_attrs:
            # si existe label en attrs, úsala; sino, usar n como id initial
            labels[n] = self.node_attrs[n].get('label', n)
        changed = True
        it = 0
        while changed and it < max_iter:
            changed = False
            nodes = list(self.node_attrs.keys())
            # se puede usar orden aleatorio para mejor convergencia en práctica; aquí es determinista
            for u in nodes:
                # recoger etiquetas de vecinos
                cnt = Counter()
                for v, eids in self.adj[u].items():
                    if v not in labels:
                        continue
                    cnt[labels[v]] += 1
                if not cnt:
                    continue
                # elegir la etiqueta con mayor frecuencia; romper empates por menor valor (determinismo)
                best_label = min([lab for lab,c in cnt.items() if c == max(cnt.values())])
                if labels[u] != best_label:
                    labels[u] = best_label
                    changed = True
            it += 1
        return labels

    # -------------------------
    # WEISFEILER-LEHMAN 1-WL relabeling (iterative hashing of neighborhood labels)
    # útil para comparar grafos etiquetados / features para ML
    # -------------------------
    def weisfeiler_lehman_hash(self, iters: int = 3) -> Dict[Any, str]:
        """
        Devuelve un mapping node -> WL-hash (string) después de `iters` iteraciones.
        Procedimiento:
          - iniciar label0 = node_attrs.get('label', str(node))
          - en cada iter: label = hash(prev_label || sorted(multiset(neighbor_labels)))
        Retorna labels por nodo.
        """
        # initialize
        wl = {}
        for n in self.node_attrs:
            base = self.node_attrs[n].get('label', str(n))
            wl[n] = str(base)
        for _ in range(iters):
            new_wl = {}
            for n in self.node_attrs:
                neighbor_labels = []
                for v, eids in self.adj[n].items():
                    neighbor_labels.append(wl[v])
                neighbor_labels.sort()
                key = wl[n] + "|" + ",".join(neighbor_labels)
                # simple deterministic hash via Python's hash + stable str
                new_wl[n] = str(abs(hash(key)))  # convert to positive integer string
            wl = new_wl
        return wl

    def wl_graph_hash(self, iters: int = 3) -> str:
        """
        Hash global del grafo: ordenar las WL-labels de los nodos y combinarlas.
        Útil para comparación rápida (aprox.) entre grafos etiquetados.
        """
        wl = self.weisfeiler_lehman_hash(iters)
        sorted_labels = sorted(wl.values())
        s = "|".join(sorted_labels)
        return str(abs(hash(s)))

    # -------------------------
    # SERIALIZACION SIMPLE
    # -------------------------
    def to_dict(self) -> Dict:
        """Convertir grafo a dict (serializable)"""
        return {
            'directed': self.directed,
            'nodes': {n: dict(attrs) for n, attrs in self.node_attrs.items()},
            'edges': {eid: {'u': u, 'v': v, 'attrs': dict(attrs)} for eid, (u, v, attrs) in self.edges.items()}
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'LabeledGraph':
        g = LabeledGraph(directed=data.get('directed', False))
        for n, attrs in data.get('nodes', {}).items():
            g.add_node(n, dict(attrs))
        # ensure edge ids preserved: we recreate but their ids will differ; that's fine for most use-cases
        for eid_str, info in data.get('edges', {}).items():
            g.add_edge(info['u'], info['v'], dict(info.get('attrs', {})))
        return g

    def __repr__(self) -> str:
        return f"LabeledGraph(directed={self.directed}, V={len(self.node_attrs)}, E={len(self.edges)})"

#Ejemplo completo de uso
if __name__ == "__main__":
    G = LabeledGraph(directed=False)

    # CRUD nodos con etiquetas
    G.add_node("Alice", {"role": "engineer", "city": "SJ"})
    G.add_node("Bob", {"role": "engineer", "city": "LP"})
    G.add_node("Carol", {"role": "manager", "city": "SJ"})
    G.add_node("Dave", {"role": "intern", "city": "SJ"})

    # CRUD aristas con etiquetas
    e1 = G.add_edge("Alice", "Bob", {"relation": "colleague", "weight": 1.0})
    e2 = G.add_edge("Alice", "Carol", {"relation": "reports_to", "weight": 2.0})
    e3 = G.add_edge("Bob", "Carol", {"relation": "reports_to", "weight": 2.5})
    e4 = G.add_edge("Alice", "Dave", {"relation": "mentors", "weight": 0.5})

    print(G)
    print("Nodos en SJ:", G.nodes_with_attr("city", "SJ"))
    print("Aristas 'reports_to' ids:", G.edges_with_attr("relation", "reports_to"))
    print("Subgrafo (city=SJ):", G.subgraph_by_node_attr("city", "SJ"))

    # BFS filtrando solo nodos con city=SJ
    order, dist, prev = G.bfs("Alice", node_pred=lambda n,a: a.get("city") == "SJ")
    print("BFS Alice (solo SJ):", order)

    # Dijkstra usando peso que lea 'weight' atributo
    dist_all, prev = G.dijkstra("Alice", cost_fn=lambda eid, attrs: attrs.get("weight", 1.0))
    print("Dijkstra dist desde Alice:", dist_all)
    def reconstruct(prev, s, t):
        if prev[t] is None and s != t: return None
        path = []
        cur = t
        while cur is not None:
            path.append(cur)
            if cur == s: break
            cur = prev[cur]
        return list(reversed(path))
    print("Camino Alice -> Carol:", reconstruct(prev, "Alice", "Carol"))

    # Label propagation (community detection)
    communities = G.label_propagation()
    print("Label propagation (communities):", communities)

    # Weisfeiler-Lehman node hashes and graph hash
    wl = G.weisfeiler_lehman_hash(iters=2)
    print("WL labels:", wl)
    print("WL graph hash:", G.wl_graph_hash(iters=2))














#Grafos ponderados 
# directed_weighted_graph.py
from collections import deque
import heapq
from typing import Any, Dict, List, Optional, Tuple

INF = float('inf')

class DirectedWeightedGraph:
    """
    Grafo dirigido y ponderado.
    Representación: adj[u] -> dict[v] = weight
    Soporta:
      - CRUD: add/remove node/edge, update weight, get nodes/edges
      - Dijkstra (O(E log V)) -> camino más corto (no-negativos)
      - Bellman-Ford (O(V*E)) -> detecta ciclos negativos y distancias con negativos
      - Shortest paths en DAG (topo + relax en orden)
      - Floyd-Warshall (APSP) con reconstrucción de caminos (O(V^3))
      - Kosaraju para SCC (componentes fuertemente conectadas)
    """

    def __init__(self):
        self.adj: Dict[Any, Dict[Any, float]] = {}
    
    # -------------------
    # CRUD NODOS
    # -------------------
    def add_node(self, u: Any) -> None:
        if u not in self.adj:
            self.adj[u] = {}

    def get_nodes(self) -> List[Any]:
        return list(self.adj.keys())

    def remove_node(self, u: Any) -> None:
        if u not in self.adj:
            return
        # eliminar aristas salientes
        del self.adj[u]
        # eliminar aristas entrantes
        for v in list(self.adj.keys()):
            if u in self.adj[v]:
                del self.adj[v][u]

    # -------------------
    # CRUD ARISTAS
    # -------------------
    def add_edge(self, u: Any, v: Any, weight: float) -> None:
        """Añade u->v con peso (crea nodos si faltan). Si existe, actualiza el peso."""
        self.add_node(u); self.add_node(v)
        self.adj[u][v] = float(weight)

    def remove_edge(self, u: Any, v: Any) -> None:
        if u in self.adj and v in self.adj[u]:
            del self.adj[u][v]

    def update_edge_weight(self, u: Any, v: Any, new_weight: float) -> None:
        if u not in self.adj or v not in self.adj[u]:
            raise KeyError("Edge not found")
        self.adj[u][v] = float(new_weight)

    def get_edges(self) -> List[Tuple[Any, Any, float]]:
        edges = []
        for u in self.adj:
            for v, w in self.adj[u].items():
                edges.append((u, v, w))
        return edges

    # -------------------
    # Dijkstra (no negativos)
    # -------------------
    def dijkstra(self, source: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
        """
        Dijkstra con heap. Requiere que no haya pesos negativos en aristas alcanzables.
        Retorna (dist, prev) donde prev permite reconstruir caminos.
        """
        if source not in self.adj:
            raise KeyError("Source node not in graph")
        dist = {u: INF for u in self.adj}
        prev = {u: None for u in self.adj}
        dist[source] = 0.0
        pq = [(0.0, source)]
        while pq:
            d,u = heapq.heappop(pq)
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
    # Bellman-Ford (soporta negativos, detecta ciclos negativos)
    # -------------------
    def bellman_ford(self, source: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
        """
        Bellman-Ford: soporta pesos negativos y detecta ciclos negativos.
        Si hay ciclo negativo alcanzable desde source lanza ValueError.
        Retorna (dist, prev).
        """
        if source not in self.adj:
            raise KeyError("Source node not in graph")
        nodes = list(self.adj.keys())
        dist = {u: INF for u in nodes}
        prev = {u: None for u in nodes}
        dist[source] = 0.0
        n = len(nodes)
        for _ in range(n - 1):
            updated = False
            for u in nodes:
                if dist[u] == INF:
                    continue
                for v, w in self.adj[u].items():
                    nd = dist[u] + w
                    if nd < dist[v]:
                        dist[v] = nd
                        prev[v] = u
                        updated = True
            if not updated:
                break
        # Detectar ciclo negativo
        for u in nodes:
            if dist[u] == INF:
                continue
            for v, w in self.adj[u].items():
                if dist[u] + w < dist[v] - 1e-12:
                    raise ValueError("Graph contains a negative-weight cycle reachable from source")
        return dist, prev

    # -------------------
    # Shortest paths on DAG (topological order)
    # -------------------
    def topological_sort(self) -> List[Any]:
        """Devuelve orden topológico (lanza ValueError si hay ciclo)."""
        indeg = {u: 0 for u in self.adj}
        for u in self.adj:
            for v in self.adj[u]:
                indeg[v] = indeg.get(v, 0) + 1
        q = deque([u for u,c in indeg.items() if c == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v in self.adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        if len(topo) != len(self.adj):
            raise ValueError("Graph is not a DAG (contains a cycle)")
        return topo

    def shortest_paths_dag(self, source: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
        """
        Si el grafo es DAG, computa SSSP en O(V + E) relajando en orden topológico.
        Soporta pesos negativos (ya que no hay ciclos).
        """
        if source not in self.adj:
            raise KeyError("Source node not in graph")
        topo = self.topological_sort()
        dist = {u: INF for u in self.adj}
        prev = {u: None for u in self.adj}
        dist[source] = 0.0
        # procesar en orden topológico; asegurarse de que source aparece antes de sus reachable en topo
        start_index = {u:i for i,u in enumerate(topo)}
        for u in topo:
            if dist[u] == INF:
                continue
            for v, w in self.adj[u].items():
                nd = dist[u] + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
        return dist, prev

    # -------------------
    # Floyd-Warshall (APSP) con path reconstruction
    # -------------------
    def floyd_warshall(self) -> Tuple[Dict[Any, Dict[Any, float]], Dict[Any, Dict[Any, Optional[Any]]]]:
        """
        Floyd-Warshall para todas-las-parejas. Retorna (dist, next)
        next[u][v] = next node after u on shortest path to v (para reconstruir).
        Complejidad: O(V^3).
        """
        nodes = list(self.adj.keys())
        n = len(nodes)
        idx = {nodes[i]: i for i in range(n)}
        # iniciar matrices
        dist_mat = [[INF]*n for _ in range(n)]
        next_mat = [[None]*n for _ in range(n)]
        for i in range(n):
            dist_mat[i][i] = 0.0
            next_mat[i][i] = nodes[i]
        for u in self.adj:
            for v, w in self.adj[u].items():
                i = idx[u]; j = idx[v]
                dist_mat[i][j] = w
                next_mat[i][j] = v
        # FW
        for k in range(n):
            for i in range(n):
                if dist_mat[i][k] == INF:
                    continue
                for j in range(n):
                    if dist_mat[k][j] == INF:
                        continue
                    nd = dist_mat[i][k] + dist_mat[k][j]
                    if nd < dist_mat[i][j]:
                        dist_mat[i][j] = nd
                        next_mat[i][j] = next_mat[i][k]
        # convertir a dicts
        dist = {nodes[i]: {nodes[j]: dist_mat[i][j] for j in range(n)} for i in range(n)}
        nxt = {nodes[i]: {nodes[j]: next_mat[i][j] for j in range(n)} for i in range(n)}
        return dist, nxt

    @staticmethod
    def reconstruct_path_from_next(next_dict: Dict[Any, Dict[Any, Optional[Any]]], start: Any, goal: Any) -> Optional[List[Any]]:
        """Reconstruye camino usando next[u][v] = next node after u on path to v (from Floyd-Warshall)."""
        if next_dict.get(start) is None or next_dict[start].get(goal) is None:
            return None
        path = [start]
        cur = start
        while cur != goal:
            cur = next_dict[cur][goal]
            if cur is None:
                return None
            path.append(cur)
        return path

    # -------------------
    # Kosaraju (SCC)
    # -------------------
    def strongly_connected_components(self) -> List[List[Any]]:
        """Kosaraju para SCC en grafo dirigido."""
        visited = set()
        order = []
        def dfs1(u):
            visited.add(u)
            for v in self.adj[u]:
                if v not in visited:
                    dfs1(v)
            order.append(u)
        for u in self.adj:
            if u not in visited:
                dfs1(u)
        # construir grafo transpuesto
        radj = {u: [] for u in self.adj}
        for u in self.adj:
            for v in self.adj[u]:
                radj[v].append(u)
        visited.clear()
        comps = []
        def dfs2(u, comp):
            visited.add(u)
            comp.append(u)
            for v in radj[u]:
                if v not in visited:
                    dfs2(v, comp)
        for u in reversed(order):
            if u not in visited:
                comp = []
                dfs2(u, comp)
                comps.append(comp)
        return comps

    # -------------------
    # Util: reconstruir camino desde prev (Dijkstra/Bellman/DAG)
    # -------------------
    @staticmethod
    def reconstruct_path(prev: Dict[Any, Optional[Any]], start: Any, goal: Any) -> Optional[List[Any]]:
        if start == goal:
            return [start]
        if goal not in prev or prev[goal] is None:
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

    def __repr__(self):
        return f"DirectedWeightedGraph(V={len(self.adj)}, E={len(self.get_edges())})"

#Ejemplo de uso completo
if __name__ == "__main__":
    G = DirectedWeightedGraph()

    # CRUD: nodos/aristas
    G.add_edge("s", "a", 5)
    G.add_edge("s", "b", 3)
    G.add_edge("a", "b", 2)
    G.add_edge("a", "c", 6)
    G.add_edge("b", "c", 7)
    G.add_edge("b", "d", 4)
    G.add_edge("c", "d", -1)  # ejemplo con peso negativo (para Bellman-Ford)
    G.add_edge("d", "e", 2)
    G.add_edge("e", "c", 1)

    print(G)
    print("Nodos:", G.get_nodes())
    print("Aristas:", G.get_edges())

    # Dijkstra (no usar si hay aristas negativas alcanzables)
    try:
        dist_dij, prev_dij = G.dijkstra("s")
        print("Dijkstra dist desde s:", dist_dij)
        print("Camino s -> d (Dijkstra):", DirectedWeightedGraph.reconstruct_path(prev_dij, "s", "d"))
    except Exception as ex:
        print("Dijkstra error:", ex)

    # Bellman-Ford (soporta negativos y detecta ciclos negativos)
    try:
        dist_bf, prev_bf = G.bellman_ford("s")
        print("Bellman-Ford dist desde s:", dist_bf)
        print("Camino s -> d (Bellman-Ford):", DirectedWeightedGraph.reconstruct_path(prev_bf, "s", "d"))
    except ValueError as e:
        print("Bellman-Ford detectó ciclo negativo:", e)

    # Si el grafo fuese DAG, usar shortest_paths_dag (ejemplo: construir DAG pequeño)
    DAG = DirectedWeightedGraph()
    DAG.add_edge("1", "2", 3)
    DAG.add_edge("1", "3", 6)
    DAG.add_edge("2", "3", 4)
    DAG.add_edge("2", "4", 2)
    DAG.add_edge("3", "4", 1)
    dist_dag, prev_dag = DAG.shortest_paths_dag("1")
    print("DAG shortest from 1:", dist_dag)
    print("Path 1->4 (DAG):", DirectedWeightedGraph.reconstruct_path(prev_dag, "1", "4"))

    # Floyd-Warshall (APSP)
    dist_fw, next_fw = G.floyd_warshall()
    print("FW dist s->e:", dist_fw["s"]["e"])
    p = DirectedWeightedGraph.reconstruct_path_from_next(next_fw, "s", "e")
    print("FW path s->e:", p)

    # SCCs (Kosaraju)
    sccs = G.strongly_connected_components()
    print("SCCs:", sccs)











#Grados aleatorios 
# random_graph.py
import random
import math
from collections import deque, defaultdict, Counter
import heapq
from typing import Any, Dict, List, Optional, Tuple, Set

INF = float('inf')

class RandomGraph:
    """
    Grafo (principalmente no dirigido) con soporte para:
     - CRUD: add_node, remove_node, add_edge, remove_edge, get_nodes, get_edges
     - Generadores aleatorios: erdos_renyi_gnp, erdos_renyi_gnm, barabasi_albert, watts_strogatz
     - Algoritmos: BFS, DFS, connected_components, largest_component,
                   degree_distribution, clustering_coefficient (local y average),
                   average_shortest_path_length (exacto o muestreado),
                   dijkstra (si weighted), kruskal_mst,
                   label_propagation (comunidad heurística).
    Nota: representación: adj: dict[node] -> dict[neighbor] -> weight (float) 
    Si el grafo es no ponderado se guarda weight=1.0 por convención.
    """

    def __init__(self, directed: bool = False, weighted: bool = False):
        self.directed = directed
        self.weighted = weighted
        self.adj: Dict[Any, Dict[Any, float]] = {}
        # mantener lista de aristas para operaciones que las requieren
        # en no dirigido cada par (u,v) aparece una sola vez en get_edges
        # almacenamiento solo en adj; edges se obtienen dinámicamente

    # -------------------
    # CRUD NODOS / ARISTAS
    # -------------------
    def add_node(self, u: Any) -> None:
        if u not in self.adj:
            self.adj[u] = {}

    def remove_node(self, u: Any) -> None:
        if u not in self.adj:
            return
        # eliminar aristas incidentes
        for v in list(self.adj[u].keys()):
            if v in self.adj:
                self.adj[v].pop(u, None)
        del self.adj[u]

    def add_edge(self, u: Any, v: Any, weight: Optional[float] = None) -> None:
        """Añade arista u-v (o u->v si directed). Crea nodos si faltan. Si weighted==False usa 1.0"""
        self.add_node(u); self.add_node(v)
        if weight is None:
            w = 1.0 if not self.weighted else 1.0
        else:
            w = float(weight)
        self.adj[u][v] = w
        if not self.directed:
            self.adj[v][u] = w

    def remove_edge(self, u: Any, v: Any) -> None:
        if u in self.adj:
            self.adj[u].pop(v, None)
        if not self.directed and v in self.adj:
            self.adj[v].pop(u, None)

    def get_nodes(self) -> List[Any]:
        return list(self.adj.keys())

    def get_edges(self) -> List[Tuple[Any, Any, float]]:
        edges = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u].items():
                if self.directed:
                    edges.append((u, v, w))
                else:
                    key = tuple(sorted((u, v), key=lambda x: str(x)))
                    if key in seen:
                        continue
                    seen.add(key)
                    edges.append((key[0], key[1], w))
        return edges

    def clear(self) -> None:
        self.adj.clear()

    # -------------------
    # GENERADORES ALEATORIOS
    # -------------------
    def erdos_renyi_gnp(self, n: int, p: float, seed: Optional[int] = None) -> None:
        """Genera G(n, p): n nodos, cada par con probabilidad p."""
        if seed is not None:
            random.seed(seed)
        self.clear()
        for i in range(n):
            self.add_node(i)
        nodes = list(self.adj.keys())
        for i in range(n):
            for j in range(i+1, n):
                if random.random() < p:
                    self.add_edge(nodes[i], nodes[j])

    def erdos_renyi_gnm(self, n: int, m: int, seed: Optional[int] = None) -> None:
        """Genera G(n, m): n nodos, exactamente m aristas aleatorias sin repetición."""
        if seed is not None:
            random.seed(seed)
        self.clear()
        for i in range(n):
            self.add_node(i)
        possible = [(i,j) for i in range(n) for j in range(i+1, n)]
        if m > len(possible):
            raise ValueError("m too large for number of node pairs")
        chosen = random.sample(possible, m)
        for u,v in chosen:
            self.add_edge(u, v)

    def barabasi_albert(self, n: int, m: int, seed: Optional[int] = None) -> None:
        """
        Barabási–Albert model: inicio con m0 = m nodos conectados (small clique or line),
        luego añadir nodos uno a uno; cada nuevo nodo se conecta a m nodos existentes
        por preferential attachment (prob ~ degree).
        Requiere m >= 1 and m < n.
        """
        if seed is not None:
            random.seed(seed)
        if m < 1 or m >= n:
            raise ValueError("Require 1 <= m < n")
        self.clear()
        # start with m nodes fully connected
        for i in range(m):
            self.add_node(i)
        for i in range(m):
            for j in range(i+1, m):
                self.add_edge(i, j)
        # list of nodes with multiplicity proportional to degree (for sampling)
        target_list = []
        for u in self.get_nodes():
            # degree times (initial degrees)
            deg = len(self.adj[u])
            target_list.extend([u] * deg)
        # now add nodes
        for new in range(m, n):
            self.add_node(new)
            # preferentially choose m distinct targets
            targets = set()
            while len(targets) < m:
                if not target_list:
                    # fallback: choose uniformly
                    cand = random.choice(self.get_nodes())
                else:
                    cand = random.choice(target_list)
                if cand == new:
                    continue
                targets.add(cand)
            for t in targets:
                self.add_edge(new, t)
            # update target_list: add new node m times + each target gets +1
            target_list.extend([new] * m)
            for t in targets:
                target_list.append(t)

    def watts_strogatz(self, n: int, k: int, beta: float, seed: Optional[int] = None) -> None:
        """
        Watts–Strogatz small-world model:
         - Start with ring lattice where each node connected to k nearest neighbors (k must be even)
         - Rewire each edge (u, v) with probability beta to a randomly chosen node (no self-loops, no duplicate edges)
        """
        if seed is not None:
            random.seed(seed)
        if k >= n:
            raise ValueError("k must be < n")
        if k % 2 != 0:
            raise ValueError("k must be even")
        self.clear()
        for i in range(n):
            self.add_node(i)
        nodes = list(range(n))
        # ring lattice: connect i to i+1..i+k/2 and symmetric
        half = k // 2
        for i in range(n):
            for j in range(1, half+1):
                v = (i + j) % n
                self.add_edge(i, v)
        # rewire edges (only consider i < v to visit each undirected edge once)
        for i in range(n):
            for j in range(1, half+1):
                v = (i + j) % n
                if i < v:
                    if random.random() < beta:
                        # rewire i - v : choose new w not equal i and not already neighbor(i)
                        candidates = [x for x in nodes if x != i and x not in self.adj[i]]
                        if not candidates:
                            continue
                        w = random.choice(candidates)
                        # remove edge i-v and add i-w (ensure symmetric)
                        self.remove_edge(i, v)
                        self.add_edge(i, w)

    # -------------------
    # RECORRIDOS Y COMPONENTES
    # -------------------
    def bfs(self, start: Any) -> Tuple[List[Any], Dict[Any,int], Dict[Any, Optional[Any]]]:
        if start not in self.adj:
            raise KeyError("Start node not in graph")
        dist = {n: -1 for n in self.adj}
        prev = {n: None for n in self.adj}
        q = deque([start])
        dist[start] = 0
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    prev[v] = u
                    q.append(v)
        return order, dist, prev

    def dfs(self, start: Any) -> List[Any]:
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
            for v in reversed(list(self.adj[u].keys())):
                if v not in visited:
                    stack.append(v)
        return order

    def connected_components(self) -> List[List[Any]]:
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

    def largest_component(self) -> List[Any]:
        comps = self.connected_components()
        if not comps:
            return []
        return max(comps, key=len)

    # -------------------
    # GRADO Y DISTRIBUCION
    # -------------------
    def degree(self, u: Any) -> int:
        if u not in self.adj:
            raise KeyError("Node not found")
        return len(self.adj[u])

    def degree_distribution(self) -> Dict[int, int]:
        cnt = Counter()
        for u in self.adj:
            cnt[len(self.adj[u])] += 1
        return dict(cnt)

    # -------------------
    # CLUSTERING COEFFICIENT
    # -------------------
    def clustering_coefficient_local(self, u: Any) -> float:
        """Coeficiente de clustering local: 2*E_n / (k*(k-1))"""
        if u not in self.adj:
            raise KeyError("Node not found")
        nbrs = list(self.adj[u].keys())
        k = len(nbrs)
        if k < 2:
            return 0.0
        links = 0
        for i in range(k):
            for j in range(i+1, k):
                a, b = nbrs[i], nbrs[j]
                if b in self.adj[a]:
                    links += 1
        return (2.0 * links) / (k * (k - 1))

    def clustering_coefficient_average(self) -> float:
        total = 0.0
        n = len(self.adj)
        if n == 0:
            return 0.0
        for u in self.adj:
            total += self.clustering_coefficient_local(u)
        return total / n

    # -------------------
    # PATHS: average shortest path length (exact or sampled)
    # -------------------
    def average_shortest_path_length(self, samples: Optional[int] = None) -> float:
        """
        Si samples is None compute exact APSP median: O(n*(n+m)) using BFS from every node (only for unweighted).
        Si samples is int, muestrea `samples` nodos aleatorios y promedia sus distancias (más rápido para grafos grandes).
        Nota: si el grafo no es conectado se calcula sobre la componente gigante.
        """
        n = len(self.adj)
        if n == 0:
            return 0.0
        giant = set(self.largest_component())
        # operate on giant component only
        nodes = list(giant)
        if samples is None or samples >= len(nodes):
            # exact: BFS from every node in giant
            total = 0
            count = 0
            for u in nodes:
                _, dist, _ = self.bfs(u)
                for v in nodes:
                    if v == u:
                        continue
                    d = dist[v]
                    if d >= 0:
                        total += d
                        count += 1
            return total / count if count > 0 else 0.0
        else:
            total = 0
            count = 0
            for _ in range(samples):
                u = random.choice(nodes)
                _, dist, _ = self.bfs(u)
                for v in nodes:
                    if v == u:
                        continue
                    d = dist[v]
                    if d >= 0:
                        total += d
                        count += 1
            return total / count if count > 0 else 0.0

    # -------------------
    # DIJKSTRA (si ponderado)
    # -------------------
    def dijkstra(self, source: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
        if source not in self.adj:
            raise KeyError("Source not in graph")
        dist = {u: INF for u in self.adj}
        prev = {u: None for u in self.adj}
        dist[source] = 0.0
        pq = [(0.0, source)]
        while pq:
            d,u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.adj[u].items():
                nd = d + (w if self.weighted else 1.0)
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev

    # -------------------
    # MST: Kruskal (necesita no dirigido y weighted=True)
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

    def kruskal_mst(self) -> Tuple[List[Tuple[Any, Any, float]], float]:
        if self.directed:
            raise ValueError("Kruskal MST only for undirected graphs")
        edges = self.get_edges()
        if not self.weighted:
            # treat all weights as 1.0
            edges = [(u,v,1.0) for (u,v,_) in edges]
        edges_sorted = sorted(edges, key=lambda x: x[2])
        dsu = RandomGraph._DSU()
        for u in self.adj:
            dsu.make_set(u)
        mst = []
        total = 0.0
        for u,v,w in edges_sorted:
            if dsu.union(u, v):
                mst.append((u, v, w))
                total += w
            if len(mst) == max(0, len(self.adj) - 1):
                break
        return mst, total

    # -------------------
    # LABEL PROPAGATION (heurística para comunidades)
    # -------------------
    def label_propagation(self, max_iter: int = 100) -> Dict[Any, Any]:
        labels = {u: u for u in self.adj}
        changed = True
        it = 0
        while changed and it < max_iter:
            changed = False
            nodes = list(self.adj.keys())
            random.shuffle(nodes)
            for u in nodes:
                cnt = Counter()
                for v in self.adj[u]:
                    cnt[labels[v]] += 1
                if not cnt:
                    continue
                best = max(cnt.items(), key=lambda x: (x[1], -hash(x[0])))[0]
                if labels[u] != best:
                    labels[u] = best
                    changed = True
            it += 1
        return labels

    # -------------------
    # UTIL
    # -------------------
    def number_of_nodes(self) -> int:
        return len(self.adj)

    def number_of_edges(self) -> int:
        return len(self.get_edges())

    def __repr__(self) -> str:
        return f"RandomGraph(directed={self.directed}, weighted={self.weighted}, V={self.number_of_nodes()}, E={self.number_of_edges()})"

#Ejemplos de uso
if __name__ == "__main__":
    # 1) Erdős–Rényi G(n,p)
    G = RandomGraph()
    G.erdos_renyi_gnp(n=100, p=0.03, seed=42)
    print("ER G(100,0.03):", G)
    print("Componente gigante size:", len(G.largest_component()))
    print("Degree dist (top 10):", sorted(G.degree_distribution().items())[:10])
    print("Avg clustering:", G.clustering_coefficient_average())
    print("Avg path length (sample 20):", G.average_shortest_path_length(samples=20))

    # 2) Barabási–Albert (scale-free)
    H = RandomGraph()
    H.barabasi_albert(n=200, m=3, seed=1)
    print("BA n=200 m=3:", H)
    dd = H.degree_distribution()
    print("Degree distribution example (top degrees):", sorted(dd.items(), reverse=True)[:10])
    print("Clustering avg:", H.clustering_coefficient_average())

    # 3) Watts–Strogatz (small-world)
    W = RandomGraph()
    W.watts_strogatz(n=100, k=6, beta=0.2, seed=7)
    print("WS n=100 k=6 beta=0.2:", W)
    print("Clustering avg:", W.clustering_coefficient_average())
    print("Avg path length sample:", W.average_shortest_path_length(samples=20))

    # 4) Use MST / Dijkstra if weighted
    # create small weighted ER
    GW = RandomGraph(weighted=True)
    GW.erdos_renyi_gnp(n=30, p=0.2, seed=5)
    # assign random weights
    for u,v,w in GW.get_edges():
        GW.adj[u][v] = random.uniform(0.1, 10.0)
        if not GW.directed:
            GW.adj[v][u] = GW.adj[u][v]
    print("Weighted small ER:", GW)
    mst, total = GW.kruskal_mst()
    print("MST total weight:", total)
    # Dijkstra from node 0
    dist, prev = GW.dijkstra(0)
    print("Dijkstra dist sample:", {k: dist[k] for k in list(dist)[:5]})

    # 5) Label propagation communities
    comm = H.label_propagation()
    # count community sizes
    sizes = Counter(comm.values())
    print("BA label-prop community sizes (top):", sizes.most_common()[:5])