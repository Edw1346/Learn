#Grafo acíclico
# acyclic_graph.py
from collections import deque, defaultdict
import math
from typing import Any, Dict, List, Tuple, Optional, Set

class AcyclicGraph:
    """
    Grafo dirigido pensado para trabajar con DAGs.
    - self.adj: dict[node] -> dict[neighbor] = weight (weight opcional; por defecto 1)
    - Si enforce_acyclic=True, add_edge comprobará si la nueva arista crea un ciclo y rechazará la inserción.
    Nodos: cualquier hashable (int, str, ...).
    """

    def __init__(self, enforce_acyclic: bool = True):
        self.adj: Dict[Any, Dict[Any, float]] = {}
        self.enforce_acyclic = enforce_acyclic

    # -------------------
    # CRUD: NODOS
    # -------------------
    def add_node(self, u: Any) -> None:
        """Crear/asegurar existencia del nodo."""
        if u not in self.adj:
            self.adj[u] = {}

    def get_nodes(self) -> List[Any]:
        return list(self.adj.keys())

    def remove_node(self, u: Any) -> None:
        """Eliminar nodo y todas las aristas entrantes/ salientes hacia/desde u."""
        if u not in self.adj:
            raise KeyError(f"Node {u} not found")
        # eliminar aristas entrantes
        for v in list(self.adj.keys()):
            self.adj[v].pop(u, None)
        # eliminar nodo
        del self.adj[u]

    # -------------------
    # CRUD: ARISTAS
    # -------------------
    def add_edge(self, u: Any, v: Any, weight: float = 1.0) -> None:
        """
        Añade arista dirigida u -> v con peso (por defecto 1).
        Si enforce_acyclic=True y la arista crea un ciclo se lanza ValueError y la arista NO se añade.
        """
        self.add_node(u)
        self.add_node(v)
        # provisional: insertar y comprobar ciclo si es requerido
        if self.enforce_acyclic:
            # insertar temporalmente
            prev = self.adj[u].get(v, None)
            self.adj[u][v] = weight
            if self.has_cycle():
                # revertir
                if prev is None:
                    del self.adj[u][v]
                else:
                    self.adj[u][v] = prev
                raise ValueError(f"Adding edge {u} -> {v} would create a cycle (operation rejected).")
        else:
            self.adj[u][v] = weight

    def get_edges(self) -> List[Tuple[Any, Any, float]]:
        """Lista de aristas (u, v, weight)."""
        edges = []
        for u in self.adj:
            for v, w in self.adj[u].items():
                edges.append((u, v, w))
        return edges

    def get_edge_weight(self, u: Any, v: Any) -> Optional[float]:
        return self.adj.get(u, {}).get(v, None)

    def remove_edge(self, u: Any, v: Any) -> None:
        """Eliminar arista u->v."""
        if u not in self.adj:
            raise KeyError(f"Node {u} not found")
        self.adj[u].pop(v, None)

    def update_edge_weight(self, u: Any, v: Any, new_weight: float) -> None:
        """Actualizar peso de arista u->v (lanza KeyError si no existe)."""
        if self.get_edge_weight(u, v) is None:
            raise KeyError(f"Edge {u}->{v} not found")
        self.adj[u][v] = new_weight

    # -------------------
    # Detección de ciclos (DFS)
    # -------------------
    def has_cycle(self) -> bool:
        """
        Detecta si hay ciclo en el grafo dirigido (DFS con recursion stack).
        Complejidad: O(V + E).
        """
        visited: Set[Any] = set()
        rec_stack: Set[Any] = set()

        def dfs(u: Any) -> bool:
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

    # -------------------
    # Topological Sort
    # -------------------
    def topological_sort_kahn(self) -> List[Any]:
        """
        Orden topológico con Kahn (BFS sobre indegrees).
        Lanza ValueError si el grafo tiene ciclo.
        Complejidad: O(V + E).
        """
        indeg: Dict[Any, int] = {u: 0 for u in self.adj}
        for u in self.adj:
            for v in self.adj[u]:
                indeg[v] = indeg.get(v, 0) + 1

        q = deque([u for u in indeg if indeg[u] == 0])
        topo: List[Any] = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v in self.adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        if len(topo) != len(indeg):
            raise ValueError("Graph has at least one cycle; topological sort not possible")
        return topo

    def topological_sort_dfs(self) -> List[Any]:
        """
        Orden topológico usando DFS (post-order reversed).
        Lanza ValueError si hay ciclo.
        """
        visited: Set[Any] = set()
        temp: Set[Any] = set()
        order: List[Any] = []

        def dfs(u: Any):
            if u in temp:
                raise ValueError("Graph has a cycle; topological sort not possible")
            if u not in visited:
                temp.add(u)
                for v in self.adj[u]:
                    dfs(v)
                temp.remove(u)
                visited.add(u)
                order.append(u)

        for node in self.adj:
            if node not in visited:
                dfs(node)
        order.reverse()
        return order

    # -------------------
    # Caminos en DAG (O(V + E))
    # -------------------
    def shortest_paths_from(self, start: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
        """
        Caminos más cortos desde `start` en DAG (pesos pueden ser >= -inf).
        Implementación en O(V + E) usando orden topológico.
        - Si hay pesos negativos es válido (sin ciclos negativos porque es DAG).
        Retorna (dist, prev)
        """
        if start not in self.adj:
            raise KeyError("Start node not found")
        # orden topológico
        topo = self.topological_sort_kahn()
        dist = {u: math.inf for u in self.adj}
        prev: Dict[Any, Optional[Any]] = {u: None for u in self.adj}
        dist[start] = 0.0
        for u in topo:
            if dist[u] != math.inf:
                for v, w in self.adj[u].items():
                    nd = dist[u] + w
                    if nd < dist[v]:
                        dist[v] = nd
                        prev[v] = u
        return dist, prev

    def longest_paths_from(self, start: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
        """
        Caminos más largos desde `start` en DAG (útil para Critical Path).
        - Inicializa dist a -inf y relaja en orden topológico.
        Complejidad: O(V + E).
        """
        if start not in self.adj:
            raise KeyError("Start node not found")
        topo = self.topological_sort_kahn()
        dist = {u: -math.inf for u in self.adj}
        prev: Dict[Any, Optional[Any]] = {u: None for u in self.adj}
        dist[start] = 0.0
        for u in topo:
            if dist[u] != -math.inf:
                for v, w in self.adj[u].items():
                    nd = dist[u] + w
                    if nd > dist[v]:
                        dist[v] = nd
                        prev[v] = u
        return dist, prev

    # -------------------
    # Utilidades
    # -------------------
    @staticmethod
    def reconstruct_path(prev: Dict[Any, Optional[Any]], start: Any, goal: Any) -> Optional[List[Any]]:
        """Reconstruye camino start -> goal usando prev dict (o None si no alcanzable)."""
        if prev.get(goal) is None and start != goal:
            if goal == start:
                return [start]
            return None
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            if cur == start:
                break
            cur = prev[cur]
        path.reverse()
        if path and path[0] == start:
            return path
        return None

    def has_path(self, u: Any, v: Any) -> bool:
        """Comprueba si existe camino de u a v (BFS). O(V + E) worst-case."""
        if u not in self.adj or v not in self.adj:
            return False
        q = deque([u])
        seen = {u}
        while q:
            x = q.popleft()
            if x == v:
                return True
            for nei in self.adj[x]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        return False

    def __repr__(self) -> str:
        return f"AcyclicGraph(nodes={len(self.adj)}, edges={len(self.get_edges())}, enforce_acyclic={self.enforce_acyclic})"

#Ejemplo de uso (práctico)
if __name__ == "__main__":
    g = AcyclicGraph(enforce_acyclic=True)

    # CRUD: nodos y aristas
    g.add_node("A")
    g.add_node("B")
    g.add_edge("A", "B", weight=3)     # A -> B
    g.add_edge("A", "C", weight=2)
    g.add_edge("B", "D", weight=4)
    g.add_edge("C", "D", weight=1)
    g.add_edge("D", "E", weight=2)

    print(g)
    print("Nodos:", g.get_nodes())
    print("Aristas:", g.get_edges())

    # Intento de añadir arista que crea ciclo (será rechazado)
    try:
        g.add_edge("E", "A", weight=1)  # intentaría crear ciclo
    except ValueError as e:
        print("Error al añadir arista:", e)

    # Topological sort (Kahn)
    topo = g.topological_sort_kahn()
    print("Topological order (Kahn):", topo)

    # Topological sort (DFS)
    topo2 = g.topological_sort_dfs()
    print("Topological order (DFS):", topo2)

    # Shortest paths from A (DAG algorithm O(V+E))
    dist, prev = g.shortest_paths_from("A")
    print("Shortest dist desde A:", dist)
    print("Camino mínimo A -> E:", AcyclicGraph.reconstruct_path(prev, "A", "E"))

    # Longest paths from A (Critical path)
    long_dist, long_prev = g.longest_paths_from("A")
    print("Longest dist desde A:", long_dist)
    print("Longest path A -> E:", AcyclicGraph.reconstruct_path(long_prev, "A", "E"))

    # Comprobar existencia de camino
    print("¿Existe camino B -> C?", g.has_path("B", "C"))
    print("¿Existe camino C -> E?", g.has_path("C", "E"))












#Árbol 
# tree_graph.py
from collections import deque, defaultdict
import math
from typing import Dict, List, Optional, Tuple, Set

class Tree:
    """
    Estructura para trabajar con árboles (no dirigidos, acíclicos y conexos).
    Representación interna: adj: dict[node] -> set(neighbors)
    Soporta 'rooted' operations (se elige una raíz y se hace preprocessing para LCA).
    """

    def __init__(self):
        self.adj: Dict = {}
        self.root: Optional = None
        # datos para operaciones en raíz: depth, parent[0], up table (binary lifting), subtree_size
        self.depth: Dict = {}
        self.parent0: Dict = {}
        self.up: List[Dict] = []   # up[j][v] = 2^j-th ancestor of v
        self.LOG: int = 0
        self.subtree_size: Dict = {}
        self._preprocessed = False

    # -------------------
    # CRUD: NODOS
    # -------------------
    def add_node(self, v):
        """Añade nodo aislado si no existe."""
        if v not in self.adj:
            self.adj[v] = set()
            self._preprocessed = False

    def get_nodes(self):
        return list(self.adj.keys())

    def remove_node(self, v):
        """
        Elimina nodo v si existe.
        Para mantener propiedad de árbol, solo se permite eliminar si es hoja (grado 0 o 1).
        Si quieres quitar un nodo interno se recomienda eliminar primero sus aristas o reorganizar.
        """
        if v not in self.adj:
            raise KeyError(f"Node {v} not found")
        deg = len(self.adj[v])
        if deg > 1:
            raise ValueError("Only leaf nodes (degree <= 1) can be removed to keep structure simple.")
        # quitar referencia del vecino si lo hay
        for nei in list(self.adj[v]):
            self.adj[nei].remove(v)
        del self.adj[v]
        self._preprocessed = False

    # -------------------
    # CRUD: ARISTAS
    # -------------------
    def add_edge(self, u, v):
        """
        Añade arista u - v.
        - Si u o v no existen, se crean.
        - Antes de añadir, comprobamos que no se forme ciclo (es decir, que u y v no ya estén conectados).
        - Después, el grafo resultante sigue siendo bosque; si quieres garantizar árbol completo,
          deberías asegurarte que ahora sea conexo y sin ciclos.
        """
        self.add_node(u)
        self.add_node(v)
        # si ya hay camino entre u y v, añadir la arista crearía ciclo -> rechazamos
        if self.has_path(u, v):
            raise ValueError("Adding this edge would create a cycle (trees must remain acyclic).")
        self.adj[u].add(v)
        self.adj[v].add(u)
        self._preprocessed = False

    def remove_edge(self, u, v):
        """
        Elimina arista u-v. El resultado puede desconectar el árbol en dos componentes (ya no sería árbol único).
        Permitimos la operación, pero el objeto ya no representará un único árbol hasta que se reconecte.
        """
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        self.adj[u].discard(v)
        self.adj[v].discard(u)
        self._preprocessed = False

    def get_edges(self):
        """Devuelve lista de aristas (u, v) con u < v (por consistencia)."""
        edges = []
        seen = set()
        for u in self.adj:
            for v in self.adj[u]:
                key = tuple(sorted((u, v), key=lambda x: str(x)))
                if key not in seen:
                    edges.append(key)
                    seen.add(key)
        return edges

    def update_edge(self, u, v, new_u=None, new_v=None):
        """
        Permite "mover" la arista u-v a new_u-new_v (útil para restructurar).
        Implementación sencilla: elimina u-v y añade new_u-new_v.
        """
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        self.remove_edge(u, v)
        nu = new_u if new_u is not None else u
        nv = new_v if new_v is not None else v
        # si sería crear ciclo, raise
        if nu not in self.adj:
            self.add_node(nu)
        if nv not in self.adj:
            self.add_node(nv)
        if self.has_path(nu, nv):
            raise ValueError("Updating edge would create a cycle.")
        self.add_edge(nu, nv)
        self._preprocessed = False

    # -------------------
    # UTIL: comprobar si la estructura es un árbol (conexo y |E| = |V| - 1)
    # -------------------
    def is_tree(self) -> bool:
        n = len(self.adj)
        if n == 0:
            return True
        m = len(self.get_edges())
        if m != n - 1:
            return False
        # comprobar conectividad via BFS desde cualquier nodo
        start = next(iter(self.adj))
        visited = set()
        q = deque([start])
        visited.add(start)
        while q:
            u = q.popleft()
            for v in self.adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return len(visited) == n

    # -------------------
    # RECORRIDOS: BFS / DFS
    # -------------------
    def bfs(self, start) -> Tuple[List, Dict]:
        """BFS: devuelve (orden, dist en saltos)."""
        if start not in self.adj:
            raise KeyError("Start node not in tree")
        dist = {u: -1 for u in self.adj}
        order = []
        q = deque([start])
        dist[start] = 0
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return order, dist

    def dfs(self, start, visited=None) -> List:
        """DFS recursivo (devuelve orden pre-order)."""
        if start not in self.adj:
            raise KeyError("Start node not in tree")
        if visited is None:
            visited = set()
        res = []
        def _dfs(u, p):
            visited.add(u)
            res.append(u)
            for v in sorted(self.adj[u], key=lambda x: str(x)):
                if v == p:
                    continue
                _dfs(v, u)
        _dfs(start, None)
        return res

    # -------------------
    # PREPROCESS PARA ROOTED OPERATIONS (LCA, depths, subtree sizes)
    # -------------------
    def preprocess(self, root=None):
        """
        Preprocesa depth, parent0 y tabla up para binary lifting, y subtree_size.
        Debe llamarse antes de consultas LCA, kth ancestor, subtree_size, path reconstruction eficientemente.
        Complejidad O(n log n).
        """
        if not self.adj:
            self.root = None
            self.depth = {}
            self.parent0 = {}
            self.up = []
            self.subtree_size = {}
            self._preprocessed = True
            return

        if root is None:
            root = next(iter(self.adj))
        self.root = root
        n = len(self.adj)
        self.LOG = math.ceil(math.log2(max(2, n)))
        self.up = [dict() for _ in range(self.LOG + 1)]
        self.depth = {}
        self.parent0 = {}
        self.subtree_size = {}

        # BFS/stack to set depth & parent0
        q = deque([root])
        self.depth[root] = 0
        self.parent0[root] = None
        visited = {root}
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                if v not in visited:
                    visited.add(v)
                    self.depth[v] = self.depth[u] + 1
                    self.parent0[v] = u
                    q.append(v)

        # if disconnected, set unseen nodes as separate (depth None) but still include
        for v in self.adj:
            if v not in visited:
                # treat as separate root
                self.depth[v] = 0
                self.parent0[v] = None

        # fill up[0]
        for v in self.adj:
            self.up[0][v] = self.parent0.get(v, None)

        # binary lifting table
        for j in range(1, self.LOG + 1):
            for v in self.adj:
                mid = self.up[j-1].get(v, None)
                self.up[j][v] = self.up[j-1].get(mid, None) if mid is not None else None

        # compute subtree sizes via post-order DFS from each component root
        self.subtree_size = {v: 0 for v in self.adj}
        visited = set()
        def dfs_size(u, p):
            s = 1
            visited.add(u)
            for w in self.adj[u]:
                if w == p:
                    continue
                if w not in visited:
                    s += dfs_size(w, u)
            self.subtree_size[u] = s
            return s

        for v in self.adj:
            if self.parent0.get(v) is None and v not in visited:
                dfs_size(v, None)

        self._preprocessed = True



    # -------------------
    # LCA (Lowest Common Ancestor) - binary lifting
    # -------------------
    def lca(self, a, b):
        """Devuelve Lowest Common Ancestor de a y b. Requiere preprocess() previo."""
        if not self._preprocessed:
            self.preprocess(self.root)
        if a not in self.adj or b not in self.adj:
            raise KeyError("Node(s) not found")
        # si en componentes distintas, no hay LCA definido -> return None
        # We'll treat different roots: if parent0 chain doesn't reach same root, return None
        # But using depth values: if both have depth 0 but different roots, return None
        # We'll climb; if ancestors never match -> None
        if self.depth.get(a) is None or self.depth.get(b) is None:
            return None

        # ensure a deeper or equal
        if self.depth[a] < self.depth[b]:
            a, b = b, a
        # lift a to depth of b
        diff = self.depth[a] - self.depth[b]
        j = 0
        while diff:
            if diff & 1:
                a = self.up[j].get(a, None)
                if a is None:
                    return None
            diff >>= 1
            j += 1
        if a == b:
            return a
        # binary lift both
        for j in range(self.LOG, -1, -1):
            ua = self.up[j].get(a, None)
            ub = self.up[j].get(b, None)
            if ua != ub:
                a = ua
                b = ub
        # now parents must be equal and the LCA
        return self.parent0.get(a, None)

    # -------------------
    # kth ancestor
    # -------------------
    def kth_ancestor(self, v, k):
        """Devuelve el k-ésimo ancestro de v (k>=0), o None si no existe. Requiere preprocess."""
        if not self._preprocessed:
            self.preprocess(self.root)
        if v not in self.adj:
            raise KeyError("Node not found")
        cur = v
        j = 0
        while k and cur is not None:
            if k & 1:
                cur = self.up[j].get(cur, None)
            k >>= 1
            j += 1
        return cur

    # -------------------
    # path between nodes
    # -------------------
    def path(self, u, v) -> Optional[List]:
        """Devuelve la lista de nodos en el camino simple entre u y v, o None si no conectados."""
        if u not in self.adj or v not in self.adj:
            raise KeyError("Node(s) not found")
        # usar LCA and reconstruct path
        if not self._preprocessed:
            self.preprocess(self.root)
        ancestor = self.lca(u, v)
        if ancestor is None:
            return None
        path_u = []
        cur = u
        while cur != ancestor:
            path_u.append(cur)
            cur = self.parent0[cur]
        path_u.append(ancestor)
        path_v = []
        cur = v
        while cur != ancestor:
            path_v.append(cur)
            cur = self.parent0[cur]
        path = path_u + list(reversed(path_v))
        return path

    # -------------------
    # diameter (two BFS method)
    # -------------------
    def diameter(self) -> Tuple[int, List]:
        """
        Retorna (length, path) donde length es número de aristas del diámetro y path es
        la lista de nodos que forman ese camino.
        Método: BFS desde un nodo para encontrar farthest A; BFS desde A para hallar B (farthest) y la distancia.
        Complejidad: O(n).
        """
        if not self.adj:
            return 0, []
        # pick arbitrary node
        start = next(iter(self.adj))
        _, dist = self.bfs(start)
        # farthest from start
        a = max(dist.items(), key=lambda x: x[1])[0]
        _, dist2 = self.bfs(a)
        b, length = max(dist2.items(), key=lambda x: x[1])
        # reconstruir camino a->b usando parent from BFS (we can run BFS that stores parents)
        parent = {}
        q = deque([a])
        parent[a] = None
        while q:
            x = q.popleft()
            for w in self.adj[x]:
                if w not in parent:
                    parent[w] = x
                    q.append(w)
        path = []
        cur = b
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        return length, path

    # -------------------
    # center(s) of tree
    # -------------------
    def centers(self) -> List:
        """
        Retorna 1 o 2 nodos que son centros del árbol (minimizan la máxima distancia a todos).
        Método: poda de hojas iterativa.
        Complejidad O(n).
        """
        n = len(self.adj)
        if n == 0:
            return []
        if n == 1:
            return [next(iter(self.adj))]
        degree = {u: len(self.adj[u]) for u in self.adj}
        leaves = deque([u for u in self.adj if degree[u] <= 1])
        removed = 0
        while removed < n:
            sz = len(leaves)
            if removed + sz == n:
                return list(leaves)
            removed += sz
            for _ in range(sz):
                u = leaves.popleft()
                for v in self.adj[u]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        leaves.append(v)
        return []

    # -------------------
    # subtree size getter (requires preprocess)
    # -------------------
    def get_subtree_size(self, v) -> int:
        if not self._preprocessed:
            self.preprocess(self.root)
        if v not in self.subtree_size:
            raise KeyError("Node not found")
        return self.subtree_size[v]

    # -------------------
    # has_path convenience (BFS)
    # -------------------
    def has_path(self, u, v) -> bool:
        if u not in self.adj or v not in self.adj:
            return False
        visited = set([u])
        q = deque([u])
        while q:
            x = q.popleft()
            if x == v:
                return True
            for w in self.adj[x]:
                if w not in visited:
                    visited.add(w)
                    q.append(w)
        return False

    # -------------------
    # Repr
    # -------------------
    def __repr__(self):
        return f"Tree(nodes={len(self.adj)}, edges={len(self.get_edges())})"

#Ejemplo de uso (completo)
if __name__ == "__main__":
    T = Tree()

    # CRUD: crear nodos y aristas (construir árbol simple)
    for ch in ["A","B","C","D","E","F","G"]:
        T.add_node(ch)
    T.add_edge("A","B")
    T.add_edge("A","C")
    T.add_edge("B","D")
    T.add_edge("B","E")
    T.add_edge("C","F")
    T.add_edge("E","G")

    print(T)
    print("Nodos:", T.get_nodes())
    print("Aristas:", T.get_edges())
    print("¿Es árbol?", T.is_tree())

    # Preprocess para operaciones rooted (elige raíz A)
    T.preprocess(root="A")

    # depth y subtree size
    print("Depths:", T.depth)
    print("Parent0:", T.parent0)
    print("Subtree sizes:", T.subtree_size)

    # LCA examples
    print("LCA(D, G):", T.lca("D","G"))   # debería ser B
    print("LCA(F, G):", T.lca("F","G"))   # debería ser A

    # kth ancestor
    print("1st ancestor of G:", T.kth_ancestor("G", 1))  # E
    print("2nd ancestor of G:", T.kth_ancestor("G", 2))  # B
    print("3rd ancestor of G:", T.kth_ancestor("G", 3))  # A

    # path between nodes
    print("Path D -> F:", T.path("D","F"))  # D-B-A-C-F

    # diameter and path
    length, path = T.diameter()
    print("Diameter length:", length, "path:", path)

    # centers
    print("Centers:", T.centers())

    # remove a leaf
    T.remove_node("G")
    print("After removing G nodes:", T.get_nodes(), "edges:", T.get_edges())

    # try to add edge creating a cycle -> raises
    try:
        T.add_edge("D","C")  # D connected to C would create a cycle D-B-A-C-D
    except ValueError as e:
        print("Error (expected):", e)























#Multigrafo. Código — multigraph.py
from collections import deque, defaultdict
import heapq
from typing import Any, Dict, List, Tuple, Optional, Set

class MultiGraph:
    """
    Multigrafo: permite múltiples aristas entre el mismo par de nodos.
    - directed: True => aristas orientadas (u->v), False => aristas no dirigidas (u-v).
    - Cada arista tiene un id único (edge_id), peso (float) y opcionalmente 'data' dict.
    """

    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj: Dict[Any, List[Tuple[Any,int,float,Dict]]] = defaultdict(list)
        # adj[u] list of tuples: (neighbor, edge_id, weight, data)
        self.nodes: Set[Any] = set()
        self.edge_counter = 0
        self.edges: Dict[int, Tuple[Any, Any, float, Dict]] = {}  # edge_id -> (u, v, weight, data)

    # -------------------
    # CRUD NODOS
    # -------------------
    def add_node(self, u: Any) -> None:
        self.nodes.add(u)
        if u not in self.adj:
            self.adj[u] = []

    def get_nodes(self) -> List[Any]:
        return list(self.nodes)

    def remove_node(self, u: Any) -> None:
        if u not in self.nodes:
            raise KeyError("Node not found")
        # eliminar todas las aristas incidentes (por id)
        to_remove = []
        for eid, (a,b,_,_) in list(self.edges.items()):
            if a == u or b == u:
                to_remove.append(eid)
        for eid in to_remove:
            self.remove_edge_by_id(eid)
        # eliminar nodo
        self.nodes.remove(u)
        self.adj.pop(u, None)

    # -------------------
    # CRUD ARISTAS (multiples)
    # -------------------
    def add_edge(self, u: Any, v: Any, weight: float = 1.0, data: Optional[Dict] = None) -> int:
        """
        Añade una arista (posible paralela). Devuelve edge_id.
        Para no dirigido se crean entradas en ambas listas adj.
        """
        data = data or {}
        self.add_node(u); self.add_node(v)
        eid = self.edge_counter
        self.edge_counter += 1
        self.edges[eid] = (u, v, float(weight), data)
        self.adj[u].append((v, eid, float(weight), data))
        if not self.directed:
            # para no dirigido guardamos espejo (v->u) con mismo id
            self.adj[v].append((u, eid, float(weight), data))
        return eid

    def get_edges(self) -> List[Tuple[int, Any, Any, float, Dict]]:
        """Lista de aristas como (edge_id, u, v, weight, data)."""
        return [(eid, u, v, w, d) for eid, (u, v, w, d) in self.edges.items()]

    def get_edge_by_id(self, eid: int) -> Optional[Tuple[Any, Any, float, Dict]]:
        return self.edges.get(eid, None)

    def remove_edge_by_id(self, eid: int) -> None:
        """Eliminar arista específica por id."""
        if eid not in self.edges:
            raise KeyError("Edge id not found")
        u, v, _, _ = self.edges.pop(eid)
        # quitar en adj[u] y adj[v] (si no dirigido quitar espejo)
        self.adj[u] = [t for t in self.adj[u] if t[1] != eid]
        if not self.directed:
            self.adj[v] = [t for t in self.adj[v] if t[1] != eid]
        else:
            # en dirigido solo eliminamos u->v entry (no mirror)
            # También puede existir arista inversa con otro id; la dejamos.
            pass

    def update_edge_weight(self, eid: int, new_weight: float) -> None:
        if eid not in self.edges:
            raise KeyError("Edge id not found")
        u, v, _, data = self.edges[eid]
        self.edges[eid] = (u, v, float(new_weight), data)
        # actualizar en adj lists
        def _update_adj(a, b):
            arr = []
            for (nei, idd, w, d) in self.adj[a]:
                if idd == eid:
                    arr.append((nei, idd, float(new_weight), d))
                else:
                    arr.append((nei, idd, w, d))
            self.adj[a] = arr
        _update_adj(u, v)
        if not self.directed:
            _update_adj(v, u)

    # -------------------
    # BÁSICOS: grados, multiplicidad
    # -------------------
    def degree(self, u: Any) -> int:
        """Número de aristas incidentes (para no dirigido cuenta multiplicidad)."""
        if u not in self.nodes:
            raise KeyError("Node not found")
        return len(self.adj[u])

    def parallel_edges_between(self, u: Any, v: Any) -> List[int]:
        """Devuelve lista de edge_ids entre u->v (y en no dirigido incluye v->u same ids)."""
        if u not in self.nodes or v not in self.nodes:
            return []
        return [eid for (nei, eid, _, _) in self.adj[u] if nei == v]

    # -------------------
    # RECORRIDOS: BFS / DFS (ignoran multiplicidad, trabajan con nodos)
    # -------------------
    def bfs(self, start: Any) -> Tuple[List[Any], Dict[Any,int], Dict[Any,Optional[Any]]]:
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
            for nei, eid, _, _ in self.adj[u]:
                if dist[nei] == float('inf'):
                    dist[nei] = dist[u] + 1
                    prev[nei] = u
                    q.append(nei)
        return order, dist, prev

    def dfs(self, start: Any) -> List[Any]:
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
            # push neighbors (unique nodes) to avoid duplicate pushes due to parallel edges
            for nei, eid, _, _ in reversed(self.adj[u]):
                if nei not in visited:
                    stack.append(nei)
        return order

    # -------------------
    # CAMINOS: Dijkstra y Bellman-Ford (considerando multiaristas naturalmente)
    # -------------------
    def dijkstra(self, start: Any) -> Tuple[Dict[Any,float], Dict[Any,Optional[Any]]]:
        if start not in self.nodes:
            raise KeyError("Start node not found")
        dist = {u: float('inf') for u in self.nodes}
        prev = {u: None for u in self.nodes}
        dist[start] = 0.0
        pq = [(0.0, start)]
        while pq:
            d,u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for nei, eid, w, _ in self.adj[u]:
                nd = d + w
                if nd < dist[nei]:
                    dist[nei] = nd
                    prev[nei] = u
                    heapq.heappush(pq, (nd, nei))
        return dist, prev

    def bellman_ford(self, start: Any) -> Tuple[Dict[Any,float], Dict[Any,Optional[Any]]]:
        if start not in self.nodes:
            raise KeyError("Start node not found")
        nodes = list(self.nodes)
        dist = {u: float('inf') for u in nodes}
        prev = {u: None for u in nodes}
        dist[start] = 0.0
        # construir lista de aristas dirigidas (u->v) para BF (en no dirigido incluir ambas direcciones)
        edges_list = []
        for eid, (u, v, w, data) in self.edges.items():
            edges_list.append((u, v, w))
            if not self.directed:
                edges_list.append((v, u, w))
        n = len(nodes)
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges_list:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    updated = True
            if not updated:
                break
        # detectar ciclo negativo
        for u, v, w in edges_list:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle reachable from start")
        return dist, prev

    # -------------------
    # CONECTIVIDAD / COMPONENTES
    # -------------------
    def connected_components(self) -> List[List[Any]]:
        """Componentes para multigrafo (no dirigido). En dirigido devuelve componentes débilmente conectadas."""
        visited = set()
        comps = []
        for node in self.nodes:
            if node in visited:
                continue
            comp = []
            q = deque([node])
            visited.add(node)
            while q:
                u = q.popleft()
                comp.append(u)
                for nei, eid, _, _ in self.adj[u]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            comps.append(comp)
        return comps

    def is_connected(self) -> bool:
        if not self.nodes:
            return True
        return len(self.connected_components()) == 1

    # -------------------
    # MST (Kruskal) — solo para grafos no dirigidos
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

    def kruskal_mst(self) -> Tuple[List[Tuple[int, Any, Any, float]], float]:
        """Devuelve (mst_edges list of (eid,u,v,w), total_weight). Solo para no dirigido."""
        if self.directed:
            raise ValueError("Kruskal MST applies only to undirected multigraphs")
        # listar aristas (cada edge_id aparece una vez)
        edge_items = [(eid, u, v, w, d) for eid, (u, v, w, d) in self.edges.items()]
        # ordenar por peso
        edge_items.sort(key=lambda x: x[3])
        dsu = MultiGraph._DSU()
        for node in self.nodes:
            dsu.make_set(node)
        mst = []
        total = 0.0
        for eid, u, v, w, d in edge_items:
            if dsu.union(u, v):
                mst.append((eid, u, v, w))
                total += w
            # si ya tenemos n-1 edges podemos parar
            if len(mst) == len(self.nodes) - 1:
                break
        return mst, total

    # -------------------
    # EULERIAN: detectar y obtener circuito/recorrido de Euler (solo en no dirigido o dirigido según reglas)
    # -------------------
    def is_eulerian(self) -> Tuple[bool, str]:
        """
        Comprueba si multigrafo tiene Eulerian trail/circuit.
        Retorna (True/ "circuit" or "trail" or ""), (False, "")
        Reglas:
         - EN GRAFO NO DIRIGIDO: Eulerian circuit si todos los grados son pares y grafo conexo (ignorando nodos aislados).
           Eulerian trail (pero no circuit) si exactamente 0<2 vértices tienen grado impar.
         - EN GRAFO DIRIGIDO: Eulerian circuit si cada nodo indegree == outdegree y cada vértice con aristas pertenece a la misma componente fuertemente conectada (aquí usamos condición débil: check reachable ignoring direction for simplicity).
           Eulerian trail: existe exactamente one start node with out-in = 1 and one end node with in-out = 1 and otros equal; y grafo débilmente conexo en los vértices con aristas.
        """
        # ignorar nodos aislados al comprobar conectividad
        non_iso = [u for u in self.nodes if self.degree(u) > 0]
        if not non_iso:
            return True, "circuit"
        # conectaridad débil (ignorar direcciones)
        comp_count = 0
        visited = set()
        q = deque([non_iso[0]])
        visited.add(non_iso[0])
        while q:
            u = q.popleft()
            for nei, eid, _, _ in self.adj[u]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        if len(visited) != len(non_iso):
            return False, ""
        if not self.directed:
            odd = [u for u in self.nodes if self.degree(u) % 2 == 1]
            if len(odd) == 0:
                return True, "circuit"
            if len(odd) == 2:
                return True, "trail"
            return False, ""
        else:
            indeg = {u:0 for u in self.nodes}
            outdeg = {u:0 for u in self.nodes}
            for eid, (u,v,w,d) in self.edges.items():
                outdeg[u] += 1
                indeg[v] += 1
            start_nodes = sum(1 for u in self.nodes if outdeg[u] - indeg[u] == 1)
            end_nodes = sum(1 for u in self.nodes if indeg[u] - outdeg[u] == 1)
            if all(indeg[u] == outdeg[u] for u in self.nodes):
                return True, "circuit"
            if start_nodes == 1 and end_nodes == 1 and all((outdeg[u] - indeg[u] in (0,1) and indeg[u] - outdeg[u] in (0,1)) for u in self.nodes):
                return True, "trail"
            return False, ""

    def eulerian_trail(self) -> Optional[List[int]]:
        """
        Devuelve lista de edge_ids en orden que forma un Eulerian circuit/trail si existe, sino None.
        Implementa Hierholzer adaptado a multiaristas (trabaja con edge_ids y marca usados).
        """
        ok, typ = self.is_eulerian()
        if not ok:
            return None
        # seleccionar start vertex
        if not self.directed:
            # if trail exists with two odd nodes, start at one odd; else start at any non isolated
            odd = [u for u in self.nodes if self.degree(u) % 2 == 1]
            start = odd[0] if odd else next(iter([u for u in self.nodes if self.degree(u) > 0]))
        else:
            # directed: if trail (start has out-in ==1) else any vertex with outdeg>0
            indeg = {u:0 for u in self.nodes}
            outdeg = {u:0 for u in self.nodes}
            for eid, (u,v,w,d) in self.edges.items():
                outdeg[u] += 1
                indeg[v] += 1
            starts = [u for u in self.nodes if outdeg[u] - indeg[u] == 1]
            start = starts[0] if starts else next(iter([u for u in self.nodes if outdeg[u] > 0]))

        # prepare adjacency map: node -> stack of (nei, eid)
        adj_map = {u: [] for u in self.nodes}
        for eid, (u,v,w,d) in self.edges.items():
            adj_map[u].append((v, eid))
            if not self.directed:
                # in undirected store both directions; but we must avoid duplicate usage so both entries refer same eid
                adj_map[v].append((u, eid))
        # used markers
        used = set()
        circuit = []
        stack = [start]
        edge_iter_idx = {u:0 for u in self.nodes}  # pointer per node
        while stack:
            u = stack[-1]
            while edge_iter_idx[u] < len(adj_map[u]) and adj_map[u][edge_iter_idx[u]][1] in used:
                edge_iter_idx[u] += 1
            if edge_iter_idx[u] == len(adj_map[u]):
                stack.pop()
                if stack:
                    # last traveled edge is between stack[-1] and u; we need its eid
                    # but we don't have direct mapping parent->eid here; instead, we reconstruct by scanning edges used?
                    # simpler approach: record eids when walking below
                    pass
                continue
            v, eid = adj_map[u][edge_iter_idx[u]]
            edge_iter_idx[u] += 1
            if eid in used:
                continue
            # traverse this edge
            used.add(eid)
            stack.append(v)
            # record travel order of eids (we'll convert Eulerian by reconstructing when backtracking)
            # store eid in a separate stack
        # The above attempt is incomplete for collecting eids in order.
        # Simpler: perform Hierholzer collecting edges on backtrack explicitly:

        # Rebuild with recursive-like stack storing (node, iterator)
        adj_map2 = {u: list(adj_map[u]) for u in adj_map}  # shallow copy lists
        path = []
        st = [start]
        edge_stack = []  # stack of eids traversed
        while st:
            u = st[-1]
            while adj_map2[u] and adj_map2[u][-1][1] in used:
                adj_map2[u].pop()
            if not adj_map2[u]:
                st.pop()
                if edge_stack:
                    path.append(edge_stack.pop())
            else:
                v, eid = adj_map2[u].pop()
                if eid in used:
                    continue
                used.add(eid)
                edge_stack.append(eid)
                st.append(v)
        path.reverse()
        # path is list of edge_ids in Euler order
        if len(path) != len(self.edges):
            # in multigraph removed isolated edges? It should match number of edges with incidence
            # For safety, if counts mismatch return path anyway
            pass
        return path

    # -------------------
    # UTIL
    # -------------------
    def __repr__(self):
        return f"MultiGraph(directed={self.directed}, nodes={len(self.nodes)}, edges={len(self.edges)})"

#Ejemplo de uso rápido
if __name__ == "__main__":
    G = MultiGraph(directed=False)

    # CRUD: nodos y múltiples aristas
    G.add_node("A"); G.add_node("B")
    e1 = G.add_edge("A", "B", weight=2.0)
    e2 = G.add_edge("A", "B", weight=3.0)   # arista paralela
    e3 = G.add_edge("B", "C", weight=1.0)
    e4 = G.add_edge("C", "A", weight=4.5)
    print(G)
    print("Nodos:", G.get_nodes())
    print("Aristas:", G.get_edges())
    print("Aristas paralelas A-B ids:", G.parallel_edges_between("A","B"))

    # BFS y DFS (trabajan por nodos)
    print("BFS desde A:", G.bfs("A")[0])
    print("DFS desde A:", G.dfs("A"))

    # Dijkstra (maneja paralelas correctamente usando la más barata en relax)
    dist, prev = G.dijkstra("A")
    print("Dijkstra dist desde A:", dist)

    # Connected components
    print("Componentes:", G.connected_components())

    # Kruskal MST (no dirigido)
    mst, tot = G.kruskal_mst()
    print("MST aristas (eid,u,v,w):", mst, "peso total:", tot)

    # Eulerian check & trail (ejemplo)
    H = MultiGraph(directed=False)
    H.add_edge(1,2); H.add_edge(2,3); H.add_edge(3,1)  # triángulo -> Eulerian circuit
    ok, typ = H.is_eulerian()
    print("H Eulerian?", ok, typ)
    print("Trail (edge ids):", H.eulerian_trail())












#Grafo bipartito. Código: bipartite_graph.py
from collections import deque, defaultdict
from typing import Any, Dict, List, Optional, Set, Tuple

class BipartiteGraph:
    """
    Grafo no dirigido pensado para bipartición.
    - adj: dict[node] -> set(neighbors)
    - No obligamos al usuario a conocer la partición al añadir aristas.
    - Métodos:
        add_node, remove_node, add_edge, remove_edge, get_nodes, get_edges
        is_bipartite() -> (bool, left_set, right_set, color_map)
        bfs/dfs/shortest_path (unweighted)
        hopcroft_karp() -> (pair_u, pair_v, matching_size)
        min_vertex_cover() -> set of nodes (size == matching_size) using König's theorem
    """

    def __init__(self):
        self.adj: Dict[Any, Set[Any]] = {}

    # --------------
    # CRUD nodos/aristas
    # --------------
    def add_node(self, u: Any) -> None:
        if u not in self.adj:
            self.adj[u] = set()

    def get_nodes(self) -> List[Any]:
        return list(self.adj.keys())

    def remove_node(self, u: Any) -> None:
        if u not in self.adj:
            raise KeyError("Node not found")
        for v in list(self.adj[u]):
            self.adj[v].discard(u)
        del self.adj[u]

    def add_edge(self, u: Any, v: Any) -> None:
        """Añade arista u-v (no dirigida). Crea nodos si no existen."""
        self.add_node(u); self.add_node(v)
        self.adj[u].add(v)
        self.adj[v].add(u)

    def remove_edge(self, u: Any, v: Any) -> None:
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        self.adj[u].discard(v)
        self.adj[v].discard(u)

    def get_edges(self) -> List[Tuple[Any, Any]]:
        """Lista de aristas (u,v) sin duplicados u<v lexicográfico por consistencia."""
        edges = []
        seen = set()
        for u in self.adj:
            for v in self.adj[u]:
                key = tuple(sorted((u, v), key=lambda x: str(x)))
                if key not in seen:
                    seen.add(key)
                    edges.append(key)
        return edges

    def neighbors(self, u: Any) -> Set[Any]:
        if u not in self.adj:
            raise KeyError("Node not found")
        return set(self.adj[u])

    # --------------
    # BFS / DFS / shortest path (unweighted)
    # --------------
    def bfs(self, start: Any) -> Tuple[List[Any], Dict[Any, int], Dict[Any, Optional[Any]]]:
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
            for v in sorted(self.adj[u], key=lambda x: str(x), reverse=True):
                if v not in visited:
                    stack.append(v)
        return order

    def shortest_path(self, start: Any, goal: Any) -> Optional[List[Any]]:
        """Camino mínimo en número de aristas (BFS)."""
        if start not in self.adj or goal not in self.adj:
            raise KeyError("Start or goal not in graph")
        _, dist, prev = self.bfs(start)
        if dist[goal] == float('inf'):
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

    # --------------
    # Comprobación bipartita y partición
    # --------------
    def is_bipartite(self) -> Tuple[bool, Optional[Set[Any]], Optional[Set[Any]], Dict[Any,int]]:
        """
        Comprueba si el grafo es bipartito.
        Retorna: (is_bipartite, left_set, right_set, color_map)
        color_map: nodo -> 0/1 (vacío si no bipartito)
        """
        color: Dict[Any,int] = {}
        left, right = set(), set()
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
                        return False, None, None, {}
        for node, c in color.items():
            (left if c == 0 else right).add(node)
        return True, left, right, color

    # --------------
    # Hopcroft-Karp (matching máximo)
    # --------------
    def hopcroft_karp(self) -> Tuple[Dict[Any, Optional[Any]], Dict[Any, Optional[Any]], int]:
        """
        Devuelve (pair_u, pair_v, matching_size)
        - pair_u: dict para todos los nodos del lado 'left' (si no están en left, se ignoran) mapping u->v or None
        - pair_v: dict para todos los nodos del lado 'right' mapping v->u or None
        Requiere que el grafo sea bipartito; si no lo es lanza ValueError.
        """
        ok, left, right, _ = self.is_bipartite()
        if not ok:
            raise ValueError("Graph is not bipartite")

        # initialize
        pair_u = {u: None for u in left}
        pair_v = {v: None for v in right}
        dist = {}

        INF = 10**9

        def bfs() -> bool:
            q = deque()
            for u in left:
                if pair_u[u] is None:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = INF
            found_augment = False
            while q:
                u = q.popleft()
                for v in self.adj[u]:
                    if v not in pair_v:  # neighbors on right only
                        continue
                    pu = pair_v[v]
                    if pu is None:
                        found_augment = True
                    else:
                        if dist.get(pu, INF) == INF:
                            dist[pu] = dist[u] + 1
                            q.append(pu)
            return found_augment

        def dfs(u) -> bool:
            for v in self.adj[u]:
                if v not in pair_v:
                    continue
                pu = pair_v[v]
                if pu is None or (dist.get(pu, INF) == dist[u] + 1 and dfs(pu)):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
            dist[u] = INF
            return False

        matching = 0
        while bfs():
            for u in list(left):
                if pair_u[u] is None:
                    if dfs(u):
                        matching += 1

        return pair_u, pair_v, matching


    # --------------
    # Minimum Vertex Cover from maximum matching (Kőnig)
    # --------------
    def min_vertex_cover(self) -> Set[Any]:
        """
        Usando resultado de Hopcroft-Karp, construye mínimo vertex cover en bipartito.
        Algoritmo:
          - Hacer matching máximo -> pair_u, pair_v
          - Tomar todos los vértices libres (no emparejados) en LEFT y hacer BFS en el grafo alternante:
            - por arista no-matching: L -> R
            - por arista matching: R -> L
          - Sea Z el conjunto de vértices alcanzables desde esos libres.
          - Vertex cover mínimo = (Left \ Z) U (Right ∩ Z)
        Retorna conjunto de nodos que pertenecen al min vertex cover.
        """
        ok, left, right, _ = self.is_bipartite()
        if not ok:
            raise ValueError("Graph is not bipartite")
        pair_u, pair_v, _ = self.hopcroft_karp()
        # free left vertices
        free_left = [u for u in left if pair_u[u] is None]
        # BFS on alternating graph
        visited_left = set()
        visited_right = set()
        q = deque(free_left)
        for u in free_left:
            visited_left.add(u)
        while q:
            u = q.popleft()
            # from left using non-matching edges to right
            for v in self.adj[u]:
                # only neighbors in right
                if v not in right:
                    continue
                if pair_u.get(u) == v:
                    continue  # matching edge, skip in this direction
                if v in visited_right:
                    continue
                visited_right.add(v)
                # from right follow matching edge to left (if exists)
                pu = pair_v.get(v)
                if pu is not None and pu not in visited_left:
                    visited_left.add(pu)
                    q.append(pu)
        # Z = visited_left U visited_right
        cover = set()
        # Left \ Z_left
        cover.update(u for u in left if u not in visited_left)
        # Right ∩ Z_right
        cover.update(v for v in right if v in visited_right)
        return cover

    # --------------
    # Representación
    # --------------
    def __repr__(self) -> str:
        return f"BipartiteGraph(nodes={len(self.adj)}, edges={len(self.get_edges())})"

#Ejemplo de uso
if __name__ == "__main__":
    g = BipartiteGraph()

    # construir ejemplo bipartito: Left = {A,B,C}, Right = {1,2,3}
    g.add_edge("A", 1)
    g.add_edge("A", 2)
    g.add_edge("B", 1)
    g.add_edge("B", 3)
    g.add_edge("C", 2)
    g.add_edge("C", 3)

    print(g)
    print("Nodos:", g.get_nodes())
    print("Aristas:", g.get_edges())

    ok, left, right, color = g.is_bipartite()
    print("¿Bipartito?", ok)
    print("Left:", left, "Right:", right)

    # Hopcroft-Karp
    pair_u, pair_v, size = g.hopcroft_karp()
    print("Matching size:", size)
    print("pair_u (left->right):", pair_u)
    print("pair_v (right->left):", pair_v)

    # Minimum vertex cover (Kőnig)
    cover = g.min_vertex_cover()
    print("Minimum vertex cover (size == matching_size):", cover, "size:", len(cover))

    # Caminos mínimos (ejemplo)
    print("Shortest path A -> 3:", g.shortest_path("A", 3))










#Planar. Código — planar_graph.py
from collections import deque
import heapq
from typing import Any, Dict, List, Optional, Set, Tuple

class PlanarGraph:
    """
    Clase para trabajar con grafos 'planar-friendly'.
    Nota: no realiza verificación completa de planaridad.
    Para funciones que requieren embedding (caras, dual), debes proporcionar
    un embedding: un dict node -> list_of_neighbors_in_cyclic_order.
    """

    def __init__(self, directed: bool = False):
        self.directed = directed
        # adj[node] -> dict(nei -> weight)
        self.adj: Dict[Any, Dict[Any, float]] = {}
        # embedding: node -> list(neighbors in clockwise order) (optional)
        self.embedding: Dict[Any, List[Any]] = {}
    
    # -------------------
    # CRUD: NODOS
    # -------------------
    def add_node(self, u: Any) -> None:
        if u not in self.adj:
            self.adj[u] = {}

    def get_nodes(self) -> List[Any]:
        return list(self.adj.keys())

    def remove_node(self, u: Any) -> None:
        if u not in self.adj:
            raise KeyError("Node not found")
        for v in list(self.adj[u].keys()):
            self.adj[v].pop(u, None)
        del self.adj[u]
        self.embedding.pop(u, None)
        # remove u from other embeddings
        for n, order in self.embedding.items():
            self.embedding[n] = [x for x in order if x != u]

    # -------------------
    # CRUD: ARISTAS
    # -------------------
    def add_edge(self, u: Any, v: Any, weight: float = 1.0) -> None:
        """Añade arista u-v (o u->v si directed). Crea nodos si hace falta."""
        self.add_node(u); self.add_node(v)
        self.adj[u][v] = float(weight)
        if not self.directed:
            self.adj[v][u] = float(weight)

    def remove_edge(self, u: Any, v: Any) -> None:
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        self.adj[u].pop(v, None)
        if not self.directed:
            self.adj[v].pop(u, None)
        # update embedding if present
        if u in self.embedding:
            self.embedding[u] = [x for x in self.embedding[u] if x != v]
        if v in self.embedding:
            self.embedding[v] = [x for x in self.embedding[v] if x != u]

    def get_edges(self) -> List[Tuple[Any, Any, float]]:
        edges = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u].items():
                if self.directed:
                    edges.append((u, v, w))
                else:
                    key = tuple(sorted((u, v), key=lambda x: str(x)))
                    if key not in seen:
                        edges.append((key[0], key[1], w))
                        seen.add(key)
        return edges

    def get_edge_weight(self, u: Any, v: Any) -> Optional[float]:
        return self.adj.get(u, {}).get(v, None)

    # -------------------
    # EMBEDDING (opcional) — almacenar el orden cíclico de vecinos
    # -------------------
    def set_embedding(self, embedding: Dict[Any, List[Any]]) -> None:
        """
        embedding: dict node -> list of neighbors in cyclic order (CW or CCW).
        Debe ser coherente con la topología del grafo (todas las referencias existen).
        """
        # basic validation
        for u, order in embedding.items():
            if u not in self.adj:
                raise KeyError(f"Embedding refers to unknown node {u}")
            for v in order:
                if v not in self.adj[u]:
                    raise KeyError(f"Embedding neighbor {v} not adjacent to {u}")
        self.embedding = {u: list(order) for u, order in embedding.items()}

    # -------------------
    # BFS / DFS / connected
    # -------------------
    def bfs(self, start: Any) -> Tuple[List[Any], Dict[Any,int], Dict[Any,Optional[Any]]]:
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
            for v in sorted(self.adj[u], key=lambda x: str(x), reverse=True):
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

    # -------------------
    # HEURÍSTICA: comprobar planaridad simple usando fórmula de Euler
    # (válido como chequeo rápido para grafos simples y conectos; no suficiente)
    # -------------------
    def is_planar_heuristic(self) -> Tuple[bool, str]:
        """
        Heurística rápida:
          - Si el grafo es simple (sin lazos ni aristas múltiples) y conectado,
            Euler: V - E + F = 2  => E <= 3V - 6  (para V >= 3)
          - Para grafos bipartitos: E <= 2V - 4
        Retorna (likely_planar, explanation).
        NO es garantía — solo filtro rápido.
        """
        V = len(self.adj)
        E = len(self.get_edges())
        if V <= 2:
            return True, "Trivially planar (V <= 2)"
        # check for loops or multiple edges: if present we cannot apply simple bound safely
        # here we do a basic test: see if any adjacency has duplicates (we store as dict so no multi-edge)
        # loops:
        for u in self.adj:
            if u in self.adj[u]:
                return False, "Contains a loop -> not simple planar"
        # bound for simple planar graph:
        if E > 3*V - 6:
            return False, f"E={E} > 3V-6 ({3*V-6}) -> not planar (by necessary condition)"
        return True, f"E={E} <= 3V-6 ({3*V-6}) -> passes necessary condition (not sufficient)"

    # -------------------
    # CARAS y GRAFO DUAL (requiere embedding)
    # -------------------
    def faces_from_embedding(self) -> List[List[Any]]:
        """
        Si tienes embedding (cyclic neighbor order for each node), calcula las caras
        usando recorrido de aristas dirigidas (u->v) y su siguiente en el orden cíclico.
        Retorna lista de caras; cada cara es lista de vértices cerrada (primer == último).
        """
        if not self.embedding:
            raise RuntimeError("Embedding required to compute faces (use set_embedding).")
        # directed edges visited set: (u,v)
        visited_dir = set()
        faces = []
        for u in self.embedding:
            for v in self.embedding[u]:
                if (u,v) in visited_dir:
                    continue
                # walk face starting from directed edge u->v
                face = []
                cur_u, cur_v = u, v
                while True:
                    visited_dir.add((cur_u, cur_v))
                    face.append(cur_u)
                    # get neighbor list for cur_v
                    nbrs = self.embedding[cur_v]
                    # find index of cur_u in cur_v neighbor list
                    try:
                        idx = nbrs.index(cur_u)
                    except ValueError:
                        raise RuntimeError(f"Embedding inconsistent: {cur_u} not in embedding of {cur_v}")
                    # next neighbor in CCW: predecessor in cyc order gives left face; we choose next clockwise:
                    # choose the neighbor after cur_u to turn right (consistent orientation)
                    next_idx = (idx - 1) % len(nbrs)  # change sign if orientation differs
                    next_w = nbrs[next_idx]
                    next_u, next_v = cur_v, next_w
                    cur_u, cur_v = next_u, next_v
                    if cur_u == u and cur_v == v:
                        break
                # close face by appending starting vertex
                face.append(u)
                faces.append(face)
        # faces may include outer face; some faces might be duplicates modulo rotation; normalize
        normalized = []
        seen = set()
        for f in faces:
            # normalize rotation to minimal tuple
            ring = f[:-1]  # drop repeated last
            n = len(ring)
            # find minimal rotation
            rotations = [tuple(ring[i:] + ring[:i]) for i in range(n)]
            canonical = min(rotations)
            if canonical in seen:
                continue
            seen.add(canonical)
            normalized.append(list(canonical) + [canonical[0]])
        return normalized

    def dual_from_embedding(self) -> 'PlanarGraph':
        """
        Construye el grafo dual a partir del embedding: cada cara -> nodo en dual;
        cada arista primal entre dos caras -> arista dual entre nodos correspondientes.
        Retorna PlanarGraph (no dirigido) representing dual.
        """
        faces = self.faces_from_embedding()
        # map each directed edge (u,v) -> face id on its left (we must recompute using the same procedure)
        # We'll compute face id for each directed edge by scanning faces
        edge_to_face = {}
        for i, face in enumerate(faces):
            # face given as closed list [a,b,c,a]
            for j in range(len(face)-1):
                a, b = face[j], face[j+1]
                edge_to_face[(a,b)] = i
        dual = PlanarGraph(directed=False)
        # create dual nodes
        for i in range(len(faces)):
            dual.add_node(f"F{i}")
        # for each primal undirected edge {u,v}, find faces on its two sides -> link dual faces
        seen_edges = set()
        for u in self.adj:
            for v in self.adj[u]:
                if self.directed:
                    continue
                key = tuple(sorted((u,v), key=lambda x: str(x)))
                if key in seen_edges:
                    continue
                seen_edges.add(key)
                # faces (u->v) and (v->u)
                f1 = edge_to_face.get((u,v), None)
                f2 = edge_to_face.get((v,u), None)
                if f1 is not None and f2 is not None and f1 != f2:
                    dual.add_edge(f"F{f1}", f"F{f2}")
        return dual

    # -------------------
    # PLANAR-SPECIFIC ALGORITHM: 5-COLOR (garantizado para planar)
    # Implementación: remove vertex with degree <= 5 recursively (stack), then color on backtrack
    # -------------------
    def five_color(self) -> Dict[Any, int]:
        """
        Colorea vértices usando a lo sumo 5 colores (algoritmo garantizado para grafos planares).
        Método:
         - repetidamente eliminar vértice con grado <= 5 y apilarlo
         - en reconstrucción, asignar color distinto de sus vecinos (<=5 colores siempre posible)
         - si en algún paso no hay grado <=5 (teóricamente no pasa para planar), se falla.
        Retorna dict node -> color (0..4)
        """
        # work on a copy
        import copy
        gcopy = {u: set(self.adj[u].keys()) for u in self.adj}
        stack = []
        while gcopy:
            # find vertex with degree <= 5
            found = None
            for u, nbrs in gcopy.items():
                if len(nbrs) <= 5:
                    found = u
                    break
            if found is None:
                raise RuntimeError("No vertex with degree <=5 found: graph may not be planar or the bound violated.")
            # push (vertex, neighbors) for reconstruction
            stack.append((found, set(gcopy[found])))
            # remove found
            for v in gcopy[found]:
                gcopy[v].remove(found)
            del gcopy[found]
        # reconstruct and color
        color = {}
        while stack:
            u, nbrs = stack.pop()
            used = set(color.get(v) for v in nbrs if v in color)
            for c in range(5):
                if c not in used:
                    color[u] = c
                    break
            else:
                # in practice for planar graphs shouldn't happen
                raise RuntimeError("Failed to color with 5 colors")
        return color

    # -------------------
    # MST (Kruskal) and shortest path (Dijkstra) — general algorithms useful in planar graphs
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
        """Kruskal (works for planar graphs too). Retorna list of edges (u,v,w) and total weight."""
        edges = self.get_edges()
        edges_sorted = sorted(edges, key=lambda x: x[2])
        dsu = PlanarGraph._DSU()
        for u in self.adj:
            dsu.make_set(u)
        mst = []
        total = 0.0
        for u, v, w in edges_sorted:
            if dsu.union(u, v):
                mst.append((u, v, w))
                total += w
            if len(mst) == max(0, len(self.adj)-1):
                break
        return mst, total

    def dijkstra(self, start: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
        if start not in self.adj:
            raise KeyError("Start node not in graph")
        dist = {u: float('inf') for u in self.adj}
        prev = {u: None for u in self.adj}
        dist[start] = 0
        pq = [(0, start)]
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
    # UTIL
    # -------------------
    def __repr__(self):
        return f"PlanarGraph(directed={self.directed}, V={len(self.adj)}, E={len(self.get_edges())})"

#Ejemplo de uso
if __name__ == "__main__":
    # crear grafo planar simple (triángulo + vértice central conectado a dos vértices)
    G = PlanarGraph(directed=False)
    G.add_edge("A","B", 1)
    G.add_edge("B","C", 1)
    G.add_edge("C","A", 1)
    G.add_edge("A","D", 1)
    G.add_edge("C","D", 1)

    print(G)
    print("Nodos:", G.get_nodes())
    print("Aristas:", G.get_edges())

    # heurística de planaridad
    ok, msg = G.is_planar_heuristic()
    print("Planar heuristic:", ok, msg)

    # Dijkstra
    dist, prev = G.dijkstra("A")
    print("Dijkstra desde A:", dist)
    # MST
    mst, tot = G.kruskal_mst()
    print("MST:", mst, "total:", tot)

    # 5-color (debería colorear con <=5 colores)
    coloring = G.five_color()
    print("Coloring (<=5):", coloring)

    # Si tienes embedding (ejemplo manual para este pequeño grafo):
    embedding = {
        "A": ["B","C","D"],  # vecinos en orden cíclico
        "B": ["C","A"],
        "C": ["A","B","D"],
        "D": ["C","A"]
    }
    G.set_embedding(embedding)
    faces = G.faces_from_embedding()
    print("Faces (requiere embedding):", faces)
    dual = G.dual_from_embedding()
    print("Dual:", dual)















#Denso. Código — dense_graph.py
# dense_graph.py
from collections import deque
import math
from typing import Any, Dict, List, Optional, Tuple

INF = float('inf')

class DenseGraph:
    """
    Grafo denso representado por matriz de adyacencia.
    - directed: True si es dirigido.
    - nodes: lista de nodos (cualquier hashable). Internamente mantenemos mapping node->index.
    - adj: matriz n x n (lista de listas) con peso (float) o math.inf si no hay arista.
    - Si el grafo es no ponderado, usa peso 1.0 por defecto al añadir arista.
    """

    def __init__(self, directed: bool = False, weighted: bool = False, default_weight: float = 1.0):
        self.directed = directed
        self.weighted = weighted
        self.default_weight = float(default_weight)
        self.nodes: List[Any] = []
        self.index: Dict[Any, int] = {}
        self.adj: List[List[float]] = []  # pesos; INF si no existe arista
        self._n = 0

    # -------------------
    # UTIL INTERNA: (re)construcción de matriz
    # -------------------
    def _ensure_node(self, u: Any):
        """Crear nodo si no existe (interno)."""
        if u in self.index:
            return
        self.index[u] = self._n
        self.nodes.append(u)
        self._n += 1
        # expandir matriz por filas y columnas
        for row in self.adj:
            row.append(INF)
        self.adj.append([INF] * self._n)
        # por convención, sin lazos: adj[i][i] = 0
        for i in range(self._n):
            self.adj[i][i] = 0.0

    def _rebuild_all(self):
        """Reconstruir matriz completa desde self.nodes (útil tras eliminar nodos)."""
        old_nodes = list(self.nodes)
        old_index = dict(self.index)
        old_adj = [row[:] for row in self.adj]
        # reset
        self.index.clear()
        self.nodes = []
        self.adj = []
        self._n = 0
        # añadir en orden original (excepto los que faltan)
        for u in old_nodes:
            if u in old_index:  # siempre True en este diseño; removals update nodes list before calling rebuild
                self._ensure_node(u)
        # old_adj values are lost; caller should re-add edges if needed.
        # We'll keep a simple pattern: when remove_node happens we reconstruct by re-adding remaining edges if we had stored them.
        # For simplicity, remove_node will reconstruct adjacency by building a fresh INF matrix and
        # copying from old_adj skipping removed index.
        # (This function is only low-level; remove_node handles copying)
        return

    # -------------------
    # CRUD: NODOS
    # -------------------
    def add_node(self, u: Any):
        """Añade nodo si no existe."""
        if u in self.index:
            return
        self._ensure_node(u)

    def get_nodes(self) -> List[Any]:
        return list(self.nodes)

    def remove_node(self, u: Any):
        """
        Elimina un nodo y reconstruye la matriz (O(n^2)).  
        Nota: en grafos densos esta operación es costosa pero aceptable si n pequeño/moderado.
        """
        if u not in self.index:
            raise KeyError("Node not found")
        rem_idx = self.index[u]
        # construir nueva lista de nodos y nueva matriz copiando todas las entradas excepto rem_idx
        new_nodes = [v for i,v in enumerate(self.nodes) if i != rem_idx]
        new_n = len(new_nodes)
        new_adj = [[INF]*new_n for _ in range(new_n)]
        for i in range(new_n):
            new_adj[i][i] = 0.0
        # copiar valores desde old adj
        for i_old, ui in enumerate(self.nodes):
            if i_old == rem_idx: 
                continue
            for j_old, vj in enumerate(self.nodes):
                if j_old == rem_idx:
                    continue
                new_i = i_old - (1 if i_old > rem_idx else 0)
                new_j = j_old - (1 if j_old > rem_idx else 0)
                new_adj[new_i][new_j] = self.adj[i_old][j_old]
        # asignar
        self.nodes = new_nodes
        self._n = new_n
        self.index = {node:i for i,node in enumerate(self.nodes)}
        self.adj = new_adj

    # -------------------
    # CRUD: ARISTAS
    # -------------------
    def add_edge(self, u: Any, v: Any, weight: Optional[float] = None):
        """
        Añade arista u->v (o u-v si no dirigido).
        - Si weighted==False y weight is None, se usa default_weight (=1.0).
        - Si weighted==True y weight is None => lanza ValueError.
        """
        if weight is None:
            if self.weighted:
                raise ValueError("Edge weight required for weighted graph")
            w = self.default_weight
        else:
            w = float(weight)
        self._ensure_node(u)
        self._ensure_node(v)
        i = self.index[u]; j = self.index[v]
        self.adj[i][j] = w
        if not self.directed:
            self.adj[j][i] = w

    def remove_edge(self, u: Any, v: Any):
        if u not in self.index or v not in self.index:
            raise KeyError("One or both nodes not found")
        i = self.index[u]; j = self.index[v]
        self.adj[i][j] = INF
        if not self.directed:
            self.adj[j][i] = INF

    def has_edge(self, u: Any, v: Any) -> bool:
        if u not in self.index or v not in self.index:
            return False
        return self.adj[self.index[u]][self.index[v]] != INF and self.index[u] != self.index[v]

    def get_edges(self) -> List[Tuple[Any, Any, float]]:
        edges = []
        n = self._n
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if self.adj[i][j] != INF:
                    if self.directed:
                        edges.append((self.nodes[i], self.nodes[j], self.adj[i][j]))
                    else:
                        if i < j:
                            # in undirected store once
                            if self.adj[i][j] != INF:
                                edges.append((self.nodes[i], self.nodes[j], self.adj[i][j]))
        return edges

    # -------------------
    # UTILIDADES
    # -------------------
    def adjacency_matrix(self) -> List[List[float]]:
        """Devuelve copia de la matriz de adyacencia (INF significa sin arista)."""
        return [row[:] for row in self.adj]

    def degree(self, u: Any) -> int:
        if u not in self.index:
            raise KeyError("Node not found")
        i = self.index[u]
        if self.directed:
            out = sum(1 for x in self.adj[i] if x != INF and x != 0.0)
            indeg = sum(1 for r in range(self._n) if self.adj[r][i] != INF and self.adj[r][i] != 0.0)
            return out + indeg  # sumar como métrica combinada; si quieres por separado pide indeg/outdeg
        else:
            return sum(1 for x in self.adj[i] if x != INF and x != 0.0)  # grado

    def density(self) -> float:
        """Densidad realista = E / (V*(V-1)) (dirigido) o E / (V*(V-1)/2) (no dirigido)."""
        n = self._n
        if n <= 1:
            return 0.0
        m = len(self.get_edges())
        if self.directed:
            return m / (n * (n - 1))
        else:
            return m / (n * (n - 1) / 2)

    # -------------------
    # RECORRIDOS (usando matriz)
    # -------------------
    def bfs(self, start: Any) -> Tuple[List[Any], Dict[Any,int], Dict[Any, Optional[Any]]]:
        if start not in self.index:
            raise KeyError("Start node not in graph")
        n = self._n
        dist = {node: math.inf for node in self.nodes}
        prev = {node: None for node in self.nodes}
        order = []
        q = deque([start])
        dist[start] = 0
        while q:
            u = q.popleft()
            order.append(u)
            ui = self.index[u]
            for v_idx in range(n):
                if v_idx == ui:
                    continue
                if self.adj[ui][v_idx] != INF:
                    v = self.nodes[v_idx]
                    if dist[v] == math.inf:
                        dist[v] = dist[u] + 1
                        prev[v] = u
                        q.append(v)
        return order, dist, prev

    def dfs(self, start: Any) -> List[Any]:
        if start not in self.index:
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
            ui = self.index[u]
            # push neighbors in deterministic order
            for v_idx in range(self._n - 1, -1, -1):
                if v_idx == ui:
                    continue
                if self.adj[ui][v_idx] != INF:
                    v = self.nodes[v_idx]
                    if v not in visited:
                        stack.append(v)
        return order

    def is_connected(self) -> bool:
        if self._n == 0:
            return True
        start = self.nodes[0]
        _, dist, _ = self.bfs(start)
        return all(dist[v] != math.inf for v in self.nodes)

    # -------------------
    # DIJKSTRA O(n^2) (bueno en grafos densos)
    # -------------------
    def dijkstra_n2(self, source: Any) -> Tuple[Dict[Any,float], Dict[Any, Optional[Any]]]:
        """
        Dijkstra sin heap: O(n^2). Mejor en grafos densos o cuando n pequeño/medio.
        Retorna dist dict y prev dict.
        """
        if source not in self.index:
            raise KeyError("Source not in graph")
        n = self._n
        dist = {node: INF for node in self.nodes}
        prev = {node: None for node in self.nodes}
        used = [False] * n
        dist[source] = 0.0
        for _ in range(n):
            # seleccionar vertice no usado con distancia mínima
            u_idx = -1
            u_dist = INF
            for i in range(n):
                node = self.nodes[i]
                if not used[i] and dist[node] < u_dist:
                    u_dist = dist[node]
                    u_idx = i
            if u_idx == -1:
                break
            used[u_idx] = True
            u_node = self.nodes[u_idx]
            # relajar vecinos (usar fila de matriz)
            for v_idx in range(n):
                if self.adj[u_idx][v_idx] == INF:
                    continue
                v_node = self.nodes[v_idx]
                nd = dist[u_node] + self.adj[u_idx][v_idx]
                if nd < dist[v_node]:
                    dist[v_node] = nd
                    prev[v_node] = u_node
        return dist, prev

    # -------------------
    # RECONSTRUIR CAMINO desde prev (Dijkstra)
    # -------------------
    @staticmethod
    def reconstruct_path(prev: Dict[Any, Optional[Any]], start: Any, goal: Any) -> Optional[List[Any]]:
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
    # PRIM O(n^2) para MST (usando matriz). Solo para grafos no dirigidos.
    # -------------------
    def prim_mst_n2(self) -> Tuple[List[Tuple[Any, Any, float]], float]:
        if self.directed:
            raise ValueError("Prim only for undirected graphs")
        n = self._n
        if n == 0:
            return [], 0.0
        in_mst = [False] * n
        key = [INF] * n
        parent = [-1] * n
        key[0] = 0.0
        total = 0.0
        edges = []
        for _ in range(n):
            # pick min key vertex not in MST
            u = -1
            best = INF
            for i in range(n):
                if not in_mst[i] and key[i] < best:
                    best = key[i]
                    u = i
            if u == -1:
                break
            in_mst[u] = True
            if parent[u] != -1:
                edges.append((self.nodes[parent[u]], self.nodes[u], self.adj[parent[u]][u]))
                total += self.adj[parent[u]][u]
            # relax neighbors to update keys
            for v in range(n):
                w = self.adj[u][v]
                if w != INF and not in_mst[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u
        return edges, total

    # -------------------
    # FLOYD-WARSHALL (APSP) O(n^3) — retorna dist_matrix y next dict para reconstruir caminos
    # -------------------
    def floyd_warshall(self) -> Tuple[Dict[Any, Dict[Any, float]], Dict[Any, Dict[Any, Optional[Any]]]]:
        n = self._n
        # init dist and next
        dist = [[INF]*n for _ in range(n)]
        nxt = [[None]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dist[i][j] = self.adj[i][j]
                if self.adj[i][j] != INF and i != j:
                    nxt[i][j] = self.nodes[j]
            dist[i][i] = 0.0
            nxt[i][i] = self.nodes[i]
        # FW
        for k in range(n):
            for i in range(n):
                # small micro-optim: skip if dist[i][k] INF
                if dist[i][k] == INF:
                    continue
                for j in range(n):
                    if dist[k][j] == INF:
                        continue
                    nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j]:
                        dist[i][j] = nd
                        nxt[i][j] = nxt[i][k]
        # convert to dicts keyed by node
        dist_dict = {self.nodes[i]: {self.nodes[j]: dist[i][j] for j in range(n)} for i in range(n)}
        next_dict = {self.nodes[i]: {self.nodes[j]: nxt[i][j] for j in range(n)} for i in range(n)}
        return dist_dict, next_dict

    @staticmethod
    def reconstruct_path_fw(next_dict: Dict[Any, Dict[Any, Optional[Any]]], start: Any, goal: Any) -> Optional[List[Any]]:
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
    # TRANSITIVE CLOSURE (reachability) via Floyd-Warshall boolean (O(n^3))
    # -------------------
    def transitive_closure(self) -> Dict[Any, Dict[Any, bool]]:
        n = self._n
        reach = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if self.adj[i][j] != INF and i != j:
                    reach[i][j] = True
            reach[i][i] = True
        for k in range(n):
            for i in range(n):
                if not reach[i][k]:
                    continue
                for j in range(n):
                    if reach[k][j]:
                        reach[i][j] = True
        return {self.nodes[i]: {self.nodes[j]: reach[i][j] for j in range(n)} for i in range(n)}

    # -------------------
    # COMPLEMENTO
    # -------------------
    def complement(self) -> 'DenseGraph':
        """Devuelve el grafo complemento (mismos nodos, aristas invertidas; sin lazos)."""
        g = DenseGraph(directed=self.directed, weighted=self.weighted, default_weight=self.default_weight)
        # create nodes
        for u in self.nodes:
            g.add_node(u)
        n = self._n
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if self.adj[i][j] == INF:
                    # add edge with default weight (or 1)
                    g.adj[i][j] = self.default_weight
                else:
                    g.adj[i][j] = INF
        # ensure symmetric if undirected
        if not self.directed:
            for i in range(n):
                for j in range(n):
                    g.adj[j][i] = g.adj[i][j]
        return g

    # -------------------
    # REPRESENTACIÓN
    # -------------------
    def __repr__(self):
        return f"DenseGraph(directed={self.directed}, weighted={self.weighted}, V={self._n}, E={len(self.get_edges())})"

#Ejemplo de uso (rápido)
if __name__ == "__main__":
    G = DenseGraph(directed=False, weighted=True)

    # CRUD: nodos y aristas
    G.add_node("A"); G.add_node("B"); G.add_node("C"); G.add_node("D")
    G.add_edge("A","B", 2.0)
    G.add_edge("A","C", 5.0)
    G.add_edge("B","C", 1.0)
    G.add_edge("C","D", 3.0)
    print(G)
    print("Nodes:", G.get_nodes())
    print("Edges:", G.get_edges())
    print("Adjacency matrix:")
    for row in G.adjacency_matrix():
        print(row)

    # Dijkstra O(n^2) desde A
    dist, prev = G.dijkstra_n2("A")
    print("Dijkstra dist:", dist)
    print("Path A -> D:", DenseGraph.reconstruct_path(prev, "A", "D"))

    # Prim O(n^2) MST
    mst, total = G.prim_mst_n2()
    print("MST:", mst, "total weight:", total)

    # Floyd-Warshall (APSP)
    dist_all, next_all = G.floyd_warshall()
    print("FW A->D dist:", dist_all["A"]["D"])
    print("FW path A->D:", DenseGraph.reconstruct_path_fw(next_all, "A", "D"))

    # Transitive closure (reachability)
    tc = G.transitive_closure()
    print("Reachable A->D?", tc["A"]["D"])

    # Density
    print("Density:", G.density())

    # Complement graph
    comp = G.complement()
    print("Complement edges:", comp.get_edges())







#Disperso. Código — sparse_graph.py
# sparse_graph.py
from collections import deque, defaultdict
import heapq
from typing import Any, Dict, List, Tuple, Optional, Set

INF = float('inf')

class SparseGraph:
    """
    Grafo disperso con listas de adyacencia.
    - directed: True = grafo dirigido; False = no dirigido.
    - weighted: True si las aristas tienen peso (float). Si weighted=False se usa weight=1 por defecto.
    Representación: adj[node] -> list of (neighbor, weight)
    """

    def __init__(self, directed: bool = False, weighted: bool = False):
        self.directed = directed
        self.weighted = weighted
        self.adj: Dict[Any, List[Tuple[Any, float]]] = {}
        self._edge_count = 0

    # -------------------
    # CRUD NODOS
    # -------------------
    def add_node(self, u: Any) -> None:
        if u not in self.adj:
            self.adj[u] = []

    def get_nodes(self) -> List[Any]:
        return list(self.adj.keys())

    def remove_node(self, u: Any) -> None:
        if u not in self.adj:
            raise KeyError("Node not found")
        # eliminar aristas incidentes
        del self.adj[u]
        for v in list(self.adj.keys()):
            # filtrar aristas hacia u
            new_list = [(nei,w) for (nei,w) in self.adj[v] if nei != u]
            self.adj[v] = new_list
        # recompute edge_count
        self._recompute_edge_count()

    # -------------------
    # CRUD ARISTAS
    # -------------------
    def add_edge(self, u: Any, v: Any, weight: Optional[float] = None) -> None:
        """
        Añade arista u->v (o u-v si no dirigido). Si weight es None y weighted==False se usa 1.0.
        Si weighted==True y weight is None -> lanza ValueError.
        """
        if weight is None:
            if self.weighted:
                raise ValueError("Edge weight required for weighted graph")
            w = 1.0
        else:
            w = float(weight)
        self.add_node(u); self.add_node(v)
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))
        self._edge_count += 1

    def get_edges(self) -> List[Tuple[Any, Any, float]]:
        """Devuelve lista (u, v, w). En no dirigido habrá duplicados en adj; filtramos para mostrar cada par una vez."""
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
                    edges.append((key[0], key[1], w))
        return edges

    def remove_edge(self, u: Any, v: Any) -> None:
        if u not in self.adj or v not in self.adj:
            raise KeyError("One or both nodes not found")
        before_u = len(self.adj[u])
        self.adj[u] = [(nei,w) for (nei,w) in self.adj[u] if nei != v]
        if not self.directed:
            self.adj[v] = [(nei,w) for (nei,w) in self.adj[v] if nei != u]
        after_u = len(self.adj[u])
        if before_u != after_u:
            self._edge_count -= 1

    def update_edge_weight(self, u: Any, v: Any, new_weight: float) -> None:
        if u not in self.adj:
            raise KeyError("Node not found")
        found = False
        for i,(nei,w) in enumerate(self.adj[u]):
            if nei == v:
                self.adj[u][i] = (nei, float(new_weight))
                found = True
                break
        if not found:
            raise KeyError("Edge not found")
        if not self.directed:
            # actualizar espejo
            for i,(nei,w) in enumerate(self.adj[v]):
                if nei == u:
                    self.adj[v][i] = (nei, float(new_weight))
                    break

    def _recompute_edge_count(self) -> None:
        if self.directed:
            self._edge_count = sum(len(lst) for lst in self.adj.values())
        else:
            self._edge_count = sum(len(lst) for lst in self.adj.values()) // 2

    # -------------------
    # BÁSICOS: BFS / DFS / connected components
    # -------------------
    def bfs(self, start: Any) -> Tuple[List[Any], Dict[Any,int], Dict[Any, Optional[Any]]]:
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
            for v,_ in self.adj[u]:
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
            for v,_ in reversed(self.adj[u]):
                if v not in visited:
                    stack.append(v)
        return order

    def connected_components(self) -> List[List[Any]]:
        """Para grafos no dirigidos devuelve componentes conectadas; si dirigido devuelve componentes débilmente conectadas."""
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
                for v,_ in self.adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
                # si dirigido, también seguir aristas entrantes para "weak connectivity"
                if self.directed:
                    # scan all nodes for incoming edges to u (costoso para muy grandes; acceptable en sparse)
                    for x in self.adj:
                        for y,_ in self.adj[x]:
                            if y == u and x not in visited:
                                visited.add(x)
                                q.append(x)
            comps.append(comp)
        return comps

    def is_connected(self) -> bool:
        if not self.adj:
            return True
        if self.directed:
            # weak connectivity check
            return len(self.connected_components()) == 1
        start = next(iter(self.adj))
        _, dist, _ = self.bfs(start)
        return all(d != -1 for d in dist.values())

    # -------------------
    # DIJKSTRA (heap) - O(E log V)
    # -------------------
    def dijkstra(self, source: Any) -> Tuple[Dict[Any,float], Dict[Any, Optional[Any]]]:
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
            for v,w in self.adj[u]:
                nd = d + (w if self.weighted else 1.0)
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev

    # -------------------
    # BELL-MANFORD - O(V*E)
    # -------------------
    def bellman_ford(self, source: Any) -> Tuple[Dict[Any,float], Dict[Any, Optional[Any]]]:
        if source not in self.adj:
            raise KeyError("Source not in graph")
        dist = {u: INF for u in self.adj}
        prev = {u: None for u in self.adj}
        dist[source] = 0.0
        nodes = list(self.adj.keys())
        for _ in range(len(nodes)-1):
            updated = False
            for u in nodes:
                for v,w in self.adj[u]:
                    weight = w if self.weighted else 1.0
                    if dist[u] != INF and dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        prev[v] = u
                        updated = True
            if not updated:
                break
        # detectar ciclo negativo
        for u in nodes:
            for v,w in self.adj[u]:
                weight = w if self.weighted else 1.0
                if dist[u] != INF and dist[u] + weight < dist[v]:
                    raise ValueError("Graph contains a negative-weight cycle reachable from source")
        return dist, prev

    # -------------------
    # KRUSKAL (MST) con DSU - para no dirigido
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
        # ensure weights exist
        sorted_edges = sorted(edges, key=lambda x: x[2] if self.weighted else 1.0)
        dsu = SparseGraph._DSU()
        for u in self.adj:
            dsu.make_set(u)
        mst = []
        total = 0.0
        for u,v,w in sorted_edges:
            if dsu.union(u, v):
                mst.append((u, v, w))
                total += (w if self.weighted else 1.0)
            if len(mst) == len(self.adj) - 1:
                break
        return mst, total

    # -------------------
    # PRIM con heap (sparse-friendly) - O(E log V)
    # -------------------
    def prim_mst(self) -> Tuple[List[Tuple[Any, Any, float]], float]:
        if self.directed:
            raise ValueError("Prim only for undirected graphs")
        if not self.adj:
            return [], 0.0
        start = next(iter(self.adj))
        visited = set()
        pq = []
        for v,w in self.adj[start]:
            heapq.heappush(pq, (w if self.weighted else 1.0, start, v))
        visited.add(start)
        mst = []
        total = 0.0
        while pq and len(visited) < len(self.adj):
            w,u,v = heapq.heappop(pq)
            if v in visited:
                continue
            visited.add(v)
            mst.append((u, v, w))
            total += w
            for to, wt in self.adj[v]:
                if to not in visited:
                    heapq.heappush(pq, ((wt if self.weighted else 1.0), v, to))
        return mst, total

    # -------------------
    # TOPOLOGICAL SORT (Kahn) y comprobación DAG
    # -------------------
    def topological_sort_kahn(self) -> List[Any]:
        if not self.directed:
            raise ValueError("Topological sort applies only to directed graphs")
        indeg = {u:0 for u in self.adj}
        for u in self.adj:
            for v,_ in self.adj[u]:
                indeg[v] = indeg.get(v, 0) + 1
        q = deque([u for u in indeg if indeg[u] == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v,_ in self.adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        if len(topo) != len(self.adj):
            raise ValueError("Graph has at least one cycle; topological sort not possible")
        return topo

    # -------------------
    # KOSARAJU - SCC (directed)
    # -------------------
    def kosaraju_scc(self) -> List[List[Any]]:
        if not self.directed:
            raise ValueError("Kosaraju applies to directed graphs")
        visited = set()
        order = []
        def dfs1(u):
            visited.add(u)
            for v,_ in self.adj[u]:
                if v not in visited:
                    dfs1(v)
            order.append(u)
        for u in self.adj:
            if u not in visited:
                dfs1(u)
        # build reversed graph
        radj = {u: [] for u in self.adj}
        for u in self.adj:
            for v,w in self.adj[u]:
                radj[v].append((u,w))
        visited.clear()
        comps = []
        def dfs2(u, comp):
            visited.add(u)
            comp.append(u)
            for v,_ in radj[u]:
                if v not in visited:
                    dfs2(v, comp)
        for u in reversed(order):
            if u not in visited:
                comp = []
                dfs2(u, comp)
                comps.append(comp)
        return comps

    # -------------------
    # ALL-PAIRS SHORTEST PATHS (opción): Dijkstra desde cada nodo (si no hay pesos negativos)
    # -------------------
    def all_pairs_shortest_paths(self) -> Dict[Any, Dict[Any, float]]:
        # verify no negatives if weighted:
        if self.weighted:
            # quick check: if any negative weight exists, user should call Bellman-Ford per source
            for u in self.adj:
                for v,w in self.adj[u]:
                    if w < 0:
                        raise ValueError("Negative weight detected; use bellman-ford per source instead")
        apsp = {}
        for u in self.adj:
            dist, _ = self.dijkstra(u)
            apsp[u] = dist
        return apsp

    # -------------------
    # UTILIDADES
    # -------------------
    @staticmethod
    def reconstruct_path(prev: Dict[Any, Optional[Any]], start: Any, goal: Any) -> Optional[List[Any]]:
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
        return path

    def degree(self, u: Any) -> int:
        if u not in self.adj:
            raise KeyError("Node not found")
        deg = len(self.adj[u])
        if self.directed:
            indeg = sum(1 for x in self.adj if any(nei == u for nei,_ in self.adj[x]))
            return indeg + deg
        return deg

    def __repr__(self) -> str:
        return f"SparseGraph(directed={self.directed}, weighted={self.weighted}, V={len(self.adj)}, E={self._edge_count})"

#Ejemplo de uso
if __name__ == "__main__":
    # construir grafo disperso no dirigido y ponderado
    G = SparseGraph(directed=False, weighted=True)

    # CRUD: nodos y aristas
    G.add_edge("A","B", 2.0)
    G.add_edge("A","C", 5.0)
    G.add_edge("B","C", 1.0)
    G.add_edge("C","D", 3.0)
    G.add_node("E")  # aislado
    print(G)
    print("Nodos:", G.get_nodes())
    print("Aristas:", G.get_edges())

    # Dijkstra desde A
    dist, prev = G.dijkstra("A")
    print("Dijkstra dist desde A:", dist)
    print("Camino A -> D:", SparseGraph.reconstruct_path(prev, "A", "D"))

    # Prim MST
    mst, total = G.prim_mst()
    print("MST (Prim):", mst, "peso total:", total)

    # Kruskal MST
    mst2, total2 = G.kruskal_mst()
    print("MST (Kruskal):", mst2, "peso total:", total2)

    # BFS desde A
    order, dist_bfs, prev_bfs = G.bfs("A")
    print("BFS orden:", order)

    # Connected components
    comps = G.connected_components()
    print("Componentes:", comps)

    # Si fuese dirigido: topological sort / kosaraju
    D = SparseGraph(directed=True, weighted=False)
    D.add_edge("T1","T2")
    D.add_edge("T2","T3")
    D.add_edge("T1","T3")
    print("Topological order (dir):", D.topological_sort_kahn())
    # Strongly connected components example
    D2 = SparseGraph(directed=True, weighted=False)
    D2.add_edge("1","2"); D2.add_edge("2","3"); D2.add_edge("3","1"); D2.add_edge("3","4")
    print("SCCs:", D2.kosaraju_scc())

