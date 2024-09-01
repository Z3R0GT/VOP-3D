"""
Conjunto de excepciones generales que puede o no lanzarse de vez
en cuanto obtengas alguno de estos muy probablemente no quieras
volver a usar esto

Contribuidores
-------------
    Z3R0_GT: 0.0.0.1 \n
        contac.es.z3r0.gt@gmail.com

Registro
--------
    Coordenadas: 0.0.0.1
        * se agregaron excepciones para las coordenadas 
    

"""


#######################
#######################
#     Coordenadas     #
#######################
#######################
class CoordNotFound(ValueError):
    def __init__(self, coord:list, *args: object) -> None:
        """Lanzado cuando las coordenadas no son suficientes"""
        self.message = f"Se necesitan una o más coordenadas ({coord}, {len(coord)})"
        self.foo = coord
        super().__init__(self.message,*args)
        
class CoordInConflic(ValueError):
    def __init__(self, node_from, node_to, *args: object) -> None:
        """Lanzado cuando la coordenada esta en conflicto a otra"""
        self.message = f"El nodo ({node_from.name}) esta en conflicto con {node_to.name} \nMETA {node_from.name}: {node_from.meta}\nMETA {node_to.name}: {node_to.meta}"
        self.foo = (node_from, node_to)
        super().__init__(self.message,*args)
        
class CoordExced(ValueError):
    def __init__(self, limit_from:list[int, int]|int, limit_to:list[int, int]|int, *args: object) -> None:
        """Lanzado cuando alguna coordenada esta fuera del limite"""
        self.message = f"Una o más coordenadas están fuera del limite; obtenida: {limit_from} limite: {limit_to}"
        self.foo = (limit_from, limit_to)
        super().__init__(self.message, *args)
        

#######################
#######################
#     Incorrectos     #
#######################
#######################
class IncorrectVector(TypeError):
    def __init__(self, node, *args: object) -> None:
        """Lanzado cuando el vector no es una lista"""
        self.message = f"Se necesita una lista, no {type(node)}"
        self.foo = node
        super().__init__(self.message, *args)

class IncorrectTypeNode(TypeError):
    def __init__(self, node,*args: object) -> None:
        """Lanzado cuando un nodo es incorrecto"""
        self.message = f"El nodo {type(node)} <--> {node.name} no es compatible"
        self.foo = node
        super().__init__(self.message, *args)
        

#######################
#######################
#     Arbol nodos     #
#######################
#######################
class IsNotAChild(AttributeError):
    def __init__(self, node, *args: object) -> None:
        """Lanzado cuando un nodo no es un hijo"""
        self.message = f"El objeto {node.name} no es un hijo o no puede ser hijo"
        self.foo = node
        super().__init__(self.message, *args)
        
class IsNotFather(AttributeError):
    def __init__(self, node, *args: object) -> None:
        """Lanzado cuando un nodo no es un padre"""
        self.message = f"El objeto {node.name} no es un padre o no puede ser padre"
        self.foo = node
        super().__init__(self.message, *args)
        