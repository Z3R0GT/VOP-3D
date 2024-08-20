from ..include.BasisViewport import *

def _insert_(old_:str|list, new_:str|list, 
             from_:int=..., to_:int=..., 
             specific_:int=...) -> str:
    temp = []
    new = ""
    cont = 0

    #print(f"Viejo: {len(old_)}", 
    #       f"Nuevo: {len(new_)}",
    #       f"Desde: {from_}",f"Hasta: {to_}", 
    #       f"Especifico: {specific_}" )

    for i in range(len(old_)):
        temp.append(old_[i])

    if to_ is ... and from_ is not ...:
        to_ = len(new_) + from_

    for mw in range(len(temp)):
        if specific_ is not ...:
            if mw > 0 and mw == specific_:
                temp[mw] = new_
        elif mw in range(from_, to_):
            temp[mw] = new_[cont]
            cont += 1

    for i in range(len(temp)):
         new += temp[i]

    return new

class BasisSquare(BasisViewPort):
    """Conjunto de funciones horientados a los cuadrados en sus diferentes
    direcciones, tamaños y vectores

    Args:
        BasisViewPort (BasisViewPort): clase base de todo objeto que se puede ver
    """
    def __tranform_2d__(self, size_x:int, size_y:int):
        """Otorga al objeto un tranformador en 2D

        Args:
            size_x (int): tamaño en X
            size_y (int): tamaño en Y
        """
        self.transform = [size_x, size_y]
        self.__set_meta__("transform", self.transform)

    def __tranform_3d__(self, size_x:int, size_y:int, size_z:int):
        """Otorga al objeto un transformador en 3D

        Args:
            size_x (int): tamaño en X
            size_y (int): tamaño en Y
            size_z (int): tamaño en Z
        """
        self.transform = [size_x, size_y, size_z]
        self.__set_meta__("transform", self.transform)
    
    def __set_vec_2d__(self, x:int, y:int):
        """Otorga al objeto una representación de vector en 2D

        Args:
            x (int): posición en X
            y (int): posición en Y
        """
        self.vec = [x, y]
        self._tmp_vec_ = [x, y]

        self.__set_meta__("vec", self.vec)

    def __set_vec_3d__(self, x:int, y:int, z:int):
        """Otorga al objeto una representación de vector en 3D

        Args:
            x (int): posición en X
            y (int): posición en Y
            z (int): posición en Z
        """
        self.vec = [x, y, z]
        self._tmp_vec_ = [x, y, z]

        self.__set_meta__("vec", self.vec)

    def _set_line_square_2d_(self):
        """Crea con base al cuadrado en 2D un frame de la vista actual del objecto
        """
        for y in range(self.vec[1]):
            for x in range(self.vec[0]):
                self.pre_view += self.character
            self.__del_pre_view__()
        del y, x
    
    def _set_frame_num_square_2d_(self, vec_x:int):
        """Crea una linea debajo del cuadrado actual con base a vector X

        Args:
            vec_x (int): limite de numero a parecer
        """
        self.__del_pre_view__()

        line_all = ""
        line_num = ""
        nro      = 0

        for num in range(vec_x):
            re = num%10
            line_all+= str(re)
            if re == 0:
                line_num += f"{nro}"
                nro += 1
            else:
                line_num+=" "

        self.square.append(line_all)
        self.square.append(line_num)
        self.__set_pre_view__()
        del line_all, line_num, nro

    def _edit_line_square_2d_(self, coords:list[tuple[int, int]], CHR:str="") -> tuple[bool,int]:
        """Edita una linea o serie de lineas con base a unas coordenadas dadas
        reemplazando en todo momento con los caracteres nuevos mantiendo la misma
        lista 

        Args:
            coords (list[tuple[int, int]]): coordenadas o lista de coordenadas
            CHR (str, optional): caracter a insertar dentro de dichas coordenadas. Defaults to "".

        Returns:
            tuple[bool,int]: representación FINAL de la operación hecha
        """
        checker_coord(coords)
        self.__del_pre_view__()

        for _in_ in coords:
            len_chr = len(CHR)
            if len_chr >= self.vec[0]:
                #add
                self.square[_in_[1]] = _insert_(self.square[_in_[1]], f"{CHR}", from_=_in_[0], to_=self.vec[0])
                #security
                self.square[_in_[1]] = _insert_(self.square[_in_[1]], f"{self.character}", specific_=self.vec[0]-1)

                return True, int(len_chr-self.vec[0])
            else:
                self.square[_in_[1]] = _insert_(self.square[_in_[1]], f"{CHR}", from_=_in_[0], to_=_in_[0]+len_chr)
                return False, 0 
        del _in_, len_chr
        self.__set_pre_view__()

    def _set_frame_square_2d_(self, coords:list[int, int],
                             single:Literal["last", "start", "none"]="none",
                             chr="") -> None | str:
        checker_coord(coords)

        temp = self.character
        if not chr == "":
            self.character = chr
        else:
            del temp

        for y in range(coords[1]):
            if y == 0 or y == (coords[1]-1):
                temp_line = f"{self.character}" * coords[0]
            else:
                temp_line = f"{self.character}"+ " " * (coords[0] - 2) + f"{self.character}"

            if single in ["last", "start"]:
                return temp_line
            elif DEBUG_MODE:
                self.square.append(temp_line+f"     line {self.abs}: {y}")
            else:
                self.square.append(temp_line)

        self.__set_pre_view__()
        if not chr == "":
            self.character = temp
