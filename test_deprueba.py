from Tarjeta import *


def Tarjeta():

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


def test_Recarga():

	azul = TarjetaComun()
	amarillo = TarjetaComun()

	naranja = TarjetaMedioBoleto()
	violeta = TarjetaMedioBoleto()

	cole1 = Colectivo("Semtur", 122, 1111)
	cole2 = Colectivo("Rosario", 'k', 7493)

	#Recargo las tarjetas, y devuelve el monto recargado
	assert azul.Recarga(3) == 3
	assert azul.Recarga(0) == 0
	assert amarillo.Recarga(196) == 230
	assert amarillo.Recarga(197) == 197
	assert naranja.Recarga(-3) == 0
	assert naranja.Recarga(5) == 5
	assert violeta.Recarga(368) == 460
	assert violeta.Recarga(-196) == 0


def test_getSaldo():

	azul = TarjetaComun()
	amarillo = TarjetaComun()

	naranja = TarjetaMedioBoleto()
	violeta = TarjetaMedioBoleto()

	cole1 = Colectivo("Semtur", 122, 1111)
	cole2 = Colectivo("Rosario", 'k', 7493)

	#saldo cuando recien se incia la trjeta
	assert azul.getSaldo() == 0
	assert naranja.getSaldo() == 0
	assert amarillo.getSaldo() == 0
	assert violeta.getSaldo() == 0

	#cargas de distintos valores para comprobar que se suman al valor anterior
	azul.Recarga(3)
	assert azul.getSaldo() == 3
	azul.Recarga(0)
	assert azul.getSaldo() == 3
	amarillo.Recarga(196)
	assert amarillo.getSaldo() == 230
	amarillo.Recarga(197)
	assert amarillo.getSaldo() == 427
	naranja.Recarga(-3)
	assert naranja.getSaldo() == 0
	naranja.Recarga(5)
	assert naranja.getSaldo() == 5
	violeta.Recarga(368)
	assert violeta.getSaldo() == 460
	violeta.Recarga(-196)
	assert violeta.getSaldo() == 460




def test_PagarBoleto():

	azul = TarjetaComun()
	amarillo = TarjetaComun()

	naranja = TarjetaMedioBoleto()
	violeta = TarjetaMedioBoleto()

	cole1 = Colectivo("Semtur", 122, 1111)
	cole2 = Colectivo("Rosario", 'k', 7493)
	cole3 = Colectivo("Mixta", 101, 0666)

	#Pagar un boleto cuando recien se incia la tarjeta
	assert azul.PagarBoleto(cole1) == False
	assert naranja.PagarBoleto(cole1) == False
	assert amarillo.PagarBoleto(cole1) == False
	assert violeta.PagarBoleto(cole1) == False

	#Pagar 2 boletos con $6 y sin transbordo
	azul.Recarga(6)
	assert azul.PagarBoleto(cole1) == True
	assert azul.PagarBoleto(cole1) == False

	#Pagar un viaje normal, despues un transbordo, y luego otro que contaria como transbordo si no hubiera un transbordo anterior
	azul.Recarga(9)
	assert azul.PagarBoleto(cole3) == True
	assert azul.PagarBoleto(cole1) == True
	assert azul.PagarBoleto(cole2) == False


	#Tomar dos colectivos iguales sin suficiente saldo, y luego un transbordo con saldo suficiente
	amarillo.Recarga(8)
	assert amarillo.PagarBoleto(cole1) == True
	assert amarillo.PagarBoleto(cole1) == False
	assert amarillo.PagarBoleto(cole2) == True

	#Pagar 4 boletos seguidos, sin importar el valor o el transbordo, teniendo saldo suficiente
	amarillo.Recarga(196)
	assert amarillo.PagarBoleto(cole1) == True
	assert amarillo.PagarBoleto(cole1) == True
	assert amarillo.PagarBoleto(cole2) == True
	assert amarillo.PagarBoleto(cole2) == True

	#Tomar dos colectivos iguales sin suficiente saldo, y luego un transbordo con saldo suficiente, pero con los precios de medio boleto
	naranja.Recarga(4)
	assert naranja.PagarBoleto(cole1) == True
	assert naranja.PagarBoleto(cole1) == False
	assert naranja.PagarBoleto(cole2) == True


	#Pagar el boleto con plata insuficiente (no con $0 de saldo)
	naranja.Recarga(0)
	assert naranja.PagarBoleto(cole1) == False


	#Dos medio boleto en el mismo colectivo
	violeta.Recarga(6)
	assert violeta.PagarBoleto(cole1) == True
	assert violeta.PagarBoleto(cole1) == True


	#4 viajes en el siguiente orden:
	#normal, transbordo, normal, transbordo, pero no puedo pagar el ultimo
	violeta.Recarga(7)
	assert violeta.PagarBoleto(cole1) == True
	assert violeta.PagarBoleto(cole2) == True
	assert violeta.PagarBoleto(cole2) == True
	assert violeta.PagarBoleto(cole1) == False

def test_Viajes():

	azul = TarjetaComun()
	amarillo = TarjetaComun()

	naranja = TarjetaMedioBoleto()
	violeta = TarjetaMedioBoleto()

	cole1 = Colectivo("Semtur", 122, 1111)
	cole2 = Colectivo("Rosario", 'k', 7493)
	cole3 = Colectivo("Mixta", 101, 0666)

	#Le doy carga suficiente a las tarjetas
	azul.Recarga(368)	
	amarillo.Recarga(368)	
	naranja.Recarga(368)	
	violeta.Recarga(368)

	#Hago 3 viajes con cada tarjeta, pero alternando entre transbordos o no transbordos
	#normal, normal, normal
	azul.PagarBoleto(cole1)	
	azul.PagarBoleto(cole1)	
	azul.PagarBoleto(cole1)

	#normal, normal, transbordo
	amarillo.PagarBoleto(cole1)	
	amarillo.PagarBoleto(cole1)	
	amarillo.PagarBoleto(cole2)

	#normal, transbordo, normal 
	naranja.PagarBoleto(cole1)	
	naranja.PagarBoleto(cole2)	
	naranja.PagarBoleto(cole3)	

test_PagarBoleto()