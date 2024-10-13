from ...models.data.d2.player import Player, override, secure_type_one, PLAYING
from .UI import *

class User(Player):
    def __init__(self, name: str, chr: str, 
                 x: int, y: int, *, comment: str | None = None) -> None:
        super().__init__(name, chr, 
                         x, y, comment=comment)
        
    @override
    def key_input(self, key:str):
        #reservado
        key = key.lower()
        if key in self.controll[:4]:
            self.mover(key)
        else:
            try:
                _id_ = self.controll.index(key)
                self.config[_id_-4]() #quita los primeros encontrados
            except ValueError:
                pass
            
    @override     
    def adder(self, node):
        node = secure_type_one(node=node, abs="obj")
        re = node.canEffect(self.stats)
        print(node.name)
        if re:
            self.apply_effects(re)
            return True
        else:
            return re