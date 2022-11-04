from directorytreemap import DirectoryTreeMap

class Element():
    __slots__='_position'

    def __init__(self,position):
        self._position=position

    def setKey(self, url):
        self._position._key=url

    def setValue(self, name, type, content=None):
        self._position.value()[0]=name
        self._position.value()[1]=type
        self.setContent(content)

    def setContent(self, content):
        if len(self._position.value()) <= 2:
            self._position.value().append(content)
        else:
            self._position.value()[2]=content

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
       self[host]=[host.removesuffix('/'),False]
       self._homepage=None

    def __isDir(self, elem):
        return not elem.getType()

    def __isPage(self, elem):
        return elem.getType()

    def __hasDir(self, ndir, cdir):
        if(not self.__isDir(cdir)):
            raise TypeError(cdir, 'is a page')
        p=self.children_search(cdir._position,ndir)
        e=Element(p)
        e.setKey(p.key())
        e.setValue(p.value()[0], p.value()[1])
        #TODO:vedere se mettere position al posto di getUrl
        if(e.getUrl()!=cdir.getUrl() and self.__isDir(e)):
            return e
        #TODO:vedere se mettere position al posto di getUrl
        elif(e.getUrl()==cdir.getUrl()):
            raise KeyError(ndir, 'does not exists')
        else:
            raise TypeError(ndir,'is a page')

    def __newDir(self, ndir, cdir):
        try:
            return self.__hasDir(ndir, cdir)
        except KeyError:
            name=ndir.split('/')[-2]        # -2 because is a directory
            p=self.set_child(cdir._position,ndir,[name,False,None])
            e=Element(p)
            e.setKey(ndir)
            e.setValue(name,False)
            return e

    def __hasPage(self, npag, cdir):
        if(not self.__isDir(cdir)):
            raise TypeError(cdir, 'is a page')
        p=self.children_search(cdir._position,npag)
        e=Element(p)
        e.setKey(p.key())
        e.setValue(p.value()[0], p.value()[1])
        #TODO:vedere se mettere position al posto di getUrl
        if(e.getUrl()!=cdir.getUrl() and self.__isPage(e)):
            return e
        #TODO:vedere se mettere position al posto di getUrl
        elif(e.getUrl()==cdir.getUrl()):
            raise KeyError(npag, 'does not exists')
        else:
            raise TypeError(npag,'is a directory')

    def __newPage(self, npag, cdir):
        try:
            return self.__hasPage(npag, cdir)
        except KeyError:
            name=npag.split('/')[-1]
            p=self.set_child(cdir._position,npag,[name,True,None])
            e=Element(p)
            #TODO
            e.setKey(npag)
            e.setValue(name, True)
            if name=='index.html' and self.parent(cdir._position)==None:
                self._homepage=e
            return e

    def getHomePage(self):
        if self._homepage==None:
            raise ValueError('there is not a homepage')
        return self._homepage

    def getSiteString(self):
        self._print_subtree(self.root(),0)

    def _print_subtree(self,p,level):
        print('---'*level+p.value()[0])
        for child in self.children(p):
            self._print_subtree(child,level+1)

    def insertPage(self, url, content):
        urlSplit=url.split('/')
        name=urlSplit[0]+'/'
        cdirString=url.removesuffix(urlSplit[-1])
        cdirPosition=self.find_position(cdirString)
        cdirElement=Element(cdirPosition)
        #TODO:vedi se set key e set value ci vanno
        # cdirElement.setKey(cdirPosition.key())
        # cdirElement.setValue(cdirPosition.value()[0], cdirPosition.value()[1])
        #inserimento di directory
        directoryToCreate=cdirElement.getUrl()
        s=url.removeprefix(directoryToCreate)
        start=url.removesuffix(s).count('/')-1
        n=s.count('/')
        newUrl=''
        #TODO: controllare se si possono creare più cartelle contemporaneamente
        for i in range(1,n+1):
            directoryToCreate=directoryToCreate+urlSplit[start+i]+'/'
            cdirElement=self.__newDir(directoryToCreate,cdirElement)
        #
        e=self.__newPage(url,cdirElement)
        e.setContent(content)
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
