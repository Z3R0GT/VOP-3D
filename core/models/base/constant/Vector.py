from ..include.BasisNode import *

COMPONENTS_VE = ["men", "map", "txt", "pla", "obj", "dor"]
COMPONENTS_TF = ["pnl", "stu"]

__vector_2d_att__ = ["chr", "x", "y"]
__vector_3d_att__ = ["chr", "x", "y", "z"]

__transform_2d_att__ = ["size_x", "size_y"]
__transform_3d_att__ = ["size_x", "size_y", "size_z"]

class Vector(BasisNode):
    def __vector__(self, **kwargs:dict):
        if contains(kwargs, __vector_2d_att__):
            self.character = secure_type_one(value=kwargs["chr"], kind="a")
            
            self.vec       = [secure_type_one(value=kwargs["x"], kind=1), secure_type_one(value=kwargs["y"], kind=1)]
            self._tmp_vec_ = [secure_type_one(value=kwargs["x"], kind=1), secure_type_one(value=kwargs["y"], kind=1)]
            
            self.set_meta("chr", self.character)
            self.set_meta("vec", self.vec)
        elif contains(kwargs, __vector_3d_att__):
            self.character = secure_type_one(value=kwargs["chr"], kind="a")
            
            self.vec       = [secure_type_one(value=kwargs["x"], kind=1), secure_type_one(value=kwargs["y"], kind=1), secure_type_one(value=kwargs["z"], kind=1)]
            self._tmp_vec_ = [secure_type_one(value=kwargs["x"], kind=1), secure_type_one(value=kwargs["y"], kind=1), secure_type_one(value=kwargs["z"], kind=1)]
            
            self.set_meta("chr", self.character)
            self.set_meta("vec", self.vec)
        else:
            raise TypeError("El objeto requiere más/menos argumento de los dados")
            
    def __transform__(self, **kwargs:dict):
        if contains(kwargs, __transform_2d_att__):
            self.transform = [secure_type_one(value=kwargs["size_x"], kind=1), secure_type_one(value=kwargs["size_y"], kind=1)]
            self.set_meta("transform", self.transform)
        
        elif contains(kwargs, __transform_3d_att__):
            self.transform = [secure_type_one(value=kwargs["size_x"], kind=1), secure_type_one(value=kwargs["size_y"], kind=1), secure_type_one(value=kwargs["size_z"], kind=1)]
            self.set_meta("transform", self.transform)
        else:
            raise TypeError("El objeto requiere más argumento de los dados")
    
    def kind_vector(self) -> tuple[list[int, int], Literal["vec", "trans"]]:
        if self.abs in COMPONENTS_VE:
            return self.vec, "vec"
        elif self.abs in COMPONENTS_TF:
            return self.transform, "trans"
        else:
            #TODO: requiere un mejor "mensaje" comico
            raise TypeError(f"¿como se te olvido colocar el objeto {self.abs} dentro de COMPONENTS")