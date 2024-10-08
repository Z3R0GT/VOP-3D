from .....base.include.BasisSquare import *
        
def _coord(line:list[str], what:str):
    tmp = []
    for i in line:
        if i == what:
            tmp.append(i)
        else:
            return tmp
    return tmp
        
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
        #TODO: agregar un type_verify_one aqui
        #TODO: plantearse mejor la forma en la que verifica las coordenadas 
        if node.abs in ["pla"]:
            coord = [node.global_x, node.global_y]
        else:
            coord = node.vec
        
        #TODO: refactorizacion urgente!
        ln_y_pos = [self.square[i][coord[0]] for i in range(0, coord[1])]
        ln_y_pos.reverse()
        ln_y_neg = [self.square[i][coord[0]] for i in range(coord[1]+1, self.vec[1])]
        
        ln_x_neg = [self.square[coord[1]][i] for i in range(0, coord[0])]
        ln_x_neg.reverse()
        ln_x_pos = [self.square[coord[1]][i] for i in range(coord[0]+1, self.vec[0])]
        
        ln_y_pos = _coord(ln_y_pos, what)
        ln_y_neg = _coord(ln_y_neg, what)
        
        ln_x_pos = _coord(ln_x_pos, what)
        ln_x_neg = _coord(ln_x_neg, what)

        negative = [len(ln_x_neg), len(ln_y_neg)]
        positive = [len(ln_x_pos), len(ln_y_pos)]
        if parts:
            return negative, positive
        else:    
            return  negative + positive