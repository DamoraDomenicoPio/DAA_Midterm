from directorytreemap import DirectoryTreeMap

class Element:
    __slots__='_page','_content','_url','_position'

    def __init__(self, url, page=False, content=None):
        self._page=page
        self._url=url
        if(page):
            self._content=content
    
    def _getPosition(self):
        return self._position
    
    def _setPosition(self, p):
        self._position=p

    def getPage(self):
        return self._page
    
    def getContent(self):
        return self._content

    def getUrl(self):
        return self._url


class WebSite(DirectoryTreeMap):
    __slots__='_host','_homepage','_root','_homedirectory'

    def __init__(self, host):
       self._host=host
       self._root=DirectoryTreeMap()
       self._homedirectory=Element()
       self._root._add_root(self._homedirectory)

    def __isDir(self, elem):
        return elem.getPage()==False

    def __isPage(self, elem):
        return elem.getPage()==True

    def __hasDir(self, ndir, cdir):
        if(self.__isDir(cdir)==False):
            raise('cdir is not a directory')
        nameCompleteNdir=cdir.getUrl()+ndir
        positionCurrent=cdir._getPosition()
        numChild=self._root.num_children(positionCurrent)
        positionChild=self._dicotomic_search(positionCurrent,ndir,0,numChild)
        if nameCompleteNdir==positionChild.key() and self.__isDir(positionChild.element()):
            return positionChild.element()
        elif(self.__isDir(positionChild.element())==False):
            raise('ndir in not a directory')
        else:
            raise('ndir does not exists')


    def __newDir(self, ndir, cdir):
        pass

    def __hasPage(self, npag, cdir):
        if(self.__isDir(cdir)==False):
            raise('cdir is not a directory')
        nameCompleteNpag=cdir.getUrl()+npag
        positionCurrent=cdir._getPosition()
        numChild=self._root.num_children(positionCurrent)
        positionChild=self._dicotomic_search(positionCurrent,npag,0,numChild)
        if nameCompleteNpag==positionChild.key() and self.__isPage(positionChild.element()):
            return positionChild.element()
        elif(self.__isPage(positionChild.element())):
            raise('npag in not a page')
        else:
            raise('npag does not exists')

    def __newPage(self, npag, cdir):
        # if not cdir._isDir: # Se cdir non è una directory lancia un eccezione 
        #     #lancia l'eccezione 
        #     return
        # self.
        pass



    def getHomePage(self):
        return self._homepage

    def getSiteString(self):
        pass

    def insertPage(self, url, content):
        e=Element(True,content)


    def getSiteFromPage(self, page):
        pass

def InvertedIndes:

    def __init__(self):
        pass

    def addWord(self, keyword):
        pass

    def addPage(self, page):
        pass

    def getList(self, keyword):
        pass

def SearchEngine:

    def __init__(self, namedir):
        pass

    def search(self, keyword, k):
        pass









