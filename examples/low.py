from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
low = mql5.iLow(symbol, period, 0)
if low == None:
    print("Não a Conexão com MetaTrader5 verifique!")
    exit()
print("Mínima do %s de %s: %.2f" % (period, symbol, low))
