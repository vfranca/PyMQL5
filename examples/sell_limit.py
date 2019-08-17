from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
op = mql5.SellLimit(symbol, 100, 29.90, 30.50, 21.80, "Comentário")
if op == -1:
    print("Ocorreu um erro!")
    exit()
print("Órdem %i" % op)
