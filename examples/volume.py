from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
volume = mql5.iVolume(symbol, period, 0)
if volume == None:
    print("Não a Conexão com MetaTrader5 verifique!")
    exit()
print("Volume do %s de %s: %i" % (period, symbol, volume))
