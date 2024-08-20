from typing_extensions import Literal
from .BasisNode import BasisNode

class BasisTreeNode(BasisNode):

    def __father_node__(self):
        """Crea las variables 'child_lst' y 'child_total' al nodo
        """
        self.child_lst = []
        self.child_total = 0

        self.__set_meta__("child_lst", self.child_lst)
        self.__set_meta__("child_total", self.child_total)

    def __child_node__(self, father, in_id:int):
        """Crea las variables 'father_nod' y 'in_id' (inside ID)

        Args:
            father (_type_): Puede ser cualquier nodo que tenga 'father_node' en su __init__
            in_id (int): es igual al total de nodo dentro de 'child_lst' (usar 'child_total' en su lugar)
        """
        self.father_node = father
        self.in_id = in_id

        self.__set_meta__("father", self.father_node)
        self.__set_meta__("in_id", in_id)

    def add_child(self, child):
        """Agrega a un hijo a los nodos que tenga 'father_node' en su __init__
        (puede escribir un metodo 'adder' para darle más funcionalidad)
        Args:
            child (_type_): referencia en memoria del nodo
        """
        self.child_lst.append(child)
        self.child_total += 1

        self.__set_meta__("child_lst", self.child_lst)
        self.__set_meta__("child_total", self.child_total)

        #ESTE METODO DEPENDERA DEL OBJETO PARA COMPLETAR LA ACCION
        self.adder()

    def edit_child(self, child):
        ...

    def del_child(self, child, kind:Literal["static","dinamic"]="static"):
        """Borra a un nodo hijo del padre (no se puede recuperar luego)
        (puede escribir un metodo 'deleter' para darle más funcionalidad)
        Args:
            child (_type_): referencia en memoria del nodo
            kind (Literal[&quot;static&quot;,&quot;dinamic&quot;], optional): tipo de operación (static mantendra la lista de hijos, mientras que dinamic la modificara, eso incluye los 'in_id' de los hijos). Defaults to "static".
        """
        if kind == "static":
            self.child_lst[child.in_id]=0
        elif kind =="dinamic":
            self.child_total-=1
            del self.child_lst[child.in_id]
            for i in self.child_lst:
                i.in_id -=1

        self.__set_meta__("child_lst", self.child_lst)
        self.__set_meta__("child_total", self.child_total)

        #ESTE METODO DEPENDERA DEL OBJETO PARA COMPLETAR LA ACCION
        self.deleter()

    def move_child(self, child_from, child_to):
        """Mueve un hijo a otra posición dentro de la lista del padre
        Args:
            child_from (_type_): Hijo que quieres mover hacia
            child_to (_type_): Hijo que quieres mover donde
        """
        tmp = child_from

        self.child_lst[child_from.in_id] = child_to
        self.child_lst[child_to.in_id] = tmp
        
        self.__set_meta__("child_lst", self.child_lst)

        
    def move_father(self, father_to):
        """Mover un nodo hijo hacia otro padre 
        (puede escribir un metodo 'mover' para darle más funcionalidad)
        
        Args:
            father_to (_type_): _description_
        """
        self.father_node.del_child(self, "dinamic")

        father_to.add_child(self)
        self.in_id = father_to.child_total-1

        self.mover()
        

