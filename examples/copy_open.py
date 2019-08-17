from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
prices = mql5.CopyOpen(symbol, period, 0, 5)
if prices == None:
    print("Não a Conexão com MetaTrader5 verifique!")
    exit()
for open in prices:
    print(open)


