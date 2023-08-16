package Classes;
import java.util.List;
import java.util.ArrayList;

public class Node<E> {
    // -> Atributos
    protected E value;
    protected Node<E> left, right;
    private int pos = -1;    
    private boolean nullable;

    // -> Constructores
    public Node(){
        value = null;
        nullable = false;
    }
    public void setPos(int pos) {
        this.pos = pos;
    }
    public Node(E value)
    {
        this.value = value;
        nullable = false;
    }    

    public Node(E value, int pos){
        this.pos = pos;
        this.value = value;
        nullable = false;
    }

    public Node(E value, Node<E> left, Node<E> right){
        this.value = value;
        nullable = false;
        if(left != null) setLeft(left);
        if(right != null) setRight(right);
    }

    // -> Getters
    public E value()
    {
        return this.value;
    }

    public Node<E> left()
    {
        return left;
    }

    public Node<E> right(){
        return right;
    }

    public int getPos() {
        return pos;
    }

    public boolean getNullable(){
        return nullable;
    }

    // -> Setters
    public void setLeft(Node<E> newLeft)
    {
        left = newLeft;
    }

    public void setRight(Node<E> newRight){
        right = newRight;
    }

    public void setValue(E value){
        this.value = value;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }

    // -> Metodos    
    public String traverse(){
        String information = "";

        if (left != null) information += left.traverse();
        information += value.toString() + "\n";
        if (right != null) information +=  right.traverse();

        return information;
    }

    public boolean isNull(){
        return (value == null);
    }

    public boolean invalidPos(){
        return (pos < 0);
    }
}

