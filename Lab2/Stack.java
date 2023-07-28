public class Stack {
    private char[] arrary = {};
    public char peek() {return this.arrary[arrary.length-1];}
    public int count(){if (isEmpty()){return 0;}return this.arrary.length;}
    public char pop() {
        if (isEmpty())
        {
            return Character.MIN_VALUE;
        }
        char value = this.arrary[this.arrary.length-1];
        char temp[] = new char[this.arrary.length-1];
        for (int i = 0; i < this.arrary.length-1; i++) {
            temp[i] = this.arrary[i];
        }
        this.arrary = temp;
        return value;
    }
    public void push(char newVal)
    {
        char[] temp = new char[this.arrary.length+1];
        for (int i = 0; i < this.arrary.length; i++) {
            temp[i] = this.arrary[i];
        }
        temp[temp.length-1] = newVal;
        this.arrary = temp;
    }
    public boolean isEmpty()
    {
        
        if (this.arrary.length==0)
        {
            return true;
        }
        return false;
    }
    public void print()
    {
        System.out.print("[");
        for (char c : arrary) {
            System.out.print(c);
        }
        System.out.print("]");
    }
    public char[] toCharArray()
    {
        return this.arrary;
    }
}
