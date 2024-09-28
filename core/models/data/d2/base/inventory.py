from typing import Literal

class Inventory():
    def __meta__(self, 
                 requeriments:dict|Literal["None"],
                 effects:dict|Literal["None"],
                 ) -> None:
        self.req = requeriments
        self.eff = effects
        
    #TODO: requiere de varios "secure_type_one"
    def canEffect(self, input:dict) -> dict:
        #si el objeto no tiene ninguna clase de requerimiento
        if self.req == "None":
            return self.eff
        #se asegura que la entrada dada tiene lo requisitos, sino
        for i in input:
            if not self.req.__contains__(i):
                return False #NotEnoughRequeriments (si, es basura XD)
            
        kind_inp = list(input.keys())
        
        for i in kind_inp:
            #int
            if type(self.req[i]) == type(1) and not self.req[i] >= input[i]:
                return False #NotEnough 
            #str
            if not self.req[i] == input[i]:
                return False

            return self.eff
        return False
            