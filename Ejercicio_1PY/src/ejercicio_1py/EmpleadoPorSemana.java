package ejercicio_1py;

public class EmpleadoPorSemana extends Empleado {

    private int numero_semana;
    private double valor_semana;

    public EmpleadoPorSemana(String n, String a, String c, double c_f, int numero_semana, double valor_semana) {
        super(n, a, c, c_f);
        setNumero_semana(numero_semana);
        setValor_semana(valor_semana);

    }

    public void setNumero_semana(int n_s) {
        numero_semana = n_s;
    }

    public int getNumero_semana() {
        return numero_semana;
    }

    public void setValor_semana(double v_s) {
        valor_semana = v_s;
    }

    public double getValor_semana() {
        return valor_semana;
    }

    public double calcular_valor_sueldo_final() {
        double sueldo_fijo = (getNumero_semana() + getComision_fija() * getValor_semana());
        return sueldo_fijo;
    }

    @Override
    public String toString() {

        String cadena = String.format("Numero semana: %s\\n Valor : %s\\n Sueldo final: %s", super.toString(), getNumero_semana(), getValor_semana(), calcular_valor_sueldo_final());
        return cadena;
    }
}
