#from ....util import *

def is_in_coords(current_coords:list[int, int], limit_coords:list[list[int, int]])-> bool:
    x = current_coords[0] in range(limit_coords[0][0], limit_coords[0][1])
    y = current_coords[1] in range(limit_coords[1][0], limit_coords[1][1]) 
    
    return x and y
    