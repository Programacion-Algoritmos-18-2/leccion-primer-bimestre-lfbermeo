package ejercicio_1py;

public class EmpleadoPorHoras extends Empleado {

    private int numero_horas;
    private double valor_hora;

    public EmpleadoPorHoras(String n, String a, String c, double c_f, int numero_horas, double valor_hora) {
        super(n, a, c, c_f);
        setNumero_horas(numero_horas);
        setValor_hora(valor_hora);

    }

    public void setNumero_horas(int n_h) {
        numero_horas = n_h;
    }

    public int getNumero_horas() {
        return numero_horas;
    }

    public void setValor_hora(double v_h) {
        valor_hora = v_h;
    }

    public double getValor_hora() {
        return valor_hora;
    }

    public double calcular_valor_sueldo_final() {
        double sueldo_fijo = (getNumero_horas() + getComision_fija() * getValor_hora());
        return sueldo_fijo;
    }

    @Override
    public String toString() {

        String cadena = String.format("Numero de horas: %s\\n Valor de horas: %s\\n Sueldo final: %s", super.toString(), getNumero_horas(), getValor_hora(), calcular_valor_sueldo_final());
        return cadena;
    }

}
