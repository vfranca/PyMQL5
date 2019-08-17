from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
high = mql5.iHigh(symbol, period, 0)
if high == None:
    print("Não a Conexão com MetaTrader5 verifique!")
    exit()
print("Máxima do %s de %s: %.2f" % (period, symbol, high))
