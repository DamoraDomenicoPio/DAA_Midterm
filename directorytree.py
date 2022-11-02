from TdP_collections.tree.tree import Tree
from TdP_collections.map.map_base import MapBase
#import numpy as np



class DirectoryTree(Tree):

  class _Node():
    __slots__= '_element','_parent','_children'

    def __init__(self, element, parent=None):
      self._element=element
      self._parent=parent
      self._children=[]

  class Position(Tree.Position):

    def __init__(self, container, node):
      """Constructor should not be invoked by user."""
      self._container = container
      self._node = node

    def element(self):
      return self._node._element

    def __eq__(self, other):
      return type(other) is type(self) and other._node is self._node

  #___________________________________________________________________________Class DirectoryTree
  def _validate(self, p):
    """Return associated node, if position is valid."""
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    if p._node._parent is p._node:      # convention for deprecated nodes
      raise ValueError('p is no longer valid')
    return p._node

  def _make_position(self, node):
    """Return Position instance for given node (or None if no node)."""
    return self.Position(self, node) if node is not None else None

  #________________________________________________________Costruttore
  def __init__(self):
    """Create an initially empty binary alberi."""
    self._root = None
    self._size = 0

  def root(self):
    """Return the root Position of the alberi (or None if alberi is empty)."""
    return self._make_position(self._root)

  def parent(self, p):
    """Return the Position of p's parent (or None if p is root)."""
    node = self._validate(p)
    return self._make_position(node._parent)
  
  def __len__(self):
    """Return the total number of elements in the alberi."""
    return self._size

  #TODO
  def num_children(self, p):
    node=self._validate(p)
    return len(node._children)

  #DA TESTARE
  def children(self, p):
    node=self._validate(p)
    for i in range(0,self.num_children(p)):
      yield self._make_position(node._children[i])
 
  #DA TESTARE
  def index_children(self,p,i):
    node=self._validate(p)
    if(i not in range(0,self.num_children(p))):
      raise ValueError('Out of bound')
    return self._make_position(node._children[i]) 

  def _add_root(self,e):
    if self._root is not None:
      raise ValueError('Root exists')
    self._size = 1
    self._root = self._Node(e)
    return self._make_position(self._root)

  def _add_child(self,p,e):
    node=self._validate(p)
    self._size+=1
    i=0
    ###
    newchild=self._Node(e,node)
    if(len(node._children)==0):
      node._children.append(newchild)
      return self._make_position(newchild)
    ###
    numChild=self.num_children(p)
    while i < numChild and e > node._children[i]._element:
      i+=1
    node._children.append(newchild)
    for j in range(numChild,i,-1):
      temp= node._children[j]
      node._children[j]=node._children[j-1]
      node._children[j-1]=temp
    return self._make_position(newchild)

  def _replace(self,p,e):
    """Replace the element at position p with e, and return old element."""
    node = self._validate(p)
    old = node._element
    node._element = e
    return old

  #DA ELIMINARE
  def _delete(self,p):
    pass









  

  


    

    



