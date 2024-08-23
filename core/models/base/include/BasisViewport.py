from .BasisNode import *
VIEWPORT_LIMIT = 2

def checker_coord(line:list, limit:list):
    if not type(line) == type([]):
        raise IncorrectVector(line)
    if not len(line) == VIEWPORT_LIMIT:
        raise CoordNotFound(line)
    if limit == "ex":
        return
    if (not line[0] < limit[0]) or (not line[1] < limit[1]):
        raise CoordExced(line, limit)

class BasisViewPort(BasisNode):
    def __viewport__(self) -> None:
        """Agrega las propiedad 'square' y 'pre_view'
        """
        self.square = []
        self.pre_view = ""

    def __set_pre_view__(self):
        """Crea un frame de como se ve actualmente
        """
        self.__del_pre_view__()
        for line in self.square:
            self.pre_view += f"{line}\n"

    def __del_pre_view__(self):
        """Purga la variable 'pre_view'
        """
        self.pre_view = ""
    
    def get_pre_view(self, isPrint:bool=True) -> str:
        """Imprime la variable 'pre_view' y la retorna

        Args:
            isPrint (bool, optional): ¿puede imprimir la variable?. Defaults to True.

        Returns:
            str: 'pre_view' en estado puro
        """
        if isPrint:
            print(self.pre_view)
        return self.pre_view
    


    def __del_square__(self):
        """Purga la variable 'square'
        """
        self.square = []

    def get_square(self) -> list:
        """retorno el actual 'square'

        Returns:
            list: 'square' en estado puro
        """
        return self.square