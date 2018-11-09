package ejercicio_1py;

public class Empleado {

    private String nombre;
    private String apellido;
    private String cedula;
    private double comision_fija;

    public Empleado(String n, String a, String c, double c_f) {
        setNombre(n);
        setApellido(a);
        setCedula(c);
        setComision_fija(c_f);
    }

    public void setNombre(String n) {
        nombre = n;
    }

    public String getNombre() {
        return nombre;
    }

    public void setApellido(String a) {
        apellido = a;
    }

    public String getApellido() {
        return apellido;
    }

    public void setCedula(String c) {
        cedula = c;
    }

    public String getCedula() {
        return cedula;
    }

    public void setComision_fija(double c_f) {
        comision_fija = c_f;
    }

    public double getComision_fija() {
        return comision_fija;
    }

    @Override
    public String toString() {

        String cadena = String.format("Información de %s %s \n\t CÉDULA %s", super.toString(), getNombre(), getApellido(), getCedula());
        return cadena;
    }
}
