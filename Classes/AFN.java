package Classes;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Stack;
public class AFN {
    protected ArrayList<GraphNode<String>> nfa = new ArrayList<>();
    protected Stack<String> tStack= new Stack<>();
    protected Stack<TwoValues<Integer,Integer>> subTreeStack = new Stack<>();
    protected int s0 = 0;
    public AFN(Tree bTree)
    {
        ArrayList<Node<token>> tree = bTree.getBinaryTree();
        int i = 0;
        for (Node<token> node : tree) {
            switch (node.value.getPrecedence()) {
                case 2://.
                if (tStack.size()>0) {
                    if(tStack.size()>1)
                    {
                        // Second Node
                        TwoValues<Integer,String> vals2 = new TwoValues<>();
                        int pos1 = i;
                        vals2.setVal2(tStack.pop());
                        vals2.setVal1(i+2);
                        ArrayList<TwoValues<Integer,String>> val2 = new ArrayList<>();
                        val2.add(vals2);
                        // First Node
                        TwoValues<Integer, String> vals1 = new TwoValues<>();
                        vals1.setVal1(i+1);
                        vals1.setVal2(tStack.pop());
                        ArrayList<TwoValues<Integer,String>> val1 = new ArrayList<>();
                        val1.add(vals1);
                        GraphNode<String> node1 = new GraphNode<>("S"+i++, val1);
                        nfa.add(node1);
                        GraphNode<String> node2 = new GraphNode<>("S"+i++, val2);
                        nfa.add(node2);
                        ArrayList<TwoValues<Integer,String>> emptyList = new ArrayList<>();
                        GraphNode<String> node3 = new GraphNode<String>("S"+i++,emptyList);
                        nfa.add(node3);
                        int pos2 = i-1;
                        TwoValues<Integer, Integer> positions = new TwoValues<>(pos1,pos2);
                        subTreeStack.push(positions);// Add the position of nodes in stack
                    }
                    else
                    {
                        // Sub tree structure indexes
                        TwoValues<Integer,Integer> positions = subTreeStack.pop();
                        System.out.println("Init:"+positions.getVal1()+"End:"+positions.getVal2());
                        // Create a new node and add it to the graph
                        ArrayList<TwoValues<Integer,String>> emptyList = new ArrayList<>();
                        GraphNode<String> newNode = new GraphNode<>("S" + i++,emptyList);
                        nfa.add(newNode);
                        // Creating a new transition to add to a node inside the graph
                        TwoValues<Integer, String> transition = new TwoValues<Integer,String>(nfa.size()-1, tStack.pop());
                        nfa.get(positions.getVal2()).getValues().add(transition);
                        // Pushing positions of subtree in sub tree stack
                        positions.setVal2(nfa.size()-1);
                        subTreeStack.push(positions);
                    }
                }
                else
                {
                    // Sub tree structure indexes
                    TwoValues<Integer,Integer> positions2 = subTreeStack.pop();
                    TwoValues<Integer,Integer> positions1 = subTreeStack.pop();
                    TwoValues<Integer,String> transitionE = new TwoValues<Integer,String>(nfa.size()-1, "ε");
                    nfa.get(positions1.getVal2()).getValues().add(transitionE);
                    positions1.setVal2(positions2.getVal2());
                    subTreeStack.push(positions1);
                }
                break;
            
                default:
                tStack.add(node.value.getToken());
                break;
            }
        }
    }
    public void generateAFN(String archive) {
        try {
            FileWriter myWriter = new FileWriter(archive, true);
            if (nfa.size() > 0) {
                myWriter.append("digraph AFN{\nnode [shape=circle];\n");
                for (GraphNode<String> node : nfa) {
                    myWriter.append(node.getValue() + " [label=\"" + node.getValue() + "\"];\n");
                }
                for (GraphNode<String> node : nfa) {
                    for (TwoValues<Integer,String> transition : node.getValues()) {
                        myWriter.append(node.getValue()+"->"+nfa.get(transition.getVal1()).getValue()+"[label=\""+transition.getVal2()+"\"];\n");
                    }
                    // myWriter.append(node.getValue()+"->"+node.getValues().);
                }
                myWriter.append("}\n");
            }
            myWriter.close();
        } catch (Exception e) {
            System.out.println("couldn't be done");
        }
    }

}
