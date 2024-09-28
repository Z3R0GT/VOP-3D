from .....base.include.BasisSquare import *

def _cord(lst:list[str], chr:str)->int:
    c=-1
    for ch in lst:
        c+=1
        if ch != chr:
            return c
        
#conjunto de piezas que resumen/acortan información
class Chunkcs():
    
    def __mem_chunks__(self, components_exe:list[str]=[]) -> None:#<- requerido para evitar calcular las mismas cosas
        self.chunks:dict   ={} 
        self.comp:list[str]=components_exe
    
    #TODO: mejorar esta función para hacerla más "dinamica" 
    # para otra clase de objetos que no sean netamente "cuadrados/triangulos"
    def generate_chunks(self) -> dict:  
        tmp = {}     
        c = 0
        for node in self.child_lst:
            node:BasisSquare
            nme = f"{node.name.replace(" ", ".")}_{node.abs}_{c}"
            c+=1
            if node.abs in self.comp:
                continue
            
            kind = node.kind_vector()
            
            if kind[1] == "vec":
                rgn_x = range(kind[0][0], kind[0][0]+1)
                rgn_y = range(kind[0][1], kind[0][1]+1)
            elif kind[1] == "trans":
                rgn_x = range(node.vec[0], node.vec[0]+kind[0][0])
                rgn_y = range(node.vec[1], node.vec[1]+kind[0][1])

            tmp[nme] = [rgn_x,
                        rgn_y ]
        
        self.chunks = tmp
        return tmp
        
    #NOTE: esta función escanea las lineas y retorna con base a una posición 
    # donde esta la "siguiente" colisión base a que una caracter != " "
    # ojo que puede quedar BUG
    def next_to(self, node:Vector, what:str=" ", parts:bool=False)->list[list[int, int], list[int, int]]|list[int, int, int, int]: #<- retorn la diferencia dado una coordenada (X/Y)
        coord = node.vec
        
        ln_y_pos = [self.square[i][coord[0]] for i in range(0, coord[1])]
        ln_y_pos.reverse()
        ln_y_neg = [self.square[i][coord[0]] for i in range(coord[1]+1, self.vec[1])]
        
        ln_x_pos = [self.square[coord[1]][i] for i in range(0, coord[0])]
        ln_x_pos.reverse()

        ln_x_neg = [self.square[coord[1]][i] for i in range(coord[0]+1, self.vec[0])]
        
        left = [_cord(ln_x_pos, what), _cord(ln_y_neg, what)]
        right= [_cord(ln_x_neg, what), _cord(ln_y_pos, what)]
        if parts:
            return left, right
        else:    
            return  [left[0], left[1], right[0], right[1]]