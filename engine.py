from directorytreemap import DirectoryTreeMap

class Element:
    __slots__='_page','_content','_url'

    def __init__(self, url, page=False, content=None):
        self._page=page
        self._url=url
        if(page):
            self._content=content

    def getPage(self):
        return self._page
    
    def getContent(self):
        return self._content


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
        

    def __newDir(self, ndir, cdir):
        pass

    def __hasPage(self, npag, cdir):
        pass

    def __newPage(self, npag, cdir):
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
