from PyMQL5 import PyMQL5
from conf import *


mql5 = PyMQL5()
ticks = mql5.CopyTicks(symbol, 0, 5)
if ticks == None:
    print("Não a Conexão com MetaTrader5 verifique!")
    exit()
print("Hora BID ASK Último Volume Flags Time_MSC Volume_Real")
for t in ticks:
    print("%s %.2f %.2f %.2f %.1f %i %i %.1f" % (t["TIME"], t["BID"], t["ASK"], t["LAST"], t["VOLUME"], t["TIME_MSC"], t["FLAGS"], t["VOLUME_REAL"]))


