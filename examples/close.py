from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
close = mql5.iClose(symbol, period, 0)
if close == None:
    print("Não a Conexão com MetaTrader5 verifique!")
    exit()
print("Fechamento do %s de %s: %.2f" % (period, symbol, close))
