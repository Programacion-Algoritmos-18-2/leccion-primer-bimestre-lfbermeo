class Empleado (object):
	def __init__(self):
		self.nombre=""
		self.apellido=""
		self.cedula=""
		self.comision_fija=0

	def agregar_nombre(self, n):
		self.nombre= n

	def obtener_nombre(self):
		return self.nombre

	def agregar_apellido(self, a):
		self.apellido= a

	def obtener_apellido(self):
		return self.apellido

	def agregar_cedula(self, c):
		self.cedula= c

	def obtener_cedula(self):
		return self.cedula

	def agregar_comision_fija(self, comision):
		self.comision_fija= comision

	def obtener_comision_fija(self):
		return self.comision_fija

	def presentar_datos(self):
		cadena = "Información de %s %s\n\t cedula %s"% (self.obtener_nombre(),self.obtener_apellido(),
    													self.obtener_cedula())
		return cadena
