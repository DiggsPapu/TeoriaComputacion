package Ejercicio3.Classes;
public class token {
    private int precedence;
    private String token;
    public token(String value)
    {
        this.token = value;
        switch (value)
        {
            case "(":
            precedence = 0;
            break;
            case ")":
            precedence = 4;
            break;
            case "*":
            precedence = 3;
            break;
            case ".":
            precedence = 2;
            break;
            case "|":
            precedence = 1;
            break;
            default:
            precedence = -2;
            break;
        }
    }
    public String getToken() {
        return token;
    }
    public int getPrecedence() {
        return precedence;
    }
}
