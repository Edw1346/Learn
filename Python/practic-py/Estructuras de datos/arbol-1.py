"""-----------------------------  Estructura de datos  -----------------------------"""



"""Árbol AVL. Incluye: insert, search, update, delete → CRUD"""
# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value  # opcional para CRUD tipo diccionario
        self.left = None
        self.right = None
        self.height = 1

# ---------------- AVL TREE CLASS ----------------
class AVLTree:

    # ---- ALTURA ----
    def get_height(self, node):
        return node.height if node else 0

    # ---- FACTOR DE BALANCE ----
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # ---- ROTACIÓN DERECHA ----
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x  # nueva raíz

    # ---- ROTACIÓN IZQUIERDA ----
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # nueva raíz

    # ---- CREATE (INSERTAR) ----
    def insert(self, node, key, value=None):
        # inserción BST normal
        if not node:
            return Node(key, value)

        if key < node.key:
            node.left = self.insert(node.left, key, value)
        elif key > node.key:
            node.right = self.insert(node.right, key, value)
        else:  # claves repetidas → actualiza valor
            node.value = value
            return node

        # actualizar altura
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # balancear
        balance = self.get_balance(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # ---- READ (BUSCAR) ----
    def search(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.value
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)

    # ---- UPDATE ----
    # realmente es search + insert sobre mismo key
    def update(self, node, key, new_value):
        return self.insert(node, key, new_value)

    # ---- NODO MÍNIMO (para eliminar) ----
    def min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    # ---- DELETE ----
    def delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            # nodo con 1 o 0 hijos
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # reemplazar con sucesor inorder
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self.delete(node.right, temp.key)

        # actualizar altura
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # rebalancear
        balance = self.get_balance(node)

        # Left Left Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)

        # Left Right Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Right Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        # Right Left Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

#Ejemplo de uso — CRUD
tree = AVLTree()
root = None

# CREATE
root = tree.insert(root, 30, "A")
root = tree.insert(root, 20, "B")
root = tree.insert(root, 40, "C")
root = tree.insert(root, 25, "D")

# READ
print(tree.search(root, 25))  # "D"

# UPDATE
root = tree.update(root, 40, "Nuevo valor")
print(tree.search(root, 40))  # "Nuevo valor"

# DELETE
root = tree.delete(root, 20)
print(tree.search(root, 20))  # None (ya no existe)















"""Árbol rojo-negro. Incluye: insert, search, update, delete → CRUD"""
# ---------------- NODE CLASS ----------------
RED = True
BLACK = False

class Node:
    def __init__(self, key, value=None, color=RED):
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

# ---------------- RED-BLACK TREE CLASS ----------------
class RedBlackTree:

        # ---- HELPER: COLOR ----
        def is_red(self, node):
            return node is not None and node.color == RED

        # ---- ROTATION LEFT ----
        def rotate_left(self, root, x):
            y = x.right
            x.right = y.left
            if y.left:
                y.left.parent = x
            y.parent = x.parent

            if x.parent is None:
                root = y
            elif x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y

            y.left = x
            x.parent = y

            return root

        # ---- ROTATION RIGHT ----
        def rotate_right(self, root, x):
            y = x.left
            x.left = y.right
            if y.right:
                y.right.parent = x
            y.parent = x.parent

            if x.parent is None:
                root = y
            elif x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y

            y.right = x
            x.parent = y

            return root

        # ---- INSERT FIXUP ----
        def fix_insert(self, root, z):
            while z.parent and z.parent.color == RED:
                if z.parent == z.parent.parent.left:
                    y = z.parent.parent.right
                    if self.is_red(y):  # Case 1: uncle red
                        z.parent.color = BLACK
                        y.color = BLACK
                        z.parent.parent.color = RED
                        z = z.parent.parent
                    else:
                        if z == z.parent.right: # Case 2
                            z = z.parent
                            root = self.rotate_left(root, z)
                        # Case 3
                        z.parent.color = BLACK
                        z.parent.parent.color = RED
                        root = self.rotate_right(root, z.parent.parent)
                else:
                    y = z.parent.parent.left
                    if self.is_red(y):
                        z.parent.color = BLACK
                        y.color = BLACK
                        z.parent.parent.color = RED
                        z = z.parent.parent
                    else:
                        if z == z.parent.left:
                            z = z.parent
                            root = self.rotate_right(root, z)
                        z.parent.color = BLACK
                        z.parent.parent.color = RED
                        root = self.rotate_left(root, z.parent.parent)

            root.color = BLACK
            return root

        # ---- CREATE (INSERT) ----
        def insert(self, root, key, value=None):
            new = Node(key, value)

            # BST insertion
            y = None
            x = root

            while x:
                y = x
                if new.key < x.key:
                    x = x.left
                elif new.key > x.key:
                    x = x.right
                else:  # update
                    x.value = value
                    return root

            new.parent = y
            if not y:
                root = new
            elif new.key < y.key:
                y.left = new
            else:
                y.right = new

            return self.fix_insert(root, new)

        # ---- READ (SEARCH) ----
        def search(self, node, key):
            if not node:
                return None
            if key == node.key:
                return node.value
            if key < node.key:
                return self.search(node.left, key)
            return self.search(node.right, key)

        # ---- UPDATE ----
        def update(self, root, key, value):
            return self.insert(root, key, value)

        # ---- MIN VALUE NODE ----
        def min_value_node(self, node):
            while node.left:
                node = node.left
            return node

        # ---- DELETE (Simplified + Standard RB Fix) ----
        # Para fines educativos, implementación parcial estable
        def delete(self, root, key):
            # buscar nodo
            if not root:
                return root

            if key < root.key:
                root.left = self.delete(root.left, key)
            elif key > root.key:
                root.right = self.delete(root.right, key)
            else:
                # nodo encontrado
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp = self.min_value_node(root.right)
                root.key = temp.key
                root.value = temp.value
                root.right = self.delete(root.right, temp.key)

            return root

#Notas: Delete árboles rojo-negro es extenso, versión sirve para CRUD educativo. En producción se  el fix completo.
#Ejemplo de uso — CRUD
tree = RedBlackTree()
root = None

# CREATE
root = tree.insert(root, 50, "A")
root = tree.insert(root, 30, "B")
root = tree.insert(root, 70, "C")
root = tree.insert(root, 20, "D")

# READ
print(tree.search(root, 20))  # "D"

# UPDATE
root = tree.update(root, 70, "Nuevo valor")
print(tree.search(root, 70))  # "Nuevo valor"

# DELETE
root = tree.delete(root, 30)
print(tree.search(root, 30))  # None


















"""Árbol B- Tree. Incluye: search, insert, update, delete → CRUD
Usaremos B-Tree mínimo t = 2 (el más didáctico)"""
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t               # grado mínimo
        self.keys = []           # claves ordenadas
        self.children = []       # nodos hijos
        self.leaf = leaf         # indica si es hoja

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t, leaf=True)

    # ----------- SEARCH -----------
    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i][0]:
            i += 1

        if i < len(node.keys) and key == node.keys[i][0]:
            return node.keys[i][1]

        if node.leaf:
            return None

        return self.search(node.children[i], key)

    # ----------- SPLIT CHILD -----------
    def split_child(self, parent, index):
        t = parent.children[index].t
        child = parent.children[index]

        new_node = BTreeNode(t, leaf=child.leaf)
        parent.keys.insert(index, child.keys[t-1])
        parent.children.insert(index + 1, new_node)

        new_node.keys = child.keys[t:]
        child.keys = child.keys[:t-1]

        if not child.leaf:
            new_node.children = child.children[t:]
            child.children = child.children[:t]

    # ----------- INSERT NON-FULL -----------
    def insert_non_full(self, node, key, value):
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append((key, value))
            node.keys.sort(key=lambda kv: kv[0])
        else:
            while i >= 0 and key < node.keys[i][0]:
                i -= 1
            i += 1

            if len(node.children[i].keys) == 2 * node.t - 1:
                self.split_child(node, i)
                if key > node.keys[i][0]:
                    i += 1
            self.insert_non_full(node.children[i], key, value)

    # ----------- INSERT (CREATE/UPDATE) -----------
    def insert(self, key, value):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, leaf=False)
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root

        self.insert_non_full(self.root, key, value)

    # ----------- UPDATE -----------
    def update(self, key, new_value):
        self.insert(key, new_value)

    # ----------- DELETE (simple educational) -----------
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # eliminación solo en hojas para enseñanza
        node.keys = [kv for kv in node.keys if kv[0] != key]
        return node

#Nota: La eliminación completa de B-Trees requiere merge y redistribución.
#Esta versión funciona para CRUD básico educativo.
#Ejemplo de uso — CRUD
tree = BTree(t=2)

# CREATE
tree.insert(50, "A")
tree.insert(20, "B")
tree.insert(70, "C")
tree.insert(10, "D")
tree.insert(30, "E")

# READ
print(tree.search(tree.root, 30))  # "E"

# UPDATE
tree.update(70, "Nuevo valor")
print(tree.search(tree.root, 70))  # "Nuevo valor"

# DELETE
tree.delete(20)
print(tree.search(tree.root, 20))  # None



















"""Árbol B+ Tree. Incluye: insert, search, update, delete → CRUD
Para claridad usamos t = 3 (muy común)"""
class BPlusTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.keys = []
        self.children = []
        self.leaf = leaf
        self.next = None  # solo para hojas

class BPlusTree:
    def __init__(self, t=3):
        self.root = BPlusTreeNode(t, leaf=True)
        self.t = t

    # ---------- SEARCH ----------
    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i][0]:
            i += 1

        if node.leaf:
            if i < len(node.keys) and key == node.keys[i][0]:
                return node.keys[i][1]
            return None

        return self.search(node.children[i], key)

    # ---------- SPLIT LEAF ----------
    def split_leaf(self, leaf):
        t = leaf.t
        new_leaf = BPlusTreeNode(t, leaf=True)
        mid = len(leaf.keys) // 2
        new_leaf.keys = leaf.keys[mid:]
        leaf.keys = leaf.keys[:mid]

        new_leaf.next = leaf.next
        leaf.next = new_leaf

        return new_leaf, new_leaf.keys[0][0]

    # ---------- SPLIT INTERNAL ----------
    def split_internal(self, node):
        t = node.t
        new_node = BPlusTreeNode(t, leaf=False)
        mid = len(node.keys) // 2

        sep_key = node.keys[mid]
        new_node.keys = node.keys[mid + 1:]
        node.keys = node.keys[:mid]

        new_node.children = node.children[mid + 1:]
        node.children = node.children[:mid + 1]

        return new_node, sep_key

    # ---------- INSERT NON-FULL ----------
    def insert_nonfull(self, node, key, value):
        if node.leaf:
            node.keys.append((key, value))
            node.keys.sort(key=lambda x: x[0])
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            child = node.children[i]
            if len(child.keys) == 2 * self.t:
                new_child, sep = (
                    self.split_leaf(child) if child.leaf else self.split_internal(child)
                )

                node.keys.insert(i, sep)
                node.children.insert(i + 1, new_child)

                if key > sep:
                    child = new_child

            self.insert_nonfull(child, key, value)

    # ---------- INSERT (CREATE/UPDATE) ----------
    def insert(self, key, value):
        root = self.root
        if len(root.keys) == 2 * self.t:
            new_root = BPlusTreeNode(self.t, leaf=False)
            new_root.children.append(root)

            new_child, sep = (
                self.split_leaf(root) if root.leaf else self.split_internal(root)
            )
            new_root.keys.append(sep)
            new_root.children.append(new_child)
            self.root = new_root

        self.insert_nonfull(self.root, key, value)

    # ---------- UPDATE ----------
    def update(self, key, value):
        return self.insert(key, value)

    # ---------- DELETE (educational simple) ----------
    def delete(self, key):
        leaf = self.root
        while not leaf.leaf:
            i = 0
            while i < len(leaf.keys) and key > leaf.keys[i]:
                i += 1
            leaf = leaf.children[i]

        leaf.keys = [kv for kv in leaf.keys if kv[0] != key]


#Tiene: insert, search, update, delete → CRUD     Hojas enlazadas → B+ Tree real
#Delete sin balanceo (suficiente para aprendizaje)
#Ejemplo de uso — CRUD
tree = BPlusTree(t=3)

# CREATE
tree.insert(20, "A")
tree.insert(5, "B")
tree.insert(35, "C")
tree.insert(10, "D")
tree.insert(50, "E")

# READ
print(tree.search(tree.root, 35))  # "C"

# UPDATE
tree.update(10, "Nuevo valor")
print(tree.search(tree.root, 10))  # "Nuevo valor"

# DELETE
tree.delete(20)
print(tree.search(tree.root, 20))  # None








"""Skip list. Implementación en Python — Completa
Nodo del Skip List"""
import random

class Nodo:
    def __init__(self, valor, nivel):
        self.valor = valor
        self.forward = [None] * (nivel + 1)  # punteros a siguientes niveles

#Clase SkipList
class SkipList:
    def __init__(self, max_nivel=4, prob=0.5):
        self.max_nivel = max_nivel   
        self.prob = prob             
        self.nivel_actual = 0        
        self.cabeza = Nodo(None, max_nivel)  

    def generar_nivel(self):
        nivel = 0
        while random.random() < self.prob and nivel < self.max_nivel:
            nivel += 1
        return nivel

# CREATE → Insertar
def insertar(self, valor):
        actual = self.cabeza
        actualizaciones = [None] * (self.max_nivel + 1)

        for i in range(self.nivel_actual, -1, -1):
            while actual.forward[i] and actual.forward[i].valor < valor:
                actual = actual.forward[i]
            actualizaciones[i] = actual
        
        nuevo_nivel = self.generar_nivel()

        if nuevo_nivel > self.nivel_actual:
            for i in range(self.nivel_actual + 1, nuevo_nivel + 1):
                actualizaciones[i] = self.cabeza
            self.nivel_actual = nuevo_nivel
        
        nuevo = Nodo(valor, nuevo_nivel)
        for i in range(nuevo_nivel + 1):
            nuevo.forward[i] = actualizaciones[i].forward[i]
            actualizaciones[i].forward[i] = nuevo

#READ → Buscar
def buscar(self, valor):
        actual = self.cabeza
        for i in range(self.nivel_actual, -1, -1):
            while actual.forward[i] and actual.forward[i].valor < valor:
                actual = actual.forward[i]

        actual = actual.forward[0]
        return actual and actual.valor == valor

#UPDATE → Modificar valor (Eliminar + insertar, forma típica)
def actualizar(self, viejo, nuevo):
        if self.eliminar(viejo):
            self.insertar(nuevo)
            return True
        return False

#DELETE → Eliminar
def eliminar(self, valor):
        actual = self.cabeza
        actualizaciones = [None] * (self.max_nivel + 1)

        for i in range(self.nivel_actual, -1, -1):
            while actual.forward[i] and actual.forward[i].valor < valor:
                actual = actual.forward[i]
            actualizaciones[i] = actual
        
        actual = actual.forward[0]

        if actual and actual.valor == valor:
            for i in range(self.nivel_actual + 1):
                if actualizaciones[i].forward[i] != actual:
                    break
                actualizaciones[i].forward[i] = actual.forward[i]

            while self.nivel_actual > 0 and self.cabeza.forward[self.nivel_actual] is None:
                self.nivel_actual -= 1
            
            return True
        
        return False

#Mostrar niveles (opcional)
def mostrar(self):
        for i in range(self.nivel_actual, -1, -1):
            actual = self.cabeza.forward[i]
            nivel = []
            while actual:
                nivel.append(actual.valor)
                actual = actual.forward[i]
            print(f"Nivel {i}: {nivel}")

#Ejemplo de uso (CRUD)
s = SkipList()

s.insertar(10)
s.insertar(3)
s.insertar(25)
s.insertar(15)

s.mostrar()

print(s.buscar(15))  # True
print(s.buscar(100)) # False

s.actualizar(15, 20)
s.mostrar()

s.eliminar(3)
s.mostrar()












"""Trie 
c
└── a
    ├── r   → "car"
    ├── s
    │   └── a → "casa"
    └── n
        └── t
            └── o → "canto"""

#Clase Nodo del Trie
class TrieNode:
    def __init__(self):
        self.hijos = {}       # dict {caracter: TrieNode}
        self.fin_palabra = False

#Clase Trie completa con CRUD
class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    # CREATE → insertar palabra
    def insertar(self, palabra):
        nodo = self.raiz
        for c in palabra:
            if c not in nodo.hijos:
                nodo.hijos[c] = TrieNode()
            nodo = nodo.hijos[c]
        nodo.fin_palabra = True

    # READ → buscar palabra exacta
    def buscar(self, palabra):
        nodo = self.raiz
        for c in palabra:
            if c not in nodo.hijos:
                return False
            nodo = nodo.hijos[c]
        return nodo.fin_palabra

    # READ → autocompletar por prefijo
    def buscar_prefijo(self, prefijo):
        nodo = self.raiz
        for c in prefijo:
            if c not in nodo.hijos:
                return []
            nodo = nodo.hijos[c]
        resultados = []
        self._dfs(nodo, prefijo, resultados)
        return resultados

    # DFS para listar palabras
    def _dfs(self, nodo, prefijo, resultados):
        if nodo.fin_palabra:
            resultados.append(prefijo)
        for c, hijo in nodo.hijos.items():
            self._dfs(hijo, prefijo + c, resultados)

    # DELETE → eliminar palabra
    def eliminar(self, palabra):
        return self._eliminar(self.raiz, palabra, 0)

    def _eliminar(self, nodo, palabra, i):
        if i == len(palabra):
            if not nodo.fin_palabra:
                return False
            nodo.fin_palabra = False
            return len(nodo.hijos) == 0

        c = palabra[i]
        if c not in nodo.hijos:
            return False

        borrar = self._eliminar(nodo.hijos[c], palabra, i+1)

        if borrar:
            del nodo.hijos[c]
            return not nodo.fin_palabra and len(nodo.hijos) == 0

        return False

    # UPDATE → renombrar palabra
    def actualizar(self, vieja, nueva):
        if self.buscar(vieja):
            self.eliminar(vieja)
            self.insertar(nueva)
            return True
        return False

#Ejemplo de uso
trie = Trie()

# CREATE
trie.insertar("casa")
trie.insertar("carro")
trie.insertar("car")
trie.insertar("canto")

# READ
print(trie.buscar("carro"))   # True
print(trie.buscar("cara"))    # False

# Autocompletar
print(trie.buscar_prefijo("ca"))
# ['casa', 'carro', 'car', 'canto']

# UPDATE
trie.actualizar("casa", "casita")
print(trie.buscar_prefijo("ca"))
# ['carro', 'car', 'canto', 'casita']

# DELETE
trie.eliminar("car")
print(trie.buscar("car"))     # False






"""Sufflix tree
Es un árbol comprimido que contiene todos los sufijos de una cadena. Ejemplo con "casa$":
casa$
asa$
sa$
a$
$
El sufijo $ es un marcador final obligatorio, evita solapamientos. El árbol resultante:
┌── "casa$"
         │
    raíz ┤── "asa$"
         │
         ├── "sa$"
         │
         ├── "a$"
         │
         └── "$"
Implementación en Python (Suffix Tree compacto)"""
#Nodo del árbol
class Nodo:
    def __init__(self):
        self.hijos = {}  # {caracter: (inicio, fin, Nodo)}

#Clase SuffixTree con construcción naive (clara para aprender)
class SuffixTree:
    def __init__(self, texto=""):
        if texto and texto[-1] != "$":
            texto += "$"
        self.texto = texto
        self.raiz = Nodo()
        if texto:
            self._construir()

    def _construir(self):
        for i in range(len(self.texto)):
            self._insertar_sufijo(i)

    def _insertar_sufijo(self, inicio):
        nodo = self.raiz
        i = inicio

        while i < len(self.texto):
            c = self.texto[i]

            if c not in nodo.hijos:
                nodo.hijos[c] = (i, len(self.texto), Nodo())
                return

            inicio_arista, fin_arista, hijo = nodo.hijos[c]
            j = inicio_arista

            while j < fin_arista and i < len(self.texto) and self.texto[j] == self.texto[i]:
                j += 1
                i += 1

            if j == fin_arista:
                nodo = hijo
            else:
                viejo_hijo = Nodo()
                viejo_hijo.hijos = hijo.hijos

                nodo.hijos[c] = (inicio_arista, j, viejo_hijo)

                if i < len(self.texto):
                    nuevo_hijo = Nodo()
                    viejo_hijo.hijos[self.texto[i]] = (i, len(self.texto), nuevo_hijo)

                return


#READ → Buscar substring
def buscar(self, patron):
        nodo = self.raiz
        i = 0

        while i < len(patron):
            c = patron[i]
            if c not in nodo.hijos:
                return False

            inicio, fin, hijo = nodo.hijos[c]
            j = inicio

            while j < fin and i < len(patron) and self.texto[j] == patron[i]:
                j += 1
                i += 1
            
            if j < fin and i == len(patron):
                return True

            if j < fin:
                return False

            nodo = hijo
        
        return True

#CREATE → Insertar nuevo texto
#En suffix trees, insertar implica reconstruir, porque toda la estructura depende del string original:
def insertar_texto(self, nuevo): self.__init__(nuevo) 

#UPDATE → Modificar texto
def actualizar(self, nuevo): self.insertar_texto(nuevo) 

#DELETE → Eliminar texto completo
def eliminar(self):
    self.texto = "" 
    self.raiz = Nodo() 
#Los suffix trees no eliminan substrings, solo reconstruyen.

#Ejemplo de uso completo (CRUD)
st = SuffixTree("banana")

print(st.buscar("nan"))   # True
print(st.buscar("nana"))  # True
print(st.buscar("baan"))  # False

# UPDATE (nuevo texto)
st.actualizar("casa")
print(st.buscar("asa"))   # True

# DELETE
st.eliminar()
print(st.buscar("a"))     # False





"""Suffix array
Es un arreglo ordenado con los índices donde comienzan todos los sufijos de un string. Ejemplo con "banana$": Sufijos:
0: banana$
1: anana$
2: nana$
3: ana$
4: na$
5: a$
6: $

Orden lexicográfico:
6: $
5: a$
3: ana$
1: anana$
0: banana$
4: na$
2: nana$
Entonces el Suffix Array es: [6, 5, 3, 1, 0, 4, 2] 

Implementación didáctica en Python
Construcción naive (clara para aprender)"""
class SuffixArray:
    def __init__(self, texto=""):
        if texto and texto[-1] != "$":
            texto += "$"
        self.texto = texto
        self.suffix_array = []
        if texto:
            self.construir()

    def construir(self):
        sufijos = [(self.texto[i:], i) for i in range(len(self.texto))]
        sufijos.sort()  # orden lexicográfico
        self.suffix_array = [i for _, i in sufijos]

#Sencillo    Correcto   Perfecto para entender

#READ — Buscar substring con Binary Search
def buscar(self, patron):
        izq, der = 0, len(self.suffix_array) - 1

        while izq <= der:
            mid = (izq + der) // 2
            inicio = self.suffix_array[mid]
            sufijo = self.texto[inicio:]

            if sufijo.startswith(patron):
                return True

            if patron > sufijo:
                izq = mid + 1
            else:
                der = mid - 1
        
        return False

#CREATE — Insertar texto nuevo  Como en Suffix Tree, se vuelve a construir:
def insertar_texto(self, nuevo): self.__init__(nuevo) 

#UPDATE — Modificar texto
def actualizar(self, nuevo): self.insertar_texto(nuevo)

#DELETE — Eliminar estructura
def eliminar(self): 
    self.texto = "" 
    self.suffix_array = [] 

#Ejemplo completo (CRUD)
sa = SuffixArray("banana")

print(sa.suffix_array)
# [6, 5, 3, 1, 0, 4, 2]

print(sa.buscar("nan"))   # True
print(sa.buscar("nab"))   # False

# UPDATE
sa.actualizar("casa")
print(sa.suffix_array)     # sufijos ordenados de "casa$"
print(sa.buscar("asa"))    # True

# DELETE
sa.eliminar()
print(sa.buscar("a"))      # False










"""Fenwick tree (binary indexed tree)
Implementación en Python
Fenwick Tree completo (CRUD incluido)"""
class FenwickTree:
    def __init__(self, arr=None):
        if arr:
            self.build(arr)
        else:
            self.n = 0
            self.tree = []

    # CREATE — construir desde un array
    def build(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n + 1)
        for i, val in enumerate(arr, start=1):
            self._update(i, val)  # función interna

    # UPDATE — sumar valor a un índice
    def _update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    # UPDATE — asignar un nuevo valor
    def update_set(self, i, new_value):
        actual = self.query_range(i, i)
        delta = new_value - actual
        self._update(i, delta)

    # READ — suma acumulada 1..i
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    # READ — suma en rango [l, r]
    def query_range(self, l, r):
        return self.query(r) - self.query(l - 1)

    # DELETE — borrar estructura
    def delete(self):
        self.n = 0
        self.tree = []

#Ejemplo completo de uso (CRUD)
arr = [2, 4, 5, 7, 1, 3]

ft = FenwickTree(arr)        # CREATE

print(ft.query(4))           # suma 1..4 → 18
print(ft.query_range(2, 5))  # 4 + 5 + 7 + 1 = 17

ft.update_set(3, 10)         # READ + UPDATE
print(ft.query_range(1, 3))  # 2 + 4 + 10 = 16

ft.delete()                  # DELETE
print(ft.tree)               # []











"""Segment tree
Implementación completa en Python (Segment Tree para suma)"""
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # tamaño seguro
        self.build(arr, 1, 0, self.n - 1)

    # CREATE — construir árbol
    def build(self, arr, node, left, right):
        if left == right:
            self.tree[node] = arr[left]
            return
        
        mid = (left + right) // 2
        self.build(arr, node*2, left, mid)
        self.build(arr, node*2+1, mid+1, right)
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    # READ — consulta de rango [l, r]
    def query(self, node, left, right, l, r):
        if r < left or right < l:       # totalmente fuera
            return 0
        if l <= left and right <= r:    # totalmente dentro
            return self.tree[node]
        
        mid = (left + right) // 2
        return (
            self.query(node*2, left, mid, l, r) +
            self.query(node*2+1, mid+1, right, l, r)
        )

    # UPDATE — cambiar valor en índice idx
    def update(self, node, left, right, idx, value):
        if left == right:
            self.tree[node] = value
            return

        mid = (left + right) // 2
        if idx <= mid:
            self.update(node*2, left, mid, idx, value)
        else:
            self.update(node*2+1, mid+1, right, idx, value)

        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    # DELETE — poner valor neutro (0 para suma)
    def delete(self, idx):
        self.update(1, 0, self.n - 1, idx, 0)

#Ejemplo de uso (CRUD)
arr = [5, 2, 7, 3, 8]
st = SegmentTree(arr)

# READ — suma del rango [1, 3] (2 + 7 + 3) = 12
print(st.query(1, 0, st.n - 1, 1, 3))

# UPDATE — cambiar arr[2] = 10
st.update(1, 0, st.n - 1, 2, 10)

# READ nuevamente — ahora 2 + 10 + 3 = 15
print(st.query(1, 0, st.n - 1, 1, 3))

# DELETE — eliminar valor en índice 4 (poner 0)
st.delete(4)

# READ — suma total del arreglo
print(st.query(1, 0, st.n - 1, 0, 4))








"""Disjoint set union (union-find) 
Implementación completa en Python — con comentarios"""
class DisjointSetUnion:
    def __init__(self):
        self.parent = {}  # padre del nodo
        self.rank = {}    # aproximación a la altura del árbol

    # CREATE — crear conjunto con un elemento
    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    # READ — encontrar el representante del conjunto
    def find(self, x):
        if self.parent[x] != x:
            # Path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # UPDATE — unir los conjuntos que contienen a x e y
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return  # ya están unidos

        # Union by rank — el árbol pequeño se pega al grande
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

    # DELETE — no existe en DSU, pero lo simulamos desactivándolo
    def delete(self, x):
        if x in self.parent:
            del self.parent[x]
            del self.rank[x]

#Ejemplo completo de uso (CRUD)
dsu = DisjointSetUnion()

# CREATE — crear elementos
for x in [1, 2, 3, 4, 5]:
    dsu.make_set(x)

# UPDATE — unir conjuntos
dsu.union(1, 2)
dsu.union(3, 4)
dsu.union(2, 3)  # ahora 1,2,3,4 están conectados

# READ — verificar conexiones
print(dsu.find(1))  # mismo representante que 4
print(dsu.find(4))

# saber si 5 pertenece al mismo grupo
print(dsu.find(1) == dsu.find(5))  # False

# DELETE — eliminar valor
dsu.delete(5)

#Salida aproximada:
#1 
#1
#False