from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
op = mql5.Buy(symbol, 100, 22.10, 21.50, 28.80, "Comentário")
if op == -1:
    print("Ocorreu um erro!")
    exit()
print("Órdem %i" % op)
