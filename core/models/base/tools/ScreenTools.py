"""
Nodo de utilidad para todo objeto que 
use directamente la pantalla

Contribuidores
-------------
    Z3R0_GT: 0.0.0.1 \n
        contac.es.z3r0.gt@gmail.com

Registro
--------
    Importaciones relativas: 0.0.0.1
        * imports
    
Modulos incluidos
-----------------
    BasisSquare: 0.0.0.1
        nodo base para todo objeto que tiene tamaño de pantalla
"""
import logging, sys
from os import system

from ...util import DEBUG_MODE

FIXER_X_SIZE:int = 5
FIXER_Y_SIZE:int = 6

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def erase_screen():
    """Borra la pantalla
    """
    if not DEBUG_MODE[0]:
        system("cls")


def size_screen(x:int=0, y:int=0, obj=...):
    """Cambia el tamaño de la consola actual

    Args:
        x (int, optional): tamaño literal de X. Defaults to 0.
        y (int, optional): tamaño literal de Y. Defaults to 0.
        obj (BasisSquare, optional): Objecto con 'vector' (es automatico). Defaults to ....
    """    
    if not (x == 0 or y==0):
        x_cols = obj.vec[0]+FIXER_X_SIZE
        y_lins = obj.vec[1]+FIXER_Y_SIZE
    else:
        x_cols = x+FIXER_X_SIZE
        y_lins = y+FIXER_Y_SIZE

    system(f"mode con:cols={x_cols} line={y_lins}")

def print_debug(*msg):
    """imprime algo en modo debug (se ve bonito XD)
    """
    logging.debug(msg)
