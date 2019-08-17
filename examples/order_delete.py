from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
op = mql5.OrderDelete(125163)
if op:
    print("A órdem 125163 foi cancelada")
else:
    print("Ocorreu um erro!")
