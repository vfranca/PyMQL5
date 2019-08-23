from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
op = mql5.PositionCloseSymbol(symbol)
if op:
    print("A posição em %s foi cancelada com sucesso!" % symbol)
else:
    print("Ocorreu um erro!")
