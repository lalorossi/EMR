class Tarjeta():
	def __init__(self, tipo):
		#NO SE PUEDEN CREAR TARJETAS SIN TIPO

	def Saldo(self):
		return self._Saldo

	def Recarga(self, monto):
		self._Saldo+=monto
		if monto==196:
			self._Saldo+=34
		elif monto==368:
			self._Saldo+=92


class TarjetaComun(Tarjeta):

	def __init__(self):
		self._Saldo=0
		self._Viajes=0	

	def PagarBoleto(self, colectivo, hora):

		#LA HORA SE PASA COMO DATO. HAY QUE BUSCAR UN FORMATO QUE ME PERMITA USARLA COMO QUIERO

		#SI NO ES DE TRANSORDO (FIJARSE HORA DE ULTIMO VIAJE)
			if self._Saldo>=5.75
				self._Saldo=self._Saldo-5.75
				#GUARDAR ULTIMO VIAJE
				return True

			else:
				return False

		#SI ES DE TRANSBORDO
			if self._Saldo>=1.90
				self._Saldo-=1.90
				#self._UltimoViaje....
				return True

			else:
				return False




class TarjetaMedioBoleto(Tarjeta):

	def __init__(self):
		self._Saldo=0
		self._Viajes=0

	def PagarBoleto(self, colectivo, hora):
		#SI NO ES DE TRANSORDO

			#if hora>=6am and hora<=24:
				if self._Saldo>=1.90:
					self._Saldo-=1.90
					#self._UltimoViaje......
					return True

				else:
					return False

		#SI ES DE TRANSBORDO
			
			#if hora>=6am and hora<=24:
				if self._Saldo>=0.96:
					self._Saldo-=0.96
					#GUARDAR ULTIMO VIAJE
					return True

				else:
					return False
			

#CLASS COLECTIVO

#CLASS VIAJE
 colectivo
 hora
 es de transbordo?
 





		
