import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Stack;

public class BalanceoExpresion {
    public static void main(String[] args) {
        // Ruta del archivo que contiene las expresiones a verificar
        String archivo = "C:\\Users\\s5349\\Documents\\Universidad\\Tareas_Universidad\\Semestre_6\\TC\\Lab2\\src\\data.txt";
        try {
            // Crear un BufferedReader para leer el archivo
            BufferedReader lector = new BufferedReader(new FileReader(archivo));
            String linea;
            int numeroLinea = 1;
            // Leer cada línea del archivo que contiene una expresión
            while ((linea = lector.readLine()) != null) {
                // Verificar si la expresión está balanceada
                boolean estaBalanceada = estaBalanceada(linea);
                System.out.println("Expresión " + numeroLinea + ": " + linea);
                // Mostrar si la expresión está balanceada o no
                if (estaBalanceada) {
                    System.out.println("Balanceada: Sí");
                } else {
                    System.out.println("Balanceada: No");
                }
                System.out.println();
                numeroLinea++;
            }
            lector.close();
        } catch (IOException e) {
            // Mostrar mensaje de error si hay problemas al leer el archivo
            System.err.println("Error al leer el archivo: " + e.getMessage());
        }
    }

    // Método para verificar si una expresión está balanceada
    public static boolean estaBalanceada(String expresion) {
        Stack<Character> pila = new Stack<>();
        // Símbolos de apertura
        String caracteresAbiertos = "([{";
        // Símbolos de cierre
        String caracteresCerrados = ")]}";

        // Recorrer cada carácter de la expresión
        for (int i = 0; i < expresion.length(); i++) {
            char caracter = expresion.charAt(i);
            // Si el carácter es un símbolo de apertura, agregarlo a la pila
            if (caracteresAbiertos.indexOf(caracter) != -1) {
                pila.push(caracter);
                // Mostrar el contenido de la pila en este paso
                System.out.println("Pila: " + pila.toString());
            } else if (caracteresCerrados.indexOf(caracter) != -1) {
                // Si el carácter es un símbolo de cierre
                if (pila.isEmpty()) {
                    // Si la pila está vacía y hay un símbolo de cierre, la expresión no está balanceada
                    // Mostrar el contenido de la pila en este paso
                    System.out.println("Pila: " + pila.toString());
                    return false;
                }
                // Si hay un símbolo de apertura correspondiente en la cima de la pila, retirarlo de la pila
                char ultimoCaracter = pila.pop();
                // Mostrar el contenido de la pila en este paso
                System.out.println("Pila: " + pila.toString());
                if (caracteresAbiertos.indexOf(ultimoCaracter) != caracteresCerrados.indexOf(caracter)) {
                    // Si el símbolo de cierre no coincide con el último símbolo de apertura, la expresión no está balanceada
                    return false;
                }
            }
        }

        // Si la pila está vacía al final, la expresión está balanceada
        return pila.isEmpty();
    }
}
