from os import walk
from importlib import import_module
from sys import argv
from time import time
from random import randint
from .test import RESET, BLUE
from inspect import signature

if (__name__ == "__main__"):
    # Run over all files recursively
    for dirpath, dirnames, filenames in walk('python'):
        for filename in filenames:
            if (
                filename[-3:] != '.py' or
                filename == '__init__.py' or
                filename == 'test.py' or
                filename == 'test_runtime.py'
            ):
                continue

            try:
                import_path = dirpath.replace('\\', '.').replace('/', '.') + '.' + filename[:-3]
                module = import_module(import_path)
                
                try:
                    avarage_time = 0
                    
                    # Take the number of rounds of the command line 
                    # "python -m python.test_runtime [rounds]"
                    rounds = argv[1] if len(argv) > 1 else 1000
                    
                    gate_name_upper = filename[:-4].upper() if filename[:-3].endswith('_') else filename[:-3].upper()
                    gate_function = getattr(module, filename[:-3])
                    num_of_parameters = len(signature(gate_function).parameters)
                    
                    for i in range(rounds):
                        parameters = [randint(0, 1) for i in range(num_of_parameters)]
                        
                        start = time()  
                        gate_function(*parameters)
                        end = time()
                        
                        avarage_time += (end - start)
                    
                    avarage_time /= rounds
                    
                    print(f'{BLUE}◷{RESET} Gate {BLUE}{gate_name_upper}{RESET} took {BLUE}{(avarage_time * 1000):.3f}{RESET} ms on average to run with {BLUE}{rounds}{RESET} rounds')
                    
                except Exception as e:
                    print(f'Erro {e} no arquivo {import_path}')
            except:
                pass                
                
