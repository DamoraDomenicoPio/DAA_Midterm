from directorytreemap import DirectoryTreeMap

class Element():
    __slots__='_position'

    def __init__(self,position):
        self._position=position

    def getUrl(self):
        return self._position.key()

    def getContent(self):
        if self.getType():
            return self._position.value()[2]
        else:
            raise ValueError('is not a page!')

    def getType(self):
        return self._position.value()[1]

    def getName(self):
        return self._position.value()[0]


class WebSite(DirectoryTreeMap):
    __slots__='_homepage'

    def __init__(self, host):
       super().__init__()
       self[host]=[host,False]
       self._homepage=None

    def __isDir(self, elem):
        return not elem.getType()

    def __isPage(self, elem):
        return elem.getType()

    def __hasDir(self, ndir, cdir):
        if(not self.__isDir(cdir)):
            raise TypeError(cdir, 'is a page')
        p=self.children_search(cdir,ndir)
        e=Element(p)
        if(e!=cdir and self.__isDir(e)):
            return e
        elif(self.__isPage(e)):
            raise TypeError(ndir,'is a page')
        else:
            raise KeyError(ndir, 'does not exists')

    def newDir(self, ndir, cdir):
        try:
            return self.__hasDir(ndir, cdir)
        except KeyError:
            name=ndir.slice('/')[-1]
            e=Element(self.set_child(cdir,ndir,[name,False]))
            return e

    def __hasPage(self, npag, cdir):
        if(not self.__isDir(cdir)):
            raise TypeError(cdir, 'is a page')
        p=self.children_search(cdir,npag)
        e=Element(p)
        if(e!=cdir and self.__isPage(e)):
            return e
        elif(self.__isDir(e)):
            raise TypeError(npag,'is a directory')
        else:
            raise KeyError(npag, 'does not exists')

    def __newPage(self, npag, cdir):
        try:
            return self.__hasPage(npag, cdir)
        except KeyError:
            name=npag.slice('/')[-1]
            e=Element(self.set_child(cdir,npag,[name,True,None]))
            if name=='index.html':
                self._homepage=e
            return e

    def getHomePage(self):
        if self._homepage==None:
            raise ValueError('there is not a homepage')
        return self._homepage

    def getSiteString(self):
        self.print_subtree(self.root(),0)

    def _print_subtree(self,p,level):
        print('---'*level+p.value()[0])
        for child in self.children(p):
            self.print_subtree(child,level+1)

    def insertPage(self, url, content):
        name=url.slice('/')[-1]
        cdirString=url.removesuffix(name)
        cdir=self.find_position(cdirString)
        e=self.__newPage(name,cdir)
        e.value()[2]=content
        return e

    #TODO
    def getSiteFromPage(self, page):
        pass

class InvertedIndes:

    def __init__(self):
        pass

    def addWord(self, keyword):
        pass

    def addPage(self, page):
        pass

    def getList(self, keyword):
        pass

class SearchEngine:

    def __init__(self, namedir):
        pass

    def search(self, keyword, k):
        pass
