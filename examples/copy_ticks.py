from PyMQL5 import PyMQL5


mql5 = PyMQL5()
ticks = mql5.CopyTicks("CCMU19", 0, 10)
if ticks == None:
    print("Não a Conexão com MetaTrader5 verifique!")
    exit()
for tick in ticks:
    #print(tick)
    print("Time: %s" % tick["TIME"])
    print("BID: %s" % tick["BID"])
    print("ASK: %s" % tick["ASK"])
    print("Último: %s" % tick["LAST"])
    print("Volume: %s" % tick["VOLUME"])
    print("TIME_MSC: %s" % tick["TIME_MSC"])
    print("Flags: %s" % tick["FLAGS"])
    print("Volume real: %s" % tick["VOLUME_REAL"])


