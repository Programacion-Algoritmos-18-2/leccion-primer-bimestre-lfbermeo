package ejercicio_1py;

public class EmpleadoFijo extends Empleado {

    private double sueldo_fijo;
    private int descuento_seguro;

    public EmpleadoFijo(String n, String a, String c, double c_f, double sueldo_fijo, int descuento_seguro) {
        super(n, a, c, c_f);
        setSueldo_fijo(sueldo_fijo);
        setDescuento_seguro(descuento_seguro);

    }

    public void setSueldo_fijo(double s_f) {
        sueldo_fijo = s_f;
    }

    public double getSueldo_fijo() {
        return sueldo_fijo;
    }

    public void setDescuento_seguro(int d_s) {
        descuento_seguro = d_s;
    }

    public int getDescuento_seguro() {
        return descuento_seguro;
    }

    public double calcular_valor_sueldo_final() {
        double sueldo_fijo = (getSueldo_fijo() + getComision_fija()) - (getSueldo_fijo() * (getDescuento_seguro() / 100));
        return sueldo_fijo;
    }

    @Override
    public String toString() {

        String cadena = String.format("Sueldo fijo: %s\\n Descuento seguro: %s\\n Sueldo final: %s", super.toString(), getSueldo_fijo(), getDescuento_seguro(), calcular_valor_sueldo_final());
        return cadena;
    }

}
