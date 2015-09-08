from Tarjeta import *

azul = TarjetaComun()
amarillo = TarjetaComun()

naranja = TarjetaMedioBoleto
violeta = TarjetaMedioBoleto()

cole1 = Colectivo("Semtur", 122, 1111)

cole2 = Colectivo("Rosario", 'k', 7493)

def Test_Recarga():
	 azul.Recarga(20)
	 amarillo.Recarga(196)
	 naranja.Recarga(0)
	 violeta.Recarga(368)

	assert azul.getSaldo() == 20
	assert amarillo.getSaldo() == 230
	assert naranja.getSaldo() == 0
	assert violeta.getSaldo() == 460



