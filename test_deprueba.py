from Tarjeta import *

azul = TarjetaComun()
amarillo = TarjetaComun()

naranja = TarjetaMedioBoleto()
violeta = TarjetaMedioBoleto()

cole1 = Colectivo("Semtur", 122, 1111)

cole2 = Colectivo("Rosario", 'k', 7493)


def test_Tarjeta():

	#Pruebo de pagar boletos sin recarga
	assert azul.PagarBoleto(cole1) == False
	assert amarillo.PagarBoleto(cole2) == False
	assert naranja.PagarBoleto(cole1) == False
	assert violeta.PagarBoleto(cole2) == False


	#Compruebo que no haya viajes realizados
	assert azul.getViajesRealizados() == []
	assert amarillo.getViajesRealizados() == []
	assert naranja.getViajesRealizados() == []
	assert violeta.getViajesRealizados() == []


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
	assert amarillo.PagarBoleto(cole2) == True
	assert naranja.PagarBoleto(cole1) == True
	assert violeta.PagarBoleto(cole1) == True


	assert len(azul.getViajesRealizados()) == 0
	assert len(amarillo.getViajesRealizados()) == 1
	assert len(naranja.getViajesRealizados()) == 1
	assert len(violeta.getViajesRealizados()) == 1

	assert amarillo.getViajesRealizados()[amarillo.getCantViajes()-1].getColectivo().getLinea() == 'k'
	assert naranja.getViajesRealizados()[naranja.getCantViajes()-1].getColectivo().getLinea() == 122
	assert violeta.getViajesRealizados()[violeta.getCantViajes()-1].getColectivo().getLinea() == 122



	#Compruebo las cargas de las tarjetas luego de pagar los boletos
	#En algunos casos, escribir un numero con decimal en lugar de la resta del saldo y el monto, da problemas de redondeo
	assert azul.getSaldo() == 3
	assert amarillo.getSaldo() == 224.25
	assert naranja.getSaldo() == 0.10
	assert violeta.getSaldo() == 457.10


	#Pruebo el transbordo con una tarjeta comun y otra de miedio boleto
	#Con las otras tarjetas, compruebo que se hayan quedado sin carga
	assert azul.PagarBoleto(cole2) == False 
	assert amarillo.PagarBoleto(cole1) == True #TRANSBORDO
	assert naranja.PagarBoleto(cole2) == False 
	assert violeta.PagarBoleto(cole2) == True #TRANSBORDO


	assert len(azul.getViajesRealizados()) == 0
	assert len(amarillo.getViajesRealizados()) == 2
	assert len(naranja.getViajesRealizados()) == 1
	assert len(violeta.getViajesRealizados()) == 2


	assert amarillo.getViajesRealizados()[amarillo.getCantViajes()-1].getColectivo().getLinea() == 122
	assert naranja.getViajesRealizados()[naranja.getCantViajes()-1].getColectivo().getLinea() == 122
	assert violeta.getViajesRealizados()[violeta.getCantViajes()-1].getColectivo().getLinea() == 'k'


	#Luego compruebo sus cargas para saber si funciona el transbordo
	assert azul.getSaldo() == 3
	assert amarillo.getSaldo() == 222.35
	assert naranja.getSaldo() == 0.10
	assert violeta.getSaldo() == 456.14


	#Ultima recarga, viaje y chequeo de saldo
	azul.Recarga(2.75)
	amarillo.Recarga(10)
	naranja.Recarga(0.10)
	violeta.Recarga(27)

	assert azul.getSaldo() == (5.75)
	assert amarillo.getSaldo() == (232.35)
	assert naranja.getSaldo() == (0.2)
	assert violeta.getSaldo() == (483.14)

	assert azul.PagarBoleto(cole1) == True
	assert amarillo.PagarBoleto(cole1) == True #No es transbordo, porque ya se uso antes
	assert naranja.PagarBoleto(cole1) == False
	assert violeta.PagarBoleto(cole2) == True


	assert len(azul.getViajesRealizados()) == 1
	assert len(amarillo.getViajesRealizados()) == 3
	assert len(naranja.getViajesRealizados()) == 1
	assert len(violeta.getViajesRealizados()) == 3

	assert azul.getViajesRealizados()[azul.getCantViajes()-1].getColectivo().getLinea() == 122
	assert amarillo.getViajesRealizados()[amarillo.getCantViajes()-1].getColectivo().getLinea() == 122
	assert naranja.getViajesRealizados()[naranja.getCantViajes()-1].getColectivo().getLinea() == 122
	assert violeta.getViajesRealizados()[violeta.getCantViajes()-1].getColectivo().getLinea() == 'k'


	assert azul.getSaldo() == 0
	assert amarillo.getSaldo() == (226.60)
	assert naranja.getSaldo() == (0.2)
	assert violeta.getSaldo() == (480.24)







#test_Tarjeta()