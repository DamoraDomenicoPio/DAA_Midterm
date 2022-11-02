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
    def _subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched."""
        if k == p.key():                                   # found match
            return p  
        if(k.startswith(p.key())):
            i=self.num_children(p)/2
            self._subtree_search(self.index_children(p,i))
            if(k<self.index_children(p,i)):
               new_i=i/2 #
               self._subtree_search(self.index_children(p,new_i)) 
            else:
                new_i=i+i/2 #
                self._subtree_search(self.index_children(p,new_i)) 
        return None
        #attenzione devi lavorare sulle position devi mettere la make position 


