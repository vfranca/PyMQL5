from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
time = mql5.iTime(symbol, period, 0)
if time == None:
    print("Não a Conexão com MetaTrader5 verifique!")
    exit()
print("Data e hora do %s de %s: %s" % (period, symbol, time))
