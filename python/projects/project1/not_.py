from ...nand import nand
from typing import Literal
from ...test import GREEN, RESET, RED

def not_(a: Literal[0, 1]) -> Literal[0, 1]:
    """
    This gate inverts the input.
    If the input is 1, the output is 0.
    If the input is 0, the output is 1.
    Truthy table:\\
    a | not(a)\\
    0 | 1\\
    1 | 0
    """
    return nand(a, a) # ¬(a ∧ a)

def __test__(shouldPrint: bool = False):
    try:
        assert not_(0) == 1
        assert not_(1) == 0
        
        if (shouldPrint): 
            print(f'{GREEN}✓{RESET} Gate {GREEN}NOT{RESET} successfully pass on test')
    except AssertionError as e:
        print(f'{RED}✕{RESET} Gate {RED}NOT{RESET} fails {e}') 

if (__name__ == "__main__"):
    # Making local tests
    __test__(True)
