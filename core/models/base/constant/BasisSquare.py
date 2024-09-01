"""
Nodo base para todo objeto que tiene tamaño de pantalla

Contribuidores
-------------
    Z3R0_GT: 0.0.0.1 \n
        contac.es.z3r0.gt@gmail.com

Registro
--------
    Importaciones relativas: 0.0.0.1
        * imports
    
Modulos incluidos
-----------------
    BasisViewPort: 0.0.0.1
        nodo base para la pantalla
"""
if __name__ == "__main__":
    from sys import exit
    exit(1)

from ..include.BasisViewport import *
    
COMPONENTS_UI_VE = ["men"]
COMPONENTS_UI_TF = ["pnl"]
    
def insert(old_:str|list, new_:str|list, 
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
    
    @overload
    def __vector__(self, chr:str, x:int, y:int) -> None:...
    @overload
    def __vector__(self, chr:str, x:int, y:int, z:int) -> None:...
    def __vector__(self, *args):
        if len(args) == 3:
            self.character = args[0]
        
            self.vec       = [args[1], args[2]]
            self._tmp_vec_ = [args[1], args[2]]
            
            self.__set_meta__("chr", self.character)
            self.__set_meta__("vec", self.vec)
        elif len(args) == 4:
            self.character = args[0]
            
            self.vec       = [args[1], args[2], args[3]]
            self._tmp_vec_ = [args[1], args[2], args[3]]
            
            self.__set_meta__("chr", self.character)
            self.__set_meta__("vec", self.vec)
            
    @overload
    def __transform__(self, size_x:int, size_y:int) -> None:...
    @overload
    def __transform__(self, size_x:int, size_y:int, size_z:int) -> None:...
    def __transform__(self, *args):
        if len(args) == 2:
            self.transform = [args[0], args[1]]
            self.__set_meta__("transform", self.transform)
        elif len(args) == 3:
            self.transform = [args[0], args[1], args[2]]
            self.__set_meta__("transform", self.transform)
    
    def _set_line_square_(self):
        for y in range(self.vec[1]):
            for x in range(self.vec[0]):
                self.pre_view += self.character
            self.__del_pre_view__()
        del y, x

    def _set_frame_num_square_(self, vec_x:int):
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

    def _edit_line_square_(self, coords:list[tuple[int, int]], 
                           CHR:str="") -> tuple[bool,int]:
        if self.abs in COMPONENTS_UI_VE:
            vec = self.vec
        elif self.abs in COMPONENTS_UI_TF:
            vec = self.transform

        for i in coords:
            checker_coord(i, vec)
        self.__del_pre_view__()

        for _in_ in coords:
            len_chr = len(CHR)
            if len_chr >= vec[0]:
                #add
                self.square[_in_[1]] = insert(self.square[_in_[1]], f"{CHR}", from_=_in_[0], to_=vec[0])
                #security
                self.square[_in_[1]] = insert(self.square[_in_[1]], f"{self.character}", specific_=vec[0]-1)

                return True, int(len_chr-vec[0])
            else:
                self.square[_in_[1]] = insert(self.square[_in_[1]], f"{CHR}", from_=_in_[0], to_=_in_[0]+len_chr)
                return False, 0 
        del _in_, len_chr
        self.__set_pre_view__()

    def _set_frame_square_(self, coords:list[int, int],
                             single:Literal["last", "start", "none"]="none",
                             chr="") -> None | str:
        checker_coord(coords, "ex")

        temp = self.character
        if not chr == "":
            self.character = chr
        else:
            del temp
        print(coords, self.character)
        for y in range(coords[1]):
            if y == 0 or y == (coords[1]-1):
                temp_line = f"{self.character}" * coords[0]
            else:
                temp_line = f"{self.character}"+ " " * (coords[0] - 2) + f"{self.character}"

            if single in ["last", "start"]:
                return temp_line
            elif DEBUG_MODE[0]:
                self.square.append(temp_line+f"     line {self.abs}: {y}")
            else:
                self.square.append(temp_line)

        self.__set_pre_view__()
        if not chr == "":
            self.character = temp




