from PyMQL5 import PyMQL5
mql5 = PyMQL5()

fechamento = mql5.iClose("PETR4", "M5", 0)

# Se o valor de retorno for None ocorreu um erro com a conexão com MetaTrader5
if fechamento != None:
	print("Ultimo preço de PETR4: ", fechamento)
else:
	print("Não a Conexão com MetaTrader5 verifique!")
