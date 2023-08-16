package Classes;
import java.util.ArrayList;
public class GraphNode<E> {
    // This gives the Sn value
    protected E value;
    // This ArrayList stores the graph node index in the graph and the transition to take to there (Integer, String)
    protected ArrayList<TwoValues<Integer,String>> values = new ArrayList<>();

    public GraphNode(E value, ArrayList<TwoValues<Integer,String>> values) {
        this.value = value;
        this.values = values;
    }

    public E getValue() {
        return this.value;
    }

    public void setValue(E value) {
        this.value = value;
    }

    public ArrayList<TwoValues<Integer,String>> getValues() {
        return this.values;
    }

    public void setValues(ArrayList<TwoValues<Integer,String>> values) {
        this.values = values;
    }
}
