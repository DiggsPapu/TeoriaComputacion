package Classes;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;
public class AFN {
    protected ArrayList<GraphNode<String>> nfa = new ArrayList<>();
    protected Stack<TwoValues<Integer,Integer>> subTreeStack = new Stack<>();
    protected int s0 = 0;
    protected int sf = 1;
    public AFN(Tree tree)
    {
        int i = 0;
        // subTreeStack will store the positions and then will just get the data from the array.
        for (int j = 0; j < tree.getBinaryTree().size(); j++) {
            // Hace recorrido postfix
            Node<token> node = tree.getBinaryTree().get(j);
            switch (node.value().getPrecedence()) {
                case 3: //Kleene
                // Getting pos of the thing to be kleened
                TwoValues<Integer,Integer> pos = subTreeStack.pop();
                // Epsilone transition from the last to the first, and from the last to the new last and set to the node in nfa
                TwoValues<Integer,String> toFirst = new TwoValues<>(pos.getVal1(), "ε");
                nfa.get(pos.getVal2()).getValues().add(toFirst);
                TwoValues<Integer,String> toLast = new TwoValues<>(i+1, "ε");
                nfa.get(pos.getVal2()).getValues().add(toLast);
                // Create the two new nodes of first and past
                ArrayList<TwoValues<Integer,String>> tn1 = new ArrayList<>();
                toFirst = new TwoValues<Integer,String>(pos.getVal1(), "ε");
                tn1.add(toLast);
                tn1.add(toFirst);
                GraphNode<String> iniNode = new GraphNode<String>("S"+i++, tn1);
                if (pos.getVal1() == s0)
                {
                    s0 = i-1;
                }
                nfa.add(iniNode);
                // Empty transitions of end node
                tn1 = new ArrayList<>();
                iniNode = new GraphNode<String>("S"+i++, tn1);
                if (pos.getVal2() == sf)
                {
                    sf = i-1;
                }
                nfa.add(iniNode);
                pos.setVal1(i-2);
                pos.setVal2(i-1);
                subTreeStack.push(pos);
                break;
                case 2: // Concat
                TwoValues<Integer,Integer> pos2 = subTreeStack.pop();
                TwoValues<Integer,Integer> pos1 = subTreeStack.pop();
                if (pos1.getVal2() == sf)
                {
                    sf = pos2.getVal2();
                }
                TwoValues<Integer,String> conection = new TwoValues<>(pos2.getVal1(), "ε");
                nfa.get(pos1.getVal2()).getValues().add(conection);
                pos1.setVal2(pos2.getVal2());
                subTreeStack.push(pos1);
                break;
                case 1: // OR
                TwoValues<Integer,Integer> position2 = subTreeStack.pop();
                TwoValues<Integer,Integer> position1 = subTreeStack.pop();
                // Epsilon to node 1 and node 2, and the transitions
                TwoValues<Integer,String> t1InitNode = new TwoValues<>(position1.getVal1(), "ε");
                TwoValues<Integer,String> t2InitNode = new TwoValues<>(position2.getVal1(), "ε");
                ArrayList<TwoValues<Integer,String>> transitionsN1 = new ArrayList<>();
                transitionsN1.add(t1InitNode);
                transitionsN1.add(t2InitNode);
                // Create the init node and add it
                GraphNode<String> initNode = new GraphNode<String>("S"+i++, transitionsN1);
                if (position2.getVal1() == s0 || position1.getVal1() == s0)
                {
                    s0 = i-1;
                }
                nfa.add(initNode);
                // Epsilon to end node
                t1InitNode = new TwoValues<>(i, "ε");
                // Empty transitions of end node
                transitionsN1 = new ArrayList<>();
                initNode = new GraphNode<String>("S"+i++, transitionsN1);
                if (position2.getVal2() == sf || position1.getVal2() == sf)
                {
                    sf = i-1;
                }
                nfa.add(initNode);
                // Add the transitions to the corresponding nodes in nfa
                nfa.get(position1.getVal2()).getValues().add(t1InitNode);
                nfa.get(position2.getVal2()).getValues().add(t1InitNode);
                // Push the positions in the stack
                position1.setVal1(i-2);
                position1.setVal2(i-1);
                subTreeStack.push(position1);
                break;
                default:
                // Create the nodes in case it is a symbol
                TwoValues<Integer,Integer> positions = new TwoValues<Integer,Integer>(i,i+1);
                TwoValues<Integer,String> t1 = new TwoValues<Integer,String>(i+1, node.value().getToken());
                ArrayList<TwoValues<Integer,String>> node1T = new ArrayList<>();
                node1T.add(t1);
                GraphNode<String> node1 = new GraphNode<String>("S"+i, node1T);
                i++;
                node1T = new ArrayList<>();
                GraphNode<String> node2 = new GraphNode<String>("S"+i, node1T);
                i++;
                nfa.add(node1);
                nfa.add(node2);
                subTreeStack.push(positions);
                break;
            }
        }
    }

    public boolean isAccepted(String input) {
        Set<Integer> currentStateSet = new HashSet<>();
        currentStateSet.add(s0);
        Set<Integer> epsilonClosure = computeEpsilonClosure(currentStateSet);
        for (char c : input.toCharArray()) {
            Set<Integer> nextStateSet = new HashSet<>();
            for (int state : epsilonClosure) {
                for (TwoValues<Integer, String> transition : nfa.get(state).getValues()) {
                    if (transition.getVal2().equals(String.valueOf(c))) {
                        nextStateSet.add(transition.getVal1());
                    }
                }
            }
            epsilonClosure = computeEpsilonClosure(nextStateSet);
        }
        return epsilonClosure.contains(sf);
    }
    private Set<Integer> computeEpsilonClosure(Set<Integer> states) {
        Stack<Integer> stack = new Stack<>();
        Set<Integer> visited = new HashSet<>();
        stack.addAll(states);
        visited.addAll(states);
        while (!stack.isEmpty()) {
            int state = stack.pop();
            for (TwoValues<Integer, String> transition : nfa.get(state).getValues()) {
                if (transition.getVal2().equals("ε") && !visited.contains(transition.getVal1())) {
                    stack.push(transition.getVal1());
                    visited.add(transition.getVal1());
                }
            }
        }
        return visited;
    }

    public void generateAFN(String archive) {
        try {
            FileWriter myWriter = new FileWriter(archive, true);
            if (nfa.size() > 0) {
                myWriter.append("digraph AFN{\nnode [shape=circle];\nrankdir=LR;\n");
                for (int i = 0; i<nfa.size(); i++) {
                    GraphNode<String> node = nfa.get(i);
                    if (i == sf)
                    {
                        myWriter.append(node.getValue() + "[shape=doublecircle] [label=\"" + node.getValue() + "\"];\n");
                    }
                    else if (i == 0)
                    {
                        myWriter.append("init [label=\"\", shape=point];\n");
                    }
                    else {
                        myWriter.append(node.getValue() + " [label=\"" + node.getValue() + "\"];\n");
                    }
                }
                for (int i = 0; i<nfa.size(); i++) {
                    GraphNode<String> node = nfa.get(i);
                    if (i==s0)
                    {
                        myWriter.append("init->"+node.getValue()+"[label=\"ε\"];\n");
                    }
                    for (TwoValues<Integer,String> transition : node.getValues()) {
                        // System.out.println("node:"+node.getValue()+" transition1:"+transition.getVal2()+" index:"+transition.getVal1());
                        nfa.get(transition.getVal1());
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

    public ArrayList<GraphNode<String>> getNfa() {
        return this.nfa;
    }

    public void setNfa(ArrayList<GraphNode<String>> nfa) {
        this.nfa = nfa;
    }

    public Stack<TwoValues<Integer,Integer>> getSubTreeStack() {
        return this.subTreeStack;
    }

    public void setSubTreeStack(Stack<TwoValues<Integer,Integer>> subTreeStack) {
        this.subTreeStack = subTreeStack;
    }

    public int getS0() {
        return this.s0;
    }

    public void setS0(int s0) {
        this.s0 = s0;
    }

    public int getSf() {
        return this.sf;
    }

    public void setSf(int sf) {
        this.sf = sf;
    }

}
