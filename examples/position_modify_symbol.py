from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
op = mql5.PositionModifySymbol(symbol, 104500, 103600)
if op:
    print("A posição em %s foi alterada com sucesso!" % symbol)
else:
    print("Ocorreu um erro!")
