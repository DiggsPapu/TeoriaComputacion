package Classes;
import java.io.FileWriter;

public class TokenStack {
    private token[] arrary = {};
    public token peek() {return this.arrary[arrary.length-1];}
    public int count(){if (isEmpty()){return 0;}return this.arrary.length;}
    public token pop() {
        if (isEmpty())
        {
            return null;
        }
        token value = this.arrary[this.arrary.length-1];
        token temp[] = new token[this.arrary.length-1];
        for (int i = 0; i < this.arrary.length-1; i++) {
            temp[i] = this.arrary[i];
        }
        this.arrary = temp;
        return value;
    }
    public void push(token newVal)
    {
        token[] temp = new token[this.arrary.length+1];
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
        for (token c : arrary) {
            System.out.print(c.getToken());
        }
        System.out.print("]");
    }
    public void writeStack(FileWriter myWriter)
    {
        try {
            myWriter.append("[");
            for (token c : arrary) {
                myWriter.append(c.getToken());
            }
            myWriter.append("]");
        } catch (Exception e) {
            // TODO: handle exception
        }
    }
    public token[] totokenArray()
    {
        return this.arrary;
    }
    public token getToken(int index)
    {
        return this.arrary[index];
    }
}
