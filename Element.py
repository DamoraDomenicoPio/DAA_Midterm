class Element:
    
    __slots__='_num'

    def __init__(self, num):
        self._num=num

    def get(self):
        return self._num

    def __lt__(self, other):
        #print(other.e.get())
        return self._num < other._num
