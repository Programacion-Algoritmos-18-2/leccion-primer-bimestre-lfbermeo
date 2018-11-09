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
		cadena = "Información de %s %s\n\t CÉDULA %s"% (self.obtener_nombre(),
														self.obtener_apellido(),
    													self.obtener_cedula())
		return cadena
#la clase empleado por hora hereda los atributos de la clase padre como lo es Empleado
class EmpleadoPorHoras(Empleado):

	def __init__(self):	
		#Con la palabra super, hago referencia a la clase padre que tome en cuenta en mi nueva clas EmpleadoPorHoras
		super(EmpleadoPorHoras,self).__init__()
		self.numero_horas=0
		self.valor_hora=0
	#Declaro mis funciones agregar y obtener para los nuevos atributos	
	def agregar_numero_horas(self,n_u):
		self.numero_horas=n_u

	def obtener_numero_horas(self):
		return self.numero_horas

	def agregar_valor_hora(self,v_h):
		self.valor_hora=v_h

	def obtener_valor_hora(self):
		return self.valor_hora
		#Para calcular el sueldo final tomo en cuenta mis funciones, las llamos y realizo las operaciones
	def calcular_valor_sueldo_final(self):
		sueldo_fijo = (self.obtener_numero_horas()*self.obtener_valor_hora()+self.obtener_comision_fija())
		return sueldo_fijo

	def presentar_datos(self):
		#Presento cada uno de los parametros de mi clase, agregandole super para que tome en cuenta mis atributos de la clase padre
		cadena = "%s\n Número horas: %s\n Valor hora: %s\n Sueldo final: %s"%(super(EmpleadoPorHoras,self).presentar_datos(),
																				self.obtener_numero_horas(),
																				self.obtener_valor_hora(),
																				self.calcular_valor_sueldo_final())
		#Retorno la cadena para qeu presenten los valores
		return cadena
class EmpleadoFijo(Empleado):

	def __init__(self):	
		#Con la palabra super, hago referencia a la clase padre que tome en cuenta en mi nueva clas EmpleadoFijo
		super(EmpleadoFijo,self).__init__()
		self.sueldo_fijo=0
		self.descuento_seguro=0
		#Declaro las funciones agregar y obtener de los nuevos atributos
	def agregar_sueldo_fijo(self,s_f):
		self.sueldo_fijo=s_f

	def obtener_sueldo_fijo(self):
		return self.sueldo_fijo

	def agregar_descuento_seguro(self,d_s):
		self.descuento_seguro=d_s

	def obtener_descuento_seguro(self):
		return self.descuento_seguro
		#Calculo el sueldo final descontando el seguro social
	def calcular_valor_sueldo_final(self):
		sueldo_fijo = (self.obtener_sueldo_fijo()+self.obtener_comision_fija())-(self.obtener_sueldo_fijo()*(self.obtener_descuento_seguro()/100))
		return sueldo_fijo
		#presento valores de los atributos de la clase padre, con los nuevos atributos
	def presentar_datos(self):
		cadena = "%s\n Sueldo Fijo: %s\n Descuento seguro: %s\n Sueldo final: %s"%(super(EmpleadoFijo,self).presentar_datos(),
																				self.obtener_sueldo_fijo(),
																				self.obtener_descuento_seguro(),
																				self.calcular_valor_sueldo_final())
		#Retorno los valores para presentar datos
		return cadena																																									

class EmpleadoPorSemana(Empleado):

	def __init__(self):
	#Con la palabra super, hago referencia a la clase padre que tome en cuenta en mi nueva clas EmpleadoPorSemana	
		super(EmpleadoPorSemana,self).__init__()
		self.numero_semanas=0
		self.valor_semanal=0
		#Agrego las funciones obtener y agregar de los nuevos atributos de la clase hijo
	def agregar_numero_semanas(self,n_s):
		self.numero_semanas= n_s

	def obtener_numero_semanas(self):
		return self.numero_semanas

	def agregar_valor_semanal(self,v_s):
		self.valor_semanal= v_s

	def obtener_valor_semanal(self):
		return self.valor_semanal
		#Calculo el sueldo final obteniendoles de las funciones obtener de los valores qeu requiero
	def calcular_valor_sueldo_final(self):
		sueldo_fijo=(self.obtener_numero_semanas()*self.obtener_valor_semanal()+self.obtener_comision_fija())
		return sueldo_fijo
		#Presento los datos tomando en cuenta los atributos de la clase padre y con los nuevos atributos de la clase hijo
	def presentar_datos(self):
		cadena = "%s\n Número semanas: %s\n Valor semanal: %s\n Sueldo final: %s"%(super(EmpleadoPorSemana,self).presentar_datos(),
																				self.obtener_numero_semanas(),
																				self.obtener_valor_semanal(),
																				self.calcular_valor_sueldo_final())	
		#Rertorno la cadena para presentar datos
		return cadena
