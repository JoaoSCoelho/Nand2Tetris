from typing import Literal
from .not_ import not_
from .and_ import and_
from ...test import RED, GREEN, RESET 

def or_(a: Literal[1, 0], b: Literal[1, 0]) -> Literal[1, 0]:
    """Truthy table:\\
    a | b | or(a, b)
    0 | 0 | 0 
    0 | 1 | 1
    1 | 0 | 1
    1 | 1 | 1
    """
    
    return not_(and_(not_(a), not_(b))) # ¬(¬a ∧ ¬b)

def __test__(shouldPrint: bool):
    try:
        assert or_(0, 0) == 0
        assert or_(0, 1) == 1
        assert or_(1, 0) == 1
        assert or_(1, 1) == 1
    
        if (shouldPrint):
            print(f'{GREEN}✓{RESET} Gate {GREEN}OR{RESET} successfully pass on test')
    except AssertionError as e:
        print(f'{RED}✕{RESET} Gate {RED}OR{RESET} fails {e}')    
        
if (__name__ == "__main__"):
    # Making local tests
    __test__(True)