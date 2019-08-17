from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
open = mql5.iOpen(symbol, period, 0)
if open == None:
    print("Não a Conexão com MetaTrader5 verifique!")
    exit()
print("Abertura do %s de %s: %.2f" % (period, symbol, open))
