from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
rates = mql5.CopyRates(symbol, period, 0, 5)
if rates == None:
    print("Não a Conexão com MetaTrader5 verifique!")
    exit()
print("Hora Abr Max Min Fch Neg Spread Financ")
for r in rates:
    print("%s %.2f %.2f %.2f %.2f %i %i %i" % (r["TIME"], r["OPEN"], r["HIGH"], r["LOW"], r["CLOSE"], r["TICK_VOLUME"], r["SPREAD"], r["REAL_VOLUME"]))


