package Classes;
import java.util.ArrayList;
import java.util.HashMap;
public class AFN {
    protected ArrayList<GraphNode<String>> nfa = new ArrayList<>();
    protected HashMap<Integer,String> nodeStack = new HashMap<>();//Index transition
    protected HashMap<Integer,Integer> subTreeStack = new HashMap<>();//Pos 1 index, pos2 index
    protected int s0 = 0;
    public AFN(Tree bTree)
    {
        GraphNode<String> s0 = new GraphNode<String>("S0", null);
        this.nfa.add(s0); //Add S0 to NFA
        ArrayList<Node<token>> tree = bTree.getBinaryTree();
        int i = 0;
        for (Node<token> node : tree) {
            GraphNode<String> newNode = new GraphNode<>();
            newNode.setValue("S"+i);
            nfa.add(newNode);
            switch (node.value.getPrecedence()) {
                case 2://.
                if (nodeStack.size()>0) {
                    int index2 = nodeStack.size()-1;
                    String transition2 = nodeStack.get(index2);
                    int index1 = nodeStack.size()-1;
                    String transition1 = nodeStack.get(index2);
                    nfa.get(index1).
                }
                break;
            
                default:
                nodeStack.put(nfa.size()-1, node.value.getToken());
                break;
            }
            i++;
        }
    }
}
