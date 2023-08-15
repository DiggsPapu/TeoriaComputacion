package Classes;
import java.util.List;
import java.util.ArrayList;

public class Node<E> {
    // -> Atributos
    protected E value;
    protected Node<E> left, right;
    private int pos = -1;    
    private boolean nullable;
    private List<Integer> firstpos, lastpos;

    // -> Constructores
    public Node(){
        value = null;
        nullable = false;
        firstpos = new ArrayList<>();
        lastpos = new ArrayList<>();
    }
    public void setPos(int pos) {
        this.pos = pos;
    }
    public Node(E value)
    {
        this.value = value;
        nullable = false;
        firstpos = new ArrayList<>();
        lastpos = new ArrayList<>();
    }    

    public Node(E value, int pos){
        this.pos = pos;
        this.value = value;
        nullable = false;
        firstpos = new ArrayList<>();
        lastpos = new ArrayList<>();
    }

    public Node(E value, Node<E> left, Node<E> right){
        this.value = value;
        nullable = false;
        if(left != null) setLeft(left);
        if(right != null) setRight(right);
        firstpos = new ArrayList<>();
        lastpos = new ArrayList<>();
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

    public List<Integer> getFirstPoses() {
        return firstpos;
    }

    public List<Integer> getLastPoses() {
        return lastpos;
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
    public void addFirstPos(int number){
        if(!firstpos.contains(number)) firstpos.add(number);
    }

    public void addLastPos(int number){
        if(!lastpos.contains(number)) lastpos.add(number);
    }
    
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

