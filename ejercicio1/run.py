#Incorporó cada una de las clases
from mipaquete.modelo import *
#Creó el objeto e de la clase padre Empleado para agregarle los valores necesarios tomando en cuenta las funciones
e = Empleado()
e.agregar_nombre("Luis")
e.agregar_apellido("Benitez")
e.agregar_cedula("110001")
#Imprimo el objeto e, tomando en cuenta la función presentar datos
print(e.presentar_datos())
#Creó el segundo método e1 que hace referencia a la segunda clase EmpladoPorHoras, agregandole los valores y el nombre pidiendoles por teclado
e1 = EmpleadoPorHoras()
nombre = input("Ingresar su nombre: ")
e1.agregar_nombre(nombre)
e1.agregar_apellido("Andrade")
e1.agregar_cedula("112233")
e1.agregar_valor_hora(20.2)
e1.agregar_numero_horas(15)
print(e1.presentar_datos())
#Creó el tercer objeto que hace referencia a la clase hijo EmpleadoFijo
e2 = EmpleadoFijo()
#Donde con la función agregar les doy sus valores respectivos 
e2.agregar_sueldo_fijo(300.2)
e2.descuento_seguro=10
#pidó por teclado la comisón donde el valor que se ingresa será con decimales o float
comision = input("Ingrese comision\n")
comision = float(comision)
e2.agregar_comision_fija(comision)
e2.agregar_nombre("Ana")
e2.agregar_apellido("Diaz")
e2.agregar_cedula("113322")
#Imprimo los valores
print(e2.presentar_datos())




    
