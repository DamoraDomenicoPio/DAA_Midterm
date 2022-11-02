from hashlib import new
from directorytree import DirectoryTree
from TdP_collections.map.map_base import MapBase

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
            return p
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
            if child!=p:
                return self._subtree_search(child,k)
        return p
        #attenzione devi lavorare sulle position devi mettere la make position 
    
    def find_position(self,k):
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            return p

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
        if k != p.key():
            raise KeyError('Key Error: ' + repr(k))
        return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        if self.is_empty():
            leaf = self._add_root(self._Item(k,v))     # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v                   # replace existing item's value
                return
            else:
                item = self._Item(k,v)
                self._add_child(p,item)
                
    def __delitem__(self,p):
        pass

