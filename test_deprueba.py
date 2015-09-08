from Tarjeta import *

azul = TarjetaComun()
amarillo = TarjetaComun()

naranja = TarjetaMedioBoleto()
violeta = TarjetaMedioBoleto()

cole1 = Colectivo("Semtur", 122, 1111)

cole2 = Colectivo("Rosario", 'k', 7493)


def test_Recarga():

	#Pruebo de pagar boletos sin recarga
	assert azul.PagarBoleto(cole1) == False
	assert amarillo.PagarBoleto(cole2) == False
	assert naranja.PagarBoleto(cole1) == False
	assert violeta.PagarBoleto(cole2) == False

	#Recargo las tarjetas
	azul.Recarga(3)
	amarillo.Recarga(196)
	naranja.Recarga(3)
	violeta.Recarga(368)

	#Compruebo si estan cargadas
	assert azul.getSaldo() == 3
	assert amarillo.getSaldo() == 230
	assert naranja.getSaldo() == 3
	assert violeta.getSaldo() == 460


	#Pruebo de pagar boletos con la carga hecha
	assert azul.PagarBoleto(cole1) == False
	assert amarillo.PagarBoleto(cole1) == True
	assert naranja.PagarBoleto(cole1) == True
	assert violeta.PagarBoleto(cole1) == True

	#Compruebo las cargas de las tarjetas luego de pagar los boletos
	assert azul.getSaldo() == 3
	assert amarillo.getSaldo() == (230 - 5.75)
	assert naranja.getSaldo() == (3 - 2.90)
	assert violeta.getSaldo() == (460 - 2.90)

	#Pruebo el transbordo con una tarjeta comun y otra de miedio boleto
	amarillo.PagarBoleto(cole1)
	violeta.PagarBoleto(cole1)

	#Luego compruebo sus cargas para saber si funciona el transbordo
	assert amarillo.getSaldo() == (230 - 5.75 - 1.90)
	assert violeta.getSaldo() == (457.10 - 0.96)






#test_Recarga()