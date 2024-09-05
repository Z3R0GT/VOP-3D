if __name__ == "__main__":
    from sys import exit
    exit(1)

from .BasisNode import *

VIEWPORT_LIMIT:int=2

def checker_coord(line:list[int, int, int]|list[int, int],
                  limit:list[int, int, int]|list[int, int]|Literal["ex"]
                  ):
    if not hasattr(line, "append"):
        raise IncorrectTypeNode(line)    
    if not len(line) == VIEWPORT_LIMIT:
        raise CoordNotFound(line)
    
    if limit == "ex":
        return
    
    if not hasattr(limit, "append"):
        raise IncorrectTypeNode(limit)
    if not len(limit) == VIEWPORT_LIMIT:
        raise CoordNotFound(limit)
    
    if line[0] > limit[0] or line[0] < 0:
        raise CoordExced(line[0], limit[0])
    if line[1] > limit[1] or line[1] < 0:
        raise CoordExced(line[1], limit[1])

class BasisViewPort(BasisNode):
    def __viewport__(self) -> None:
        self.square = []
        self.pre_view = ""

    def __set_pre_view__(self):
        self.__del_pre_view__()
        for line in self.square:
            self.pre_view += f"{line}\n"

    def __del_pre_view__(self):
        self.pre_view = ""
    
    def get_pre_view(self, isPrint:bool=True) -> str:
        if isPrint:
            print(self.pre_view)
        return self.pre_view
    
    
    def __del_square__(self):
        self.square = []

    def get_square(self) -> list:
        return self.square