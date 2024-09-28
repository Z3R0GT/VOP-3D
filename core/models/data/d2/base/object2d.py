from core.models.base.tools.maths import insert
from .include.chunks import *
from .include.figure import *

class Object2D(Figures, Chunkcs):
    def __init__(self, name: str, 
                 id: int, abs: str, 
                 chr, x, y,
                 comment: str | None = None) -> None:
        super().__init__(name, id, abs, comment)
        super().__vector__(chr=chr, x=x, y=y)
        
    def insert_square(self, node):
        checker(line=node.vec,
                limit=self.kind_vector()[0],
                vector=2)
        checker(line=[node.vec[0]+node.transform[0], 
                      node.vec[1]+node.transform[1]
                      ], 
                limit=self.kind_vector()[0], 
                vector=2)
        checker(node_from=self, 
                node_to=node)
        
        c=0
        for y in range(node.vec[1], node.transform[1]+node.vec[1]):
            self.square[y] = insert(self.square[y], node.square[c], 
                                    node.vec[0],
                                    node.vec[0]+node.transform[0])
            c+=1
        self.set_pre_view()