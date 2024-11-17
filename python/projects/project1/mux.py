from typing import Literal
from ...test import RED, GREEN, RESET
from ...nand import nand
from .not_ import not_  

def mux(a: Literal[1, 0], b: Literal[1, 0], sel: Literal[1, 0]) -> Literal[1, 0]:
    """Truthy table:\\
    a | b | sel | mux(a, b)\\
    0 | 0 | 0   | 0\\
    0 | 1 | 0   | 0\\
    1 | 0 | 0   | 1\\
    1 | 1 | 0   | 1\\
    0 | 0 | 1   | 0\\
    0 | 1 | 1   | 1\\
    1 | 0 | 1   | 0\\
    1 | 1 | 1   | 1
    """
    
    return nand(nand(a, not_(sel)), nand(b, sel)) # (a ↑ ¬sel) ↑ (b ↑ sel)

def __test__(shouldPrint: bool = False):
    try:
        assert mux(0, 0, 0) == 0
        assert mux(0, 1, 0) == 0
        assert mux(1, 0, 0) == 1
        assert mux(1, 1, 0) == 1
        assert mux(0, 0, 1) == 0
        assert mux(0, 1, 1) == 1
        assert mux(1, 0, 1) == 0
        assert mux(1, 1, 1) == 1
    
        if (shouldPrint):
            print(f'{GREEN}✓{RESET} Gate {GREEN}MUX{RESET} successfully pass on test')
    except AssertionError as e:
        print(f'{RED}✕{RESET} Gate {RED}MUX{RESET} fails {e}')    
        


if (__name__ == "__main__"):
    # Making local tests
    __test__(True)