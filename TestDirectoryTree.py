from Element import Element
from directorytree import DirectoryTree

###CAMBAIRE MAPBASE

print('*** INIZIO ***')
print()
e=Element(5)
d=DirectoryTree()
d._add_root(e)
print('Radice',d.root().element().get())
print('Parent --- testare ancora',d.parent(d.root()))
print('Lunghezza',d.__len__())
### ERRORE CORRETTO IN num_children: LEN AL POSTO DI np. AGGIUNTA DI ._node._children
print('Numero figli', d.num_children(d.root()))
e1=Element(4)
print('Replace (stampa il vecchio valore)', d._replace(d.root(),e1).get())
print('Radice nuova',d.root().element().get())
e2=Element(3)
d._add_child(d.root(),e2)
print('Numero figli', d.num_children(d.root()))
generator=d.children(d.root())
print('Figli', next(generator).element().get())
#print('Figli', next(generator).element().get())

print('*** TEST 2 FIGLI ***')
e3=Element(2)
d._add_child(d.root(),e3)
print('Numero figli', d.num_children(d.root()))


generator2=d.children(d.root())
print('Figli', next(generator2).element().get())
print('Figli', next(generator2).element().get())
###TODO:CONTROLLARE LA VALIDATE DOVE METTERLA

print('*** TEST 5 FIGLI ***')
e4=Element(0)
d._add_child(d.root(),e4)
print('Numero figli', d.num_children(d.root()))
e5=Element(10)
d._add_child(d.root(),e5)
print('Numero figli', d.num_children(d.root()))
e6=Element(1)
d._add_child(d.root(),e6)
print('Numero figli', d.num_children(d.root()))

generator3=d.children(d.root())
print('Figli', next(generator3).element().get())
print('Figli', next(generator3).element().get())
print('Figli', next(generator3).element().get())
print('Figli', next(generator3).element().get())
print('Figli', next(generator3).element().get())

print()
print('*** TEST index_children ***')
print('Indice 0', d.index_children(d.root(),0).element().get())
print('Indice 1', d.index_children(d.root(),1).element().get())
print('Indice 2', d.index_children(d.root(),2).element().get())
print('Indice 3', d.index_children(d.root(),3).element().get())
print('Indice 4', d.index_children(d.root(),4).element().get())
#print('Indice 5', d.index_children(d.root(),5).element().get())

print('*** TEST PARENT ***')
position=d.index_children(d.root(),1)
print('Padre',d.parent(position).element().get())
print()
print('*** FINE ***')