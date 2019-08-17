from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
op = mql5.CancelAllOrder()
if op:
    print("Todas as órdens pendentes foram canceladas")
else:
    print("Ocorreu um erro!")
