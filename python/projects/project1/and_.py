from .not_ import not_
from ...nand import nand
from ...test import GREEN, RESET, RED
from typing import Literal

def and_(a: Literal[1, 0], b: Literal[1, 0]) -> Literal[1, 0]:
    """Truthy table:\\
    a | b | and(a, b)\\
    0 | 0 | 0\\
    0 | 1 | 0\\
    1 | 0 | 0\\
    1 | 1 | 1
    """
    
    return not_(nand(a, b)) # ¬¬(a ∧ b)

def __test__(shouldPrint: bool = False):
    try:
        assert and_(0, 0) == 0
        assert and_(0, 1) == 0
        assert and_(1, 0) == 0
        assert and_(1, 1) == 1
        
        if (shouldPrint):
            print(f'{GREEN}✓{RESET} Gate {GREEN}AND{RESET} successfully pass on test')
    except AssertionError as e:
        print(f'{RED}✕{RESET} Gate {RED}AND{RESET} fails {e}')    
        
if (__name__ == "__main__"):
    # Making local tests
    __test__(True)