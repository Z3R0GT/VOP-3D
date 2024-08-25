from typing_extensions import Literal
from .BasisNode import *

class BasisTreeNode(BasisNode):

    def __father_node__(self):
        """Crea las variables 'child_lst' y 'child_total' al nodo
        """
        self.child_lst:list[BasisNode] = []
        self.child_total = 0

        self.__set_meta__("child_lst", self.child_lst)
        self.__set_meta__("child_total", self.child_total)

    def __child_node__(self):
        """Crea las variables 'father_nod' y 'in_id' (inside ID)

        """
        self.father:BasisNode = ...
        self.in_id:int = ...

        self.__set_meta__("father", self.father)
        self.__set_meta__("in_id", self.in_id)

    def add_child(self, child, is_new:bool=True):
        """Agrega a un hijo a los nodos que tenga 'father_node' en su __init__
        (puede escribir un metodo 'adder' para darle más funcionalidad)
        Args:
            child (_type_): referencia en memoria del nodo
        """
        self.can_be_child(child, throw=True)
        self.can_be_father(self, throw=True)
        if child.father != ...:
            raise IncorrectTypeNode(child)

        if is_new:
            child.in_id  = self.child_total
            child.father = self

            child.__set_meta__("father", child.father)
            child.__set_meta__("in_id", child.in_id)

            self.child_lst.append(child)
            self.child_total += 1

            self.__set_meta__("child_lst", self.child_lst)
            self.__set_meta__("child_total", self.child_total)

        #ESTE METODO DEPENDERA DEL OBJETO PARA COMPLETAR LA ACCION
        if hasattr(self, "adder"):
            self.adder(child)
        else:
            print("Metodo 'adder' no encontrado, continuando con la ejecución")

    def edit_child(self, child, *args):
        self.can_be_child(child, throw=True)
        self.can_be_father(self, throw=True)

        #ESTE METODO DEPENDERA DEL OBJETO PARA COMPLETAR LA ACCION
        if hasattr(self, "editter"):
            self.editter(child, args)
        else:
            print("Metodo 'editter' no encontrado, continuando con la ejecución")


    def del_child(self, child, *, is_new:bool=True, kind:Literal["static","dinamic"]="static"):
        """Borra a un nodo hijo del padre (no se puede recuperar luego)
        (puede escribir un metodo 'deleter' para darle más funcionalidad)
        Args:
            child (_type_): referencia en memoria del nodo
            kind (Literal[&quot;static&quot;,&quot;dinamic&quot;], optional): tipo de operación (static mantendra la lista de hijos, mientras que dinamic la modificara, eso incluye los 'in_id' de los hijos). Defaults to "static".
        """
        self.can_be_child(child, throw=True)
        self.can_be_father(self, throw=True)

        if is_new:
            if kind == "static":
                self.child_lst[child.in_id]=0
            elif kind =="dinamic":
                self.child_total-=1
                del self.child_lst[child.in_id]
                for i in self.child_lst:
                    i.in_id -=1
                    i.__set_meta__("in_id", i.in_id)

            self.__set_meta__("child_lst", self.child_lst)
            self.__set_meta__("child_total", self.child_total)

            child.in_id = ...
            child.father = ...

            child.__set_meta__("father", child.father)
            child.__set_meta__("in_id", child.in_id)

        #ESTE METODO DEPENDERA DEL OBJETO PARA COMPLETAR LA ACCION
        if hasattr(self, "deleter"):
            self.deleter(child)
        else:
            print("Metodo 'deleter' no encontrado, continuando con la ejecución")


    def move_child(self, child_from, child_to):
        """Mueve un hijo a otra posición dentro de la lista del padre
        Args:
            child_from (_type_): Hijo que quieres mover hacia
            child_to (_type_): Hijo que quieres mover donde
        """
        self.can_be_child(child_from, throw=True)
        self.can_be_child(child_to, throw=True)
        self.can_be_father(self, throw=True)

        tmp = child_from

        self.child_lst[child_from.in_id] = child_to
        self.child_lst[child_to.in_id] = tmp
        
        self.__set_meta__("child_lst", self.child_lst)

    def can_be_child(self, node:BasisNode,* , components:list[str]=[], throw:bool=False) -> bool:
        """Pregunta si un el nodo puede o no ser un hijo

        Args:
            node (_type_): node que quieres hacer hijo
            throw (bool, optional): puede soltar una excepción?. Defaults to False.

        Raises:
            IsNotAChild: Lanzado si throw es True

        Returns:
            bool: literal de 'si' o 'no'
        """
        if components == []:
            con = hasattr(node, "in_id")
        else:
            con = node.abs in components

        if con:
            return True
        else:
            if throw:
                raise IsNotAChild(node)
            else:
                return False

    def can_be_father(self, node:BasisNode, *, components:list[str]=[], throw:bool=False) -> bool:
        """Pregunta si un el nodo puede o no ser un padre

        Args:
            node (_type_): node que quieres hacer padre
            throw (bool, optional): puede soltar una excepción?. Defaults to False.

        Raises:
            IsNotAFather: Lanzado si throw es True

        Returns:
            bool: literal de 'si' o 'no'
        """
        if components == []:
            con = hasattr(node, "child_lst")
        else:
            con = node.abs in components

        if con:
            return True
        else:
            if throw:
                raise IsNotAFather(node)
            else:
                return False
            
    def move_father(self, father_to):
        """Mover un nodo hijo hacia otro padre 
        (puede escribir un metodo 'mover' para darle más funcionalidad)
        
        Args:
            father_to (_type_): _description_
        """
        self.can_be_father(father_to, throw=True)
        self.can_be_father(self, throw=True)

        self.father.del_child(self, is_new=False, kind="dinamic")

        father_to.add_child(self)
        self.in_id = father_to.child_total-1
        if hasattr(self, "mover"):
            self.mover(father_to)
        else:
            print("Metodo 'mover' no encontrado, continuando con la ejecución")
        

