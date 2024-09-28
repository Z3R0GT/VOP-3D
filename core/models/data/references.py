MENU_OBJ   :list = []
BUTTONS_OBJ:list = []
PANEL_OBJ  :list = []
CAMER_OBJ  :list = []
MAP_OBJ    :list = []
STU_OBJ    :list = []
DOO_OBJ    :list = []
PLA_OBJ    :list = []
OBJ_OBJ    :list = []


def find_node(lst:list, what) -> bool:
    for i in lst:
        if i.name == what.name:
            return True
    return False

TPF = 0.15