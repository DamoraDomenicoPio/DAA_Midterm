# from directorytreemap import DirectoryTreeMap

# print('*** INIZIO ***')
# print()

# d=DirectoryTreeMap()
# print('*** TEST SETITEM ***')
# d['www.unisa.it/']=3
# d['www.unisa.it/diem/']=4
# d['www.unisa.it/dies/']=5
# d['www.unisa.it/diem/a/']=6
# d['www.unisa.it/diet/']=7

# print('*** TEST GETITEM ***')
# print('www.unisa.it/', d['www.unisa.it/'])
# print('www.unisa.it/diem/', d['www.unisa.it/diem/'])
# print('www.unisa.it/dies/', d['www.unisa.it/dies/'])
# print('www.unisa.it/diem/a/', d['www.unisa.it/diem/a/'])
# print('www.unisa.it/diet/', d['www.unisa.it/diet/'])

# print('Root', d.root().element()._key)
# generator=d.children(d.root())
# a=next(generator).element()._key
# print('Figlio', a)
# print('Figlio', next(generator).element()._key)
# print('Figlio', next(d.children(d.find_position(a))).element()._key)

# print()
# print('*** FINE ***')
