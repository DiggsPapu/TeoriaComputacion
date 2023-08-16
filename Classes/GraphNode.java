package Classes;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Objects;
public class GraphNode<E> {
    // This gives the Sn value
    protected E value;
    // This ArrayList stores the graph node index in the graph and the transition to take to there (Integer, String)
    protected ArrayList<HashMap<Integer, String>> values = new ArrayList<>();  

    public GraphNode() {
    }

    public GraphNode(E value, ArrayList<HashMap<Integer,String>> values) {
        this.value = value;
        this.values = values;
    }

    public E getValue() {
        return this.value;
    }

    public void setValue(E value) {
        this.value = value;
    }

    public ArrayList<HashMap<Integer,String>> getValues() {
        return this.values;
    }

    public void setValues(ArrayList<HashMap<Integer,String>> values) {
        this.values = values;
    }

    public GraphNode value(E value) {
        setValue(value);
        return this;
    }

    public GraphNode values(ArrayList<HashMap<Integer,String>> values) {
        setValues(values);
        return this;
    }

    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof GraphNode)) {
            return false;
        }
        GraphNode graphNode = (GraphNode) o;
        return Objects.equals(value, graphNode.value) && Objects.equals(values, graphNode.values);
    }

    @Override
    public int hashCode() {
        return Objects.hash(value, values);
    }

    @Override
    public String toString() {
        return "{" +
            " value='" + getValue() + "'" +
            ", values='" + getValues() + "'" +
            "}";
    }

}
