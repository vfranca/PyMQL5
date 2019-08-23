from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
op = mql5.PositionCloseParcial(123456, 2)
if op:
    print("A posição 123456 fechou 2 volumes com sucesso!")
else:
    print("Ocorreu um erro!")
