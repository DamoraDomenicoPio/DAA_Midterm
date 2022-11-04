from engine import WebSite, Element

print('*** INIZIO ***')
print()

w=WebSite('www.unisa.it/')
#
#
#
#aggiungere controllo del / 
#
#
#
#w.getSiteString()
w.insertPage('www.unisa.it/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/inde.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/indet.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')

w.insertPage('www.unisa.it/ciao/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/cosa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/cosa/casa/index.html','Antonio il pisciaiuolo')

w.insertPage('www.unisa.it/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/inde.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/indet.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')

w.insertPage('www.unisa.it/ciao/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/cosa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/cosa/casa/index.html','Antonio il pisciaiuolo')


w.insertPage('www.unisa.it/cosa/casa/cobalto/cara/minchia/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/cosa/casa/cobalto/cara/manchia/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/cosa/casa/cobalto/cara/monchia/index.html','Antonio il pisciaiuolo')



w.insertPage('www.unisa.it/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/inde.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/indet.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')

w.insertPage('www.unisa.it/ciao/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/cosa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/cosa/casa/index.html','Antonio il pisciaiuolo')

w.insertPage('www.unisa.it/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/inde.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/indet.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/index.html','Antonio il pescatore')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')

w.insertPage('www.unisa.it/ciao/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/ciao/casa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/cosa/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/cosa/casa/index.html','Antonio il pisciaiuolo')


w.insertPage('www.unisa.it/cosa/casa/cobalto/cara/minchia/index.html','Antonio il pisciaiuolo')
page=w.insertPage('www.unisa.it/cosa/casa/cobalto/cara/manchia/index.html','Antonio il pisciaiuolo')
w.insertPage('www.unisa.it/cosa/casa/cobalto/cara/monchia/index.html','Antonio il pisciaiuolo')
# print(w['www.unisa.it/index.html'])
# print(w['www.unisa.it/inde.html'])
# print(w['www.unisa.it/indet.html'])
#print(w.getHomePage())
print()
w.getSiteString()
home=w.getHomePage()
print(home._position.key(), home._position.value())

w2=WebSite('www.unina.it/')

w2.insertPage('www.unina.it/index.html','Antonio il pisciaiuolo')
w2.insertPage('www.unina.it/inde.html','Antonio il pisciaiuolo')
w2.insertPage('www.unina.it/indet.html','Antonio il pisciaiuolo')
w2.insertPage('www.unina.it/index.html','Antonio il pisciaiuolo')
w2.insertPage('www.unina.it/ciao/casa/index.html','Antonio il pisciaiuolo')
w2.insertPage('www.unina.it/ciao/casa/index.html','Antonio il pisciaiuolo')


assia=WebSite.getSiteFromPage(page)

print(assia)
print(assia.getHomePage().getUrl())

print()
print('*** FINE ***')