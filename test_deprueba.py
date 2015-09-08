from Tarjeta import *

azul = TarjetaComun()
amarillo = TarjetaComun()

naranja = TarjetaMedioBoleto()
violeta = TarjetaMedioBoleto()

cole1 = Colectivo("Semtur", 122, 1111)

cole2 = Colectivo("Rosario", 'k', 7493)
azul.Recarga(2)
amarillo.Recarga(196)
naranja.Recarga(0)
violeta.Recarga(368)

#def test_Recarga():

	#assert azul.getSaldo() == 20
	#assert amarillo.getSaldo() == 230
	#assert naranja.getSaldo() == 0
	#assert violeta.getSaldo() == 460



def test_Pagar():

	#Esto no se debe hacer, pero es para probar con saldo=0
	#azul._saldo=0
	#amarillo._saldo=0
	#naranja._saldo=0
	#violeta._saldo=0

	assert azul.PagarBoleto(cole1) == False
	assert amarillo.PagarBoleto(cole1) == True
	assert naranja.PagarBoleto(cole1) == False
	assert violeta.PagarBoleto(cole1) == True

	azul.Recarga(5)
	amarillo.Recarga(196)
	naranja.Recarga(2)
	violeta.Recarga(368)

	assert azul.PagarBoleto(cole1) == True
	assert amarillo.PagarBoleto(cole1) == True
	assert naranja.PagarBoleto(cole1) == False
	assert violeta.PagarBoleto(cole1) == True

test_Pagar()