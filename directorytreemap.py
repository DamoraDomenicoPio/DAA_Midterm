from hashlib import new
from directorytree import DirectoryTree
from .TdP_collections.map import MapBase

class DirectoryTreeMap(DirectoryTree,MapBase):
    #---------------------------- override Position class ----------------------------
  class Position(DirectoryTree.Position):
    def key(self):
        """Return key of map's key-value pair."""
        return self.element()._key

    def value(self):
        """Return value of map's key-value pair."""
        return self.element()._value

    #------------------------------- nonpublic utilities -------------------------------
    def _dicotomic_search(self,p,k,i,f):
        m=(i+f)/2
        if(f<i):
            return None
        if(k.startswith(self.index_children(p,m).key())):
            return self.index_children(p,m)
        if(k<self.index_children(p,m)):
            return self._dicotomic_search(p,k,i,m-1)
        if(k>self.index_children(p,m)):
            return self._dicotomic_search(p,k,m+1,f)
        
    def _subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched."""
        if k == p.key():                                   # found match
            return p  
        if(k.startswith(p.key())):
            child=self._dicotomic_search(p,k,0,self.num_children(p)-1)
            if child is not None:
                return self._subtree_search(child,k)
        return None
        #attenzione devi lavorare sulle position devi mettere la make position 
    


    def find_position(self,k):
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            return p

