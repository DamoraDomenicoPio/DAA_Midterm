from Element import Element
from directorytree import DirectoryTree

###CAMBAIRE MAPBASE

print('*** INIZIO ***')
print()
e=Element(5)
d=DirectoryTree()
d._add_root(e)
print('Radice',d.root().element().get())
print('Parent',d.parent(d.root()))
print('Lunghezza',d.__len__())
### ERRORE CORRETTO IN num_children: LEN AL POSTO DI np. AGGIUNTA DI ._node._children
print('Numero figli', d.num_children(d.root()))
e1=Element(4)
print('Replace (stampa il vecchio valore)', d._replace(d.root(),e1).get())
print('Radice nuova',d.root().element().get())
e2=Element(3)
d._add_child(d.root(),e2)
print('Numero figli', d.num_children(d.root()))
print('Figli', d.children(d.root()))

###CONTROLLARE LA VALIDATE DOVE METTERLA

print()
print('*** FINE ***')