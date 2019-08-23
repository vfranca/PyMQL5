from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
op = mql5.PositionCloseTicket(123456)
if op:
    print("A posição 123456 foi cancelada com sucesso!")
else:
    print("Ocorreu um erro!")
