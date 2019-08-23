from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
op = mql5.CancelAllPosition()
if op:
    print("Todas as Posições foram canceladas")
else:
    print("Ocorreu um erro!")
