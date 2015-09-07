
from datetime import datetime


class Tarjeta():
	def __init__(self):
		print	("No se pueden crear tarjetas sin un tipo")
		return False

	def getSaldo(self):
		return self._Saldo

	def Recarga(self, monto):
		self._Saldo+=monto
		if monto==196:
			self._Saldo+=34
		elif monto==368:
			self._Saldo+=92

	def setUltimoViaje(self, colectivo, hora, monto):
		self._UltimoViaje=Viaje(colectivo, hora, monto)

	def getViajesRealizados(self):
		return self._Viajes

	def AgregarViaje(self):
		# Podria llamar aca a setUltimoViaje
		self._Viajes+=self._UltimoViaje # Esto funciona?

	def EsTransbordo(self, hora, colectivo): # En vez de pasar colectivo, no tendria que pasar viaje?
		if(!isinstance(self._UltimoViaje, Viaje)):
			return False
		else:
			self._ultimaHora=self._UltimoViaje.getHora()
			self._HoraViaje=hora # Y esto de donde sale?
			if self._HoraViaje-self._ultimaHora <=3600 and self._UltimoViaje.getColectivo()!=colectivo:
				return True
			else:
				return False



class TarjetaComun(Tarjeta):

	def __init__(self):
		self.setSaldo()
		self.setViajes()

	def setSaldo(self):
		self._Saldo=0

	def setViajes(self):
		self._Viajes=0	

	def PagarBoleto(self, colectivo, hora):

		# transbordo=self.EsTransbordo(hora)

		if(!self.EsTransbordo(hora, colectivo)):
			if self.getSaldo()>=5.75
				self._Saldo=self._Saldo-5.75
				self.setUltimoViaje(colectivo, hora, 5.75)
				self.AgregarViaje(self._UltimoViaje) #
				return True

			else:
				return False

		else:
			if self.getSaldo()>=1.90
				self._Saldo-=1.90
				self.setUltimoViaje(colectivo, hora, 1.90)
				self.AgregarViaje(self._UltimoViaje)
				return True

			else:
				return False




class TarjetaMedioBoleto(Tarjeta):

	hora6=datetime.strptime("diadehoy 06:00", "%d/%m/%Y %H:%M")
	hora24=datetime.strptime("diadehoy 00:00", "%d/%m/%Y %H:%M")

	def __init__(self):
		self.setSaldo()
		self.setViajes()

	def setSaldo(self):
		self._Saldo=0

	def setViajes(self):
		self._Viajes=0		

	def PagarBoleto(self, colectivo, hora):
		if (!self.EsTransbordo(hora, colectivo)):
			if hora>=hora6 and hora<=hora24:
				if self.getSaldo()>=2.90:
					self._Saldo-=2.90
					self._UltimoViaje=Viaje(colectivo, hora, 2.90)
					self.AgregarViaje(self._UltimoViaje)
					return True
				else:
					return False
			else:
				if self.getSaldo()>=5.75
					self._Saldo=self._Saldo-5.75
					self.setUltimoViaje(colectivo, hora, 5.75)
					self.AgregarViaje(self._UltimoViaje) 
					return True
				else:
					return False
				
		else:
			if hora>=hora6 and hora<=hora24:
				if self.getSaldo()>=0.96:
					self._Saldo-=0.96
					self._UltimoViaje=Viaje(colectivo, hora, 0.96)
					self.AgregarViaje(self._UltimoViaje)
					return True
				else:
					return False
			else:
				if self.getSaldo()>=1.90
					self._Saldo-=1.90
					self.setUltimoViaje(colectivo, hora, 1.90)
					self.AgregarViaje(self._UltimoViaje)
					return True
				else:
					return False

			

class Colectivo:
	def __init__(self, empresa, linea, nint):
		self.setEmpresa(empresa)
		self.setLinea(linea)
		self.setNint(nint)		

	def setEmpresa(self, empresa):
		self._Empresa=empresa

	def getEmpresa(self):
		return self._Empresa

	def setLinea(self, linea):
		self._Linea=linea

	def getLinea(self):
		return self._Linea

	def setNint(self, nint):
		self._Nint=nint

	def getNint(self):
		return self._Nint


class Viaje:
"""			   			(colectivo, time, int)"""
	def __init__ (self, colectivo, hora, monto):
		self.setColectivo(colectivo)
		self.setHora(hora)
		self.setMonto(monto)
 	
	def setColectivo(self, colectivo):
		self._Colectivo=colectivo

	def getColectivo(self):
		return self._Colectivo

	def setHora(self, hora):
		self._Hora=hora

	def getHora(self):
		return self._Hora

	def setMonto(self, monto):
		self._Monto=monto

	def getMonto(self):
		return self._Monto
