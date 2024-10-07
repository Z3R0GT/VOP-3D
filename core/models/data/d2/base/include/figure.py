#quizas necesite una nueva vista
from .....base.include.BasisSquare import *
from .....base.constant.function import *

class Figures(BasisSquare):
    def create_triangule(self, base:int, height:int, dot:int, chr:str="",invert:bool=False) -> list[str]:
        tmp = []
        c=0
        if chr=="":
            chr = self.character
        
        for y in range(height):
            mn=""
            for x in range(base):
                if (x == dot-c or x==dot+c) or \
                ( (x>=base-1 and base-1<=dot+c ) or (x==0 and dot-c<=0) ) or \
                (y==height-1 and x>=dot-c and x<=dot+c): 
                    mn+=chr
                    continue
                mn+="-"
            tmp.append(mn)
            c+=1
        if invert:
            tmp.reverse()

        return tmp    
        
    def create_square(self, base:int, height:int, chr:str="", as_square:bool=True) -> list[str]:
        tmp = []
        if chr=="":
            chr = self.character
        
        for y in range(height):
            if not as_square:
                mn = " "*(base)
            else:
                if y==0 or y==height-1:
                    mn = f"{chr}"+" "*(base)
                else:
                    mn = f"{chr}"+" "*(base-2)+f"{chr}"
            tmp.append(mn)
        return tmp    
        

