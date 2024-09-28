from ..base.include.BasisSquare import *
from .references import CAMER_OBJ

@final
class Camera(BasisSquare):
    def __init__(self, name: str, 
                 zone:BasisSquare,
                 look:BasisSquare,
                 static:bool = True,
                 comment: str | None = None) -> None:
        super().__init__(name, len(CAMER_OBJ), "cam", comment)
        super().__square__()
        self.focus = look
        self.zone  = zone
        
        self.static = secure_type_one(value=static, kind=True)
        self.square_render()
        self.render_image("experimental")
        CAMER_OBJ.append(self)
        
    def square_render(self,
                      left:int=-4,  up:int=3, 
                      right:int=5, down:int=-2):
        
        self.coords = [secure_type_one(value=left,kind=1), 
                       secure_type_one(value=up,kind=1), 
                       secure_type_one(value=right, kind=1), 
                       secure_type_one(value=down, kind=1)
                       ]
        
    def render_image(self, kind:Literal["normal", "experimental"]="normal"):
        self.del_square()
        self.del_pre_view()
        
        if self.static:
            cur_ren_x, cur_ren_y = self.focus.vec
        else:
            cur_ren_x, cur_ren_y = self.focus.global_x, self.focus.global_y
              
        if kind == "normal":
            #NOTE: Este metodo soporta dentro de los limites, pero no es adaptable
            c=0
            for y in range(cur_ren_y+self.coords[3], cur_ren_y+self.coords[1]):
                line = self.zone.square[y][cur_ren_x+self.coords[0]:cur_ren_x+self.coords[2]]
                if DEBUG_MODE[0]:
                    self.square.append(line+f"\t\tline {self.zone.abs}: {y} {self.abs}: {c}")
                else:
                    self.square.append(line)
                c+=1
        elif kind == "experimental":
            #NOTE: este metodo es experimental, los inputs a ratos les pica
            # por hacer cualquier cosa
            for y in range(self.zone.vec[1]):
                if y in range(cur_ren_y + self.coords[3], cur_ren_y+self.coords[1]):
                    for x in range(self.zone.vec[0]):
                        if x in range(cur_ren_x+self.coords[0], cur_ren_x+self.coords[2]):
                            self.pre_view += self.zone.square[y][x]
                    if DEBUG_MODE[0]:
                        self.square.append(self.pre_view+f"\t\tline {self.zone.abs}: {y}") 
                    else:
                        self.square.append(self.pre_view)
                    self.del_pre_view()
        self.set_pre_view()
                    
                        
        