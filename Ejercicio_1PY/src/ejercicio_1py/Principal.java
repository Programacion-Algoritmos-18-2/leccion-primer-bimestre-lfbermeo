package ejercicio_1py;

import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {
        String nombre;
        double comision;
        Scanner entrada = new Scanner(System.in);

        Empleado e = new Empleado(" Luis ", " Benitez ", " 110000001 ", 0);
        System.out.println(e);
        
        System.out.println("Ingrese su nombre: ");
        nombre = entrada.nextLine();
        EmpleadoPorHoras e2 = new  EmpleadoPorHoras(nombre, " Andrade ", " 11000001 ", 0, 15, 20.2);
        System.out.println(e2);
        
        System.out.println("Ingrese la comision: ");
        comision = entrada.nextDouble();
        EmpleadoFijo e3 = new  EmpleadoFijo(" Ana ", " Díaz ", " 111000001 ", comision, 3002.0, 10);
        System.out.println(e3);
        
        
        EmpleadoPorSemana e4 = new  EmpleadoPorSemana(" Ana ", " Andrade ", " 11000001 ", 0, 20, 15);
        System.out.println(e4);

    }
}
