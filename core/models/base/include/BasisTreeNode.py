from .BasisNode import *

__ch_attr__ =  ["father", "in_id"]
__fa_attr__ = ["child_lst", "child_tlt"]

__mo_ch_attr__ = ["node_f", "node_t"]
__mo_fa_attr__ = ["node_f"]

def _coin(lst:list, info:dict):
    tmp = []
    for node in lst:
        
        for proper in info:
            if node.meta[proper] == info[proper]:
                tmp.append(node)
        
    return tmp
class BasisTreeNode(BasisNode):
    def __father_node__(self, components:list) -> None:
        self.child_lst:list[BasisNode]= []
        self.child_tlt:int            = 0
        
        self.comp_ch = components
        self.update_node()
    
    def __child_node__(self, components:list) -> None:
        self.father:list[BasisNode] = []
        self.in_id :list[int]       = []
        
        self.comp_fa = components
        
        self.update_node()
        
    def add_child(self, node:BasisNode, is_new:bool=True):
        self.can_be_added(node, throw=True)
        node.can_be_added(self, kind="fa", throw=True)
        
        if is_new:
            node.in_id .append(self.child_tlt)
            node.father.append(self)
            
            node.update_node()
        
            self.child_lst.append(node)
            self.child_tlt+=1
            
            self.update_node()
        
        if hasattr(self, "adder"):
            self.adder(node)
        else:
            print("Metodo 'adder' no encontrado, continuando con la ejecución")
            
    def edit_child(self, node:BasisNode, **kwargs):
        self.can_be_added(node, throw=True)
        node.can_be_added(self, kind="fa", throw=True)
        
        if hasattr(self, "editter"):
            self.editter(node, kwargs)
        else:
            print("Metodo 'editter' no encontrado, continuando con la ejecución")

    def del_child(self, node:BasisNode, *, kind:Literal["static", "dinamic"]="static", is_new:bool=True):
        self.can_be_added(node, throw=True)
        node.can_be_added(self, kind="fa", throw=True)
        
        ID =  node.in_id[node.father.index(self)]
        if is_new:
            if kind =="static":
                self.child_lst[ID] = 0
                node.father[ID]    = 0
            elif kind == "dinamic":
                self.child_tlt-=1
                del self.child_lst[ID]
                for i in range(ID, self.child_tlt):
                    nod = self.child_lst[i]
                    #BUG: en caso se bug, el concepto es que el nodo hijo restante, 
                    # se reste su propio IN_ID apartir del que fue borrado
                    nod.in_id[nod.father.index(self)]-=1
                    #print(IN_ID)
                    #nod.in_id[IN_ID] -= 1
                    nod.set_meta("in_id", nod.in_id)

            self.update_node()
            node.__child_node__(node.comp_fa)

        if hasattr(self, "deleter"):
            self.deleter(node)
        else:
            print("Metodo 'deleter' no encontrado, continuando con la ejecución")

    def update_father(self, kind:Literal["adder", "deleter"]="adder"):
        for i in self.father:
            if hasattr(i, kind):
                if kind == "adder":
                    i.adder(self)
                elif kind == "deleter":
                    i.deleter(self)
            else:
                print("Metodo adder no encontrado, continuando ejecución")

    def find_child(self, info:dict) -> list:
        return _coin(self.child_lst, info)

    def find_father(self, info:dict) -> list:        
        return _coin(self.father, info)
        
    @deprecated("requiere muy probablemente un renombre para no tener conflictos con move_to de 'Skeleton'")
    def move_to_child(self,**kwargs):
        if contains(kwargs, __mo_ch_attr__):
            secure_type_one(kwargs["node_f"], kwargs["node_t"], __fa_attr__, __ch_attr__)
            node_f = kwargs["node_f"]
            node_t = kwargs["node_t"]
            
            self.can_be_added(node_f, throw=True)
            self.can_be_added(node_t, throw=True)
            
            node_f.can_be_added(self, kind="fa", throw=True)
            node_t.can_be_added(self, kind="fa", throw=True)
            #TODO: possible bugs here, need more test
            id_f = node_f.father.index(self)
            id_t = node_t.father.index(self)
            
            self.child_lst[node_f.in_id[id_f]] = node_t
            self.child_lst[node_t.in_id[id_t]] = node_f
            
            id_t_tmp = node_t.in_id[id_t]
            node_t.in_id[id_t] = node_f.in_id[id_f]
            node_f.in_id[id_f] = id_t_tmp
            
            self.update_node()
            node_t.update_node()
            node_f.update_node()
        elif contains(kwargs, __mo_fa_attr__):
            #TODO: este codigo se encargara de mover desde
            # un mismo objeto hijo hacia otro padre
            # los posibles argumentos: node_f, node_t (father_f, father_t)
            # ademas al final llama a la función "mover" para cambiar ello
            ...
        else:
            #TODO: requiere cambiar este comentario
            print("lo argumentos dados no son suficientes")
            
    def can_be_added(self, node:BasisNode, *, kind:Literal["ch", "fa"]="ch", throw:bool=False) -> bool:
        try:
            if kind == "ch":
                result = hasmutlattr(node, __ch_attr__) and node.abs in self.comp_ch
                if throw and not result:
                    raise IsNotAChild(node, self)
                return result
                
            elif kind == "fa":
                result = hasmutlattr(node, __fa_attr__) and node.abs in self.comp_fa
                if throw and not result:
                    raise IsNotAFather(node, self)
                return result
        except AttributeError:
            raise IncorrectTypeNode(self, node)
        
    def as_connection(self) -> tuple[bool, bool]:
        ch = hasattr(self, "child_lst") and len(self.child_lst)!=0 #cuando es padre
        fa = hasattr(self, "fahter") and len(self.father) != 0     #cuando es hijo
    
        return ch, fa
        
    def get_childs(self, kind:str|Literal["all"])-> list:
        if not kind == "all":
            return [i for i in self.child_lst if i.abs == kind]
        else:
            return self.child_lst
        
    def update_node(self):
        if hasmutlattr(self, __ch_attr__):
            self.set_meta("father", [i.get_meta(False) for i in self.father])
            self.set_meta("in_id", self.in_id)
        if  hasmutlattr(self, __fa_attr__):
            self.set_meta("child_lst", [i.get_meta(False) for i in self.child_lst])
            self.set_meta("child_tlt", self.child_tlt)