import logging, sys
from os import system

from ...util import DEBUG_MODE

FIXER_X_SIZE:int = 5
FIXER_Y_SIZE:int = 6

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def erase_screen():
    if not DEBUG_MODE[0]:
        system("cls")


def size_screen(x:int=0, y:int=0, obj=...):
    if not (x == 0 or y==0):
        x_cols = obj.vec[0]+FIXER_X_SIZE
        y_lins = obj.vec[1]+FIXER_Y_SIZE
    else:
        x_cols = x+FIXER_X_SIZE
        y_lins = y+FIXER_Y_SIZE

    system(f"mode con:cols={x_cols} line={y_lins}")

def print_debug(*msg):
    logging.debug(msg)
