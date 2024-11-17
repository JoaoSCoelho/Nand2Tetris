from typing import Literal
from .test import GREEN, RESET, RED

def nand(a: Literal[0, 1], b: Literal[0, 1]) -> Literal[0, 1]:
    """
    The basis of all logic gates.
    The objective is to construct everything from this function (gate).
    His function is to return the NOT of the AND of the inputs.
    Thuthy table:\\
    a | b | nand(a, b)\\
    0 | 0 | 1\\
    0 | 1 | 1\\
    1 | 0 | 1\\
    1 | 1 | 0 
    """   
    return not (a and b) # ¬(a ∧ b)

def __test__(shouldPrint: bool):
    """
    Run local tests on NAND gate.
    
    Parameters:
    shouldPrint (bool): If True, print the result.
    
    Returns:
    None
    """
    
    try:
        assert nand(0, 0) == 1 # Throws a AssertionError if the test fails
        assert nand(0, 1) == 1
        assert nand(1, 0) == 1
        assert nand(1, 1) == 0
        
        if (shouldPrint): 
            print(f'{GREEN}✓{RESET} Gate {GREEN}NAND{RESET} successfully pass on test')
    except AssertionError as e:
        print(f'{RED}✕{RESET} Gate {RED}NAND{RESET} fails {e}') 

if (__name__ == "__main__"):
    # Making local tests
    __test__(True)

