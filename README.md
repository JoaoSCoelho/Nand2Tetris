# Nand2Tetris

# Python gates

The objective is to replicate the logic gates in python.

The basis of all logic gates is the [`nand`](python/nand.py) function, located on the root of python directory.

Every logic gate need to have a short description inside the function (documentation) and a local test on the bottom of the file that is a function called `__test__(shouldPrint: bool): -> None`. See the [`nand.py`](python/nand.py) file for an example.

To run the tests, in the root directory run the command:
```bash
$ python -m python.test
```
*OBS: Is necessary to have python installed on your machine.*