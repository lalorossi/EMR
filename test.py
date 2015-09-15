from EMR import *

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
	cole3 = Colectivo("Mixta", 101, 1111)

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

	############################################################################################
	#																						   #
	#   AHORA PROBAMOS CON DEFINIR UNA VARIABLE DE HORA PARA USAR EN LUGAR DE LA HORA ACTUAL   #
	#   		   PARA PODER USAR EL MEDIO BOLETO SIN CONSULTAR LA HORA ACTUAL	               #
	#																						   #
	############################################################################################

	horaMedio=datetime.today()
	horaMedio=horaMedio.replace(hour=07, minute=00, second=00, microsecond=00)
	
	#La tarjeta naranja se prueba dentro del horario de medio boleto
	naranja.Recarga(4)
	assert naranja.PagarBoleto(cole1, horaMedio) == True
	assert naranja.PagarBoleto(cole1, horaMedio) == False
	assert naranja.PagarBoleto(cole2, horaMedio) == True


	#Pagar el boleto con plata insuficiente (no con $0 de saldo)
	naranja.Recarga(0)
	assert naranja.PagarBoleto(cole1, horaMedio) == False


	horaNoMedio=datetime.today()
	horaNoMedio=horaNoMedio.replace(hour=03, minute=00, second=00, microsecond=00)

	#La tarjeta violeta se toma fuera de horario de medio boleto
	#Dos medio boleto en el mismo colectivo
	violeta.Recarga(6)
	assert violeta.PagarBoleto(cole1, horaNoMedio) == True
	assert violeta.PagarBoleto(cole1, horaNoMedio) == False


	#4 viajes en el siguiente orden:
	#normal, transbordo, normal, transbordo, pero no puedo pagar el ultimo
	violeta.Recarga(14)
	assert violeta.PagarBoleto(cole1, horaNoMedio) == True
	assert violeta.PagarBoleto(cole2, horaNoMedio) == True
	assert violeta.PagarBoleto(cole2, horaNoMedio) == True
	assert violeta.PagarBoleto(cole1, horaNoMedio) == False

################################################################################################
#Probamos el transbordo fallido, pero esta vez por la diferencia entre horas. Anteriormente solo se habia probado por tomarse dos veces el mismo colectivo. Para esto, creamos una nueva tarjeta

	rojo = TarjetaComun()

	#Le damos suficiente carga para un solo boleto, pero no el siguiente, a menos que sea tranbordo (como no lo es, se supone que no se deberia poder pagar)
	#Para probar con una diferencia de mas de una hora, se usan las horas dentro y fuera del horario de medio boleto
	rojo.Recarga(10)
	assert rojo.PagarBoleto(cole2, horaNoMedio) == True
	assert rojo.PagarBoleto(cole1, horaMedio) == False


def test_Viajes():

	azul = TarjetaComun()
	amarillo = TarjetaComun()

	naranja = TarjetaMedioBoleto()
	violeta = TarjetaMedioBoleto()

	cole1 = Colectivo("Semtur", 122, 1111)
	cole2 = Colectivo("Rosario", 'k', 7493)
	cole3 = Colectivo("Mixta", 101, 6666)

	#Le doy carga suficiente a las tarjetas. Hago las pruebas para una tarjeta de cada tipo
	azul.Recarga(368)	
	naranja.Recarga(368)	

	#Hago 9 viajes con cada tarjeta, pero alternando entre transbordos o no transbordos, para comprobar que los dos tipos de viaje se agregan a la lista de viajes realizados
	#normal, normal, normal
	azul.PagarBoleto(cole1)	
	azul.PagarBoleto(cole1)	
	azul.PagarBoleto(cole1)

	#normal, normal, transbordo
	azul.PagarBoleto(cole1)	
	azul.PagarBoleto(cole1)	
	azul.PagarBoleto(cole2)

	#normal, transbordo, normal 
	azul.PagarBoleto(cole1)	
	azul.PagarBoleto(cole2)	
	azul.PagarBoleto(cole3)

	#Los assert van a comprobar el colectivo y el tipo de viaje de cada viaje realizado
	#Primeros 3 viajes
	i=0
	assert azul.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert azul.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert azul.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert azul.getViajesRealizados()[i].getMonto() == 5.75

	i+=1
	assert azul.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert azul.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert azul.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert azul.getViajesRealizados()[i].getMonto() == 5.75

	i+=1
	assert azul.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert azul.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert azul.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert azul.getViajesRealizados()[i].getMonto() == 5.75

	#Siguientes 3 viajes
	i+=1
	assert azul.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert azul.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert azul.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert azul.getViajesRealizados()[i].getMonto() == 5.75

	i+=1
	assert azul.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert azul.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert azul.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert azul.getViajesRealizados()[i].getMonto() == 5.75

	i+=1
	assert azul.getViajesRealizados()[i].getColectivo().getEmpresa() == "Rosario"
	assert azul.getViajesRealizados()[i].getColectivo().getLinea() == 'k'
	assert azul.getViajesRealizados()[i].getColectivo().getNint() == 7493
	assert azul.getViajesRealizados()[i].getMonto() == 1.90

	#Ultimos 3 viajes
	i+=1
	assert azul.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert azul.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert azul.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert azul.getViajesRealizados()[i].getMonto() == 5.75

	i+=1
	assert azul.getViajesRealizados()[i].getColectivo().getEmpresa() == "Rosario"
	assert azul.getViajesRealizados()[i].getColectivo().getLinea() == 'k'
	assert azul.getViajesRealizados()[i].getColectivo().getNint() == 7493
	assert azul.getViajesRealizados()[i].getMonto() == 1.90

	i+=1
	assert azul.getViajesRealizados()[i].getColectivo().getEmpresa() == "Mixta"
	assert azul.getViajesRealizados()[i].getColectivo().getLinea() == 101
	assert azul.getViajesRealizados()[i].getColectivo().getNint() == 6666
	assert azul.getViajesRealizados()[i].getMonto() == 5.75



	#normal, normal, normal
	naranja.PagarBoleto(cole1)	
	naranja.PagarBoleto(cole1)	
	naranja.PagarBoleto(cole1)

	#normal, normal, transbordo
	naranja.PagarBoleto(cole1)	
	naranja.PagarBoleto(cole1)	
	naranja.PagarBoleto(cole2)

	#normal, transbordo, normal 
	naranja.PagarBoleto(cole1)	
	naranja.PagarBoleto(cole2)	
	naranja.PagarBoleto(cole3)


	#Los assert van a comprobar el colectivo y el tipo de viaje de cada viaje realizado
	#Primeros 3 viajes
	i=0
	assert naranja.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert naranja.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert naranja.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert naranja.getViajesRealizados()[i].getMonto() == 2.90

	i+=1
	assert naranja.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert naranja.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert naranja.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert naranja.getViajesRealizados()[i].getMonto() == 2.90

	i+=1
	assert naranja.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert naranja.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert naranja.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert naranja.getViajesRealizados()[i].getMonto() == 2.90

	#Siguientes 3 viajes
	i+=1
	assert naranja.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert naranja.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert naranja.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert naranja.getViajesRealizados()[i].getMonto() == 2.90

	i+=1
	assert naranja.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert naranja.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert naranja.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert naranja.getViajesRealizados()[i].getMonto() == 2.90

	i+=1
	assert naranja.getViajesRealizados()[i].getColectivo().getEmpresa() == "Rosario"
	assert naranja.getViajesRealizados()[i].getColectivo().getLinea() == 'k'
	assert naranja.getViajesRealizados()[i].getColectivo().getNint() == 7493
	assert naranja.getViajesRealizados()[i].getMonto() == 0.96

	#Ultimos 3 viajes
	i+=1
	assert naranja.getViajesRealizados()[i].getColectivo().getEmpresa() == "Semtur"
	assert naranja.getViajesRealizados()[i].getColectivo().getLinea() == 122
	assert naranja.getViajesRealizados()[i].getColectivo().getNint() == 1111
	assert naranja.getViajesRealizados()[i].getMonto() == 2.90

	i+=1
	assert naranja.getViajesRealizados()[i].getColectivo().getEmpresa() == "Rosario"
	assert naranja.getViajesRealizados()[i].getColectivo().getLinea() == 'k'
	assert naranja.getViajesRealizados()[i].getColectivo().getNint() == 7493
	assert naranja.getViajesRealizados()[i].getMonto() == 0.96

	i+=1
	assert naranja.getViajesRealizados()[i].getColectivo().getEmpresa() == "Mixta"
	assert naranja.getViajesRealizados()[i].getColectivo().getLinea() == 101
	assert naranja.getViajesRealizados()[i].getColectivo().getNint() == 6666
	assert naranja.getViajesRealizados()[i].getMonto() == 2.90
