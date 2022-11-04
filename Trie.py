from TdP_collections.tree.tree import Tree
from TdP_collections.hash_table.chain_hash_map import ChainHashMap

# HashTree - Un albero con più di due figli e non ordinato. 
# I figli sono conservati i ntabelle hash per ricerche più veloci 
class Trie(Tree):

    class _Node(): 
        __slots__ = '_element', '_parent', '_children'

        def __init__(self, element, parent = None): 
            self._element = element 
            self._parent = parent 
            self._children = ChainHashMap()   # i figli del nodo sono raccolti in una hashMap

    class Position(Tree.Position): 
        def __init__(self, container, node): 
            """NB: Il costruttore non dovrebbe essere invocato dall'utente"""
            self._container = container
            self._node = node 

        def element(self): 
            return self._node.element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    # ---- TRIE ----

    # ---- Costruttore ---- 
    def __init__(self): 
        self._root = None
        self._size = 0

    # ---- Metodi dell'interfaccia Tree da implementare 
    # -------- "Public accessors" ----

    def root(self):
        """Ritorna la position della root ( o None se l'albero è vuoto)"""
        return self._make_position(self._root)

    def parent(self, p):
        """Ritorna la Position del genitore (o None se p è la radice)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    # Equivalente di left e right 
    def getChild(self, p, childKey):
        """Ritorna la position del figlio di p che ha come chiave child"""
        node = self._validate(p)
        return self._make_position(node._children[childKey])

    def num_children(self, p): 
        node = self._validate(p) # Estrae il nodo 
        return len(node._children)
        
    def children(self, p): 
        node = self._validate(p) # Estrae il nodo 
        return iter(node._children) # Restituisce un iteratore sui figli 
        #TODO serve make_position? _children dovrebbe essere una tabella di position

    def __len__(self): 
        return self._size

    # ---- Nuovi metodi ---- 

    # -------- Utility ----
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:      # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    # -------- "Non public mutators" ---- 
    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    def _add_root(self, e): 
        if self._root is not None:
            raise ValueError('La radice è già esistente')
        self._size = 1 
        self._root = self._Node(e) # Crea un nuovo nodo contenente e 
        return self._make_position(self._root)

    #Equivalente di addLeft e addRight
    #TODO è possibiile usare e come chiave k? (magari manipolando la __eq__ di e)
    def _add_child(self, p, e):  
        node = self._validate(p)
        self._size += 1
        child = self._Node(e, node) # Crea il nuovo nodo da inserire e aggiunge il reference al padre 
        node._children[e] = child
        return self._make_position(child)



    def _replace(self, p , e): 
        pass 

    def __str__(self): 
        """Stampa il contenuto dell'albero"""
        self._printSubtree(self.root(), 0)


    def _printSubtree(self, p, depth):
        print("---"*depth + str(p.element()))
        for child in self.children(p):
            self._printSubtree(child, depth+1)







    # Rispetto a linkedBinaryTree mancano solo delete e attach  

    # La ricerca viene fatta nella classe superiore perché 
    # tiene conto anche di come è fatto l'element