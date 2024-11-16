from os import walk
import importlib

# Códigos ANSI para cores
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# Run over all files recursively
if (__name__ == "__main__"): # to avoid running every time it is imported
    for dirpath, dirnames, filenames in walk('python'):
        """
        dirpath : str -> a string with the path of current directory, like "python/projects"
        dirnames : list[str] -> a list of all subdirectories
        filenames : list[str] -> a list of all files in current directory
        """
        for filename in filenames:
            if (filename[-3:] != '.py' or filename == '__init__.py' or filename == 'test.py'): continue

            try:
                import_path = dirpath.replace('\\', '.') + '.' + filename[:-3]
                module = importlib.import_module(import_path)
                
                try:
                    module.__test__(True)
                except Exception as e:
                    print(f'Erro {e} no arquivo {import_path}')
            except:
                pass
    
    
