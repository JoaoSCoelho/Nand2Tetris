from typing import Literal
from .not_ import not_
from ...test import RED, GREEN, RESET
from ...nand import nand

def xor(a: Literal[1, 0], b: Literal[1, 0]) -> Literal[1, 0]:
    """Truthy table:\\
    a | b | xor(a, b)
    0 | 0 | 0 
    0 | 1 | 1
    1 | 0 | 1
    1 | 1 | 0
    """
    
    return nand(nand(a, not_(b)), nand(not_(a), b)) # ¬(¬(a ∧ ¬b) ∧ ¬(¬a ∧ b))

def __test__(shouldPrint: bool = False):
    try:
        assert xor(0, 0) == 0
        assert xor(0, 1) == 1
        assert xor(1, 0) == 1
        assert xor(1, 1) == 0
    
        if (shouldPrint):
            print(f'{GREEN}✓{RESET} Gate {GREEN}XOR{RESET} successfully pass on test')
    except AssertionError as e:
        print(f'{RED}✕{RESET} Gate {RED}XOR{RESET} fails {e}')    
        


if (__name__ == "__main__"):
    # Making local tests
    __test__(True)