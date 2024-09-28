from .Vector import *

class text(Vector):
    def __init__(self, 
                 name: str,
                 text: str,
                 id:int,
                 abs:str,
                 x:int,
                 y:int,
                 comment: str | None = None) -> None:
        super().__init__(name, id, abs, comment)
        super().__vector__(chr=text, x=x, y=y)
        
    