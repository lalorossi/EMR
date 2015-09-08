
from datetime import *
#AGREGAR VIAJE PLUS


class Tarjeta():
	def __init__(self):
		print	("No se pueden crear tarjetas sin un tipo")
		return False
		self._Viajes=[]

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

	def Formateo(self, colectivo, hora, monto):
		formato = "%a %d %b %Y %H:%M:%S"
		hora = hora.strftime(formato)
		self._UltimoViajeFormat=Viaje(colectivo, hora, monto)

	def AgregarViaje(self):
		self._Viajes.append(self._UltimoViajeFormat)
		self._CantViajes=1
		#Esta bandera se hace para ver si hay al menos un viaje realizado (y poder compararlo en EsTransbordo)
		#Anda

	def getViajesRealizados(self):
		return self._Viajes


	def EsTransbordo(self, hora, colectivo):
		if(self._CantViajes!=1):
			return False
		else:
			#Para hacerlo mas seguro, no confiamos en solo comparar con el numero de linea
			#Ya que podemos tomar un colectivo de ida, y luego la misma linea de vuelta
			#Tampoco comparamos solo el numero interno, porque distintas empresas pueden usar el mismo numero interno para distintos colectivos
			#Por lo tanto, comparamos la empresa, el numero interno y la linea, para estar seguros de que el colectivo no es el mismo
			if (hora-self._UltimoViaje.getHora() <= timedelta(hours=1) and self._UltimoViaje.getColectivo().getNint() != colectivo.getNint() and self._UltimoViaje.getColectivo().getLinea() != colectivo.getLinea() and self._UltimoViaje.getColectivo().getEmpresa() != colectivo.getEmpresa()):
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
		self._Viajes=[]
		self._CantViajes=0

	def PagarBoleto(self, colectivo):

		hora = datetime.today()

		if(self.EsTransbordo(hora, colectivo)==False):
			if (self.getSaldo() >= 5.75):
				self._Saldo=self._Saldo-5.75
				self.setUltimoViaje(colectivo, hora, 5.75)
				self.Formateo(colectivo, hora, 5.75)
				self.AgregarViaje() 
				return True

			else:
				return False

		else:
			if self.getSaldo()>=1.90:
				self._Saldo-=1.90
				self.setUltimoViaje(colectivo, hora, 1.90)
				self.Formateo(colectivo, hora, 1.90)
				self.AgregarViaje()
				return True

			else:
				return False




class TarjetaMedioBoleto(Tarjeta):

	def __init__(self):
		self._Hora6=datetime.today()
		self._Hora6=self._Hora6.replace(hour=06, minute=00, second=00, microsecond=00)
		#print self._Hora6
		self._Hora24=datetime.today()
		self._Hora24=self._Hora24.replace(hour=23, minute=59, second=59, microsecond=9999)
		self.setSaldo()
		self.setViajes()

	def setSaldo(self):
		self._Saldo=0

	def setViajes(self):
		self._Viajes=[]
		self._CantViajes=0

	def PagarBoleto(self, colectivo):

		self._hora = datetime.today()
		
		if (self.EsTransbordo(self._hora, colectivo)==False):
			if self._hora >= self._Hora6 and self._hora <= self._Hora24:
				if self.getSaldo()>=2.90:
					self._Saldo-=2.90
					self._UltimoViaje=Viaje(colectivo, self._hora, 2.90)
					self.Formateo(colectivo, self._hora, 2.90)
					self.AgregarViaje()
					return True
				else:
					return False
			else:
				if self.getSaldo()>=5.75:
					self._Saldo=self._Saldo-5.75
					self.setUltimoViaje(colectivo, self._hora, 5.75)
					self.Formateo(colectivo, self._hora, 5.75)
					self.AgregarViaje() 
					return True
				else:
					return False
				
		else:
			if self._hora>=self._Hora6 and self._hora<=self._Hora24:
				if self.getSaldo()>=0.96:
					self._Saldo-=0.96
					self._UltimoViaje=Viaje(colectivo, self._hora, 0.96)
					self.Formateo(colectivo, self._hora, 0.96)
					self.AgregarViaje()
					return True
				else:
					return False
			else:
				if self.getSaldo()>=1.90:
					self._Saldo-=1.90
					self.setUltimoViaje(colectivo, self._hora, 1.90)
					self.Formateo(colectivo, self._hora, 1.90)
					self.AgregarViaje()
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
	#		   			(colectivo, time, int)
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




