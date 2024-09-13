from .BasisNode import *

class BasisTreeNode(BasisNode):
    def __father_node__(self, components:list):
        self.child_lst:list[BasisNode] = []
        self.child_tlt:int             = 0
        
        self.comp_ch = components
        
        self.__update_father__()
        
    def __child_node__(self, components:list):
        self.father:list[BasisNode] = []
        self.in_id :list[int]       = []
        
        self.comp_fa = components
        
        self.__update_child__()
        
        
    def add_child(self, node:BasisNode, is_new:bool=True):
        self.can_be_child (node, throw=True)
        node.can_be_father(self, throw=True) 
        
        if is_new:
            node.in_id .append(self.child_tlt)
            node.father.append(self)
            
            node.__update_child__()
            
            self.child_lst.append(node)
            self.child_tlt+=1
            
            self.__update_father__()

        if hasattr(self, "adder"):
            self.adder(node)
        else:
            print("Metodo 'adder' no encontrado, continuando con la ejecución")
            
    def edit_child(self, child:BasisNode, *args):
        self.can_be_child (child, throw=True)
        child.can_be_father(self , throw=True)   
    
        if hasattr(self, "editter"):
            self.editter(child, args)
        else:
            print("Metodo 'editter' no encontrado, continuando con la ejecución")

    def del_child(self, child:BasisNode,*, is_new:bool=True, kind:Literal["static", "dinamic"]="static"):
        self.can_be_child (child, throw=True)
        child.can_be_father(self , throw=True)    
         
        ID = child.father.index(self)
        
        if is_new:
            if kind == "static":
                self.child_lst[ID]= 0
                child.father[ID]  = 0
            elif kind == "dinamic":
                self.child_tlt-=1
                del self.child_lst[ID]
                for i in range(ID, self.child_tlt):
                    IN_ID = self.child_lst[i].father.index(self)
                    
                    self.child_lst[i].in_id[IN_ID] -= 1
                    self.child_lst[i].__set_meta__("in_id", self.child_lst[i].in_id)
            
            self.__update_father__()
    
            child.__child_node__(child.comp_fa)
            
        if hasattr(self, "deleter"):
            self.deleter(child)
        else:
            print("Metodo 'deleter' no encontrado, continuando con la ejecución")
        
    def can_be_child(self, node:BasisNode,*,throw:bool=False) -> bool:
        if hasattr(node, "father") and node.abs in self.comp_ch:
            return True
        else:
            if throw:
                raise IsNotAChild(node, self)
            else:
                return False
     
    def can_be_father(self, node:BasisNode,*,throw:bool=False) -> bool:
        if hasattr(node, "child_tlt") and node.abs in self.comp_fa:
            return True
        else:
            if throw:
                raise IsNotFather(node, self)
            else:
                return False
     
    def move_child(self, child_from:BasisNode, child_to:BasisNode):
        self.can_be_child(child_from, throw=True)
        self.can_be_child(child_to  , throw=True)
        child_from.can_be_father(self     , throw=True)
        child_to  .can_be_father(self     , throw=True)
        
        tmp = child_from
        self.child_lst[child_from.in_id] = child_to
        self.child_lst[child_to.in_id  ] = tmp
        
        self.__update_father__()
        

    def move_father(self, father_to:BasisNode):
        self     .can_be_father(father_to, throw=True)
        father_to.can_be_father(self     , throw=True)
        
        self.father.del_child(self, is_new=False, kind="dinamic")
        
        father_to.add_child(self)
        self.in_id = father_to.child_tlt-1
        
        if hasattr(self, "move"):
            self.move(father_to)
        else:
            print("Metodo 'mover' no encontrado, continuando con la ejecución")
   
        
    def __update_child__(self):
        self.__set_meta__("father", self.father)
        self.__set_meta__("in_id",  self.in_id)
    
    def __update_father__(self):
        self.__set_meta__("child_lst", self.child_lst)
        self.__set_meta__("child_tlt", self.child_tlt)