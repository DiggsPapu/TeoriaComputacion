package Classes;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;
public class AFN {
    protected ArrayList<GraphNode<String>> nfa = new ArrayList<>();
    protected Stack<String> tStack= new Stack<>();
    protected Stack<TwoValues<Integer,Integer>> subTreeStack = new Stack<>();
    protected int s0 = 0;
    protected int sf = 1;
    // public AFN(Tree bTree)
    // {
    //     ArrayList<Node<token>> tree = bTree.getBinaryTree();
    //     int i = 0;
    //     for (Node<token> node : tree) {
    //         switch (node.value.getPrecedence()) {
    //             case 2://In case it gets an concat "."
    //             if (tStack.size()>0) {
    //                 if(tStack.size()>1)
    //                 {
    //                     // Second Node
    //                     TwoValues<Integer,String> vals2 = new TwoValues<>();
    //                     int pos1 = i;
    //                     vals2.setVal2(tStack.pop());
    //                     vals2.setVal1(i+2);
    //                     ArrayList<TwoValues<Integer,String>> val2 = new ArrayList<>();
    //                     val2.add(vals2);
    //                     // First Node
    //                     TwoValues<Integer, String> vals1 = new TwoValues<>();
    //                     vals1.setVal1(i+1);
    //                     vals1.setVal2(tStack.pop());
    //                     ArrayList<TwoValues<Integer,String>> val1 = new ArrayList<>();
    //                     val1.add(vals1);
    //                     GraphNode<String> node1 = new GraphNode<>("S"+i++, val1);
    //                     nfa.add(node1);
    //                     GraphNode<String> node2 = new GraphNode<>("S"+i++, val2);
    //                     nfa.add(node2);
    //                     ArrayList<TwoValues<Integer,String>> emptyList = new ArrayList<>();
    //                     GraphNode<String> node3 = new GraphNode<String>("S"+i++,emptyList);
    //                     nfa.add(node3);
    //                     int pos2 = i-1;
    //                     TwoValues<Integer, Integer> positions = new TwoValues<>(pos1,pos2);
    //                     subTreeStack.push(positions);// Add the position of nodes in stack
    //                 }
    //                 else
    //                 {
    //                     // Sub tree structure indexes
    //                     TwoValues<Integer,Integer> positions = subTreeStack.pop();
    //                     System.out.println("Init:"+positions.getVal1()+"End:"+positions.getVal2());
    //                     // Create a new node and add it to the graph
    //                     ArrayList<TwoValues<Integer,String>> emptyList = new ArrayList<>();
    //                     GraphNode<String> newNode = new GraphNode<>("S" + i++,emptyList);
    //                     nfa.add(newNode);
    //                     // Creating a new transition to add to a node inside the graph
    //                     TwoValues<Integer, String> transition = new TwoValues<Integer,String>(nfa.size()-1, tStack.pop());
    //                     nfa.get(positions.getVal2()).getValues().add(transition);
    //                     // Pushing positions of subtree in sub tree stack
    //                     positions.setVal2(nfa.size()-1);
    //                     subTreeStack.push(positions);
    //                 }
    //             }
    //             else
    //             {
    //                 // Sub tree structure indexes
    //                 TwoValues<Integer,Integer> positions2 = subTreeStack.pop();
    //                 TwoValues<Integer,Integer> positions1 = subTreeStack.pop();
    //                 TwoValues<Integer,String> transitionE = new TwoValues<Integer,String>(nfa.size()-1, "ε");
    //                 nfa.get(positions1.getVal2()).getValues().add(transitionE);
    //                 positions1.setVal2(positions2.getVal2());
    //                 subTreeStack.push(positions1);
    //             }
    //             break;
    //             case 1: //In case it gets an or "|"
    //             if (tStack.size()>0) {
    //                 if(tStack.size()>1)
    //                 {
    //                     TwoValues<Integer,Integer> positions = new TwoValues<>();
    //                     TwoValues<Integer,String> transitionE11 = new TwoValues<Integer,String>(i+1, "ε");
    //                     TwoValues<Integer,String> transitionE12 = new TwoValues<Integer,String>(i+3, "ε");
    //                     ArrayList<TwoValues<Integer,String>> initTransitions = new ArrayList<>();
    //                     initTransitions.add(transitionE11);
    //                     initTransitions.add(transitionE12);
    //                     positions.setVal1(i);
    //                     GraphNode<String> initNode = new GraphNode<String>("S"+i++, initTransitions);
    //                     nfa.add(initNode);
    //                     ArrayList<TwoValues<Integer,String>> emptyTransition = new ArrayList<>();
    //                     TwoValues<Integer,String> transition2 = new TwoValues<Integer,String>(i+3, tStack.pop());
    //                     ArrayList<TwoValues<Integer,String>> node21T = new ArrayList<>();
    //                     node21T.add(transition2);
    //                     TwoValues<Integer,String> transition1 = new TwoValues<Integer,String>(i+1, tStack.pop());
    //                     ArrayList<TwoValues<Integer,String>> node11T = new ArrayList<>();
    //                     node11T.add(transition1);
    //                     TwoValues<Integer,String> transitionfN = new TwoValues<Integer,String>(i+4, "ε");
    //                     ArrayList<TwoValues<Integer,String>> lastTFN = new ArrayList<>();
    //                     lastTFN.add(transitionfN);
    //                     GraphNode<String> node11 = new GraphNode<String>("S"+i++, node11T);
    //                     nfa.add(node11);
    //                     GraphNode<String> node12 = new GraphNode<String>("S"+i++, lastTFN);
    //                     nfa.add(node12);
    //                     GraphNode<String> node21 = new GraphNode<String>("S"+i++, node21T);
    //                     nfa.add(node21);
    //                     GraphNode<String> node23 = new GraphNode<String>("S"+i++, lastTFN);
    //                     nfa.add(node23);
    //                     positions.setVal2(i);
    //                     GraphNode<String> finalNode = new GraphNode<String>("S"+i++, emptyTransition);
    //                     nfa.add(finalNode);
    //                     subTreeStack.push(positions);
    //                 }
    //                 else
    //                 {
    //                     // k
    //                     TwoValues<Integer,Integer> positions1 = subTreeStack.pop();

    //                 }
    //             } else {
    //                 TwoValues<Integer,Integer> positions2 = subTreeStack.pop();
    //                 TwoValues<Integer,Integer> positions1 = subTreeStack.pop();
    //                 TwoValues<Integer,String> transitionE11 = new TwoValues<Integer,String>(positions1.getVal1(), "ε");
    //                 TwoValues<Integer,String> transitionE12 = new TwoValues<Integer,String>(positions2.getVal1(), "ε");
    //                 ArrayList<TwoValues<Integer,String>> initTransitions = new ArrayList<>();
    //                 initTransitions.add(transitionE11);
    //                 initTransitions.add(transitionE12);
    //                 GraphNode<String> initNode = new GraphNode<String>("S"+i++, initTransitions);
    //                 nfa.add(initNode);
    //                 ArrayList<TwoValues<Integer,String>> emptyList = new ArrayList<>();
    //                 GraphNode<String> finalNode = new GraphNode<String>("S"+i++, emptyList);
    //                 nfa.add(finalNode);
    //                 TwoValues<Integer,String> transitionE21 = new TwoValues<Integer,String>(i-1, "ε");
    //                 TwoValues<Integer,String> transitionE22 = new TwoValues<Integer,String>(i-1, "ε");
    //                 nfa.get(positions1.getVal2()).getValues().add(transitionE21);
    //                 nfa.get(positions2.getVal2()).getValues().add(transitionE22);
    //                 positions1.setVal1(i-1);
    //                 positions1.setVal2(i);
    //                 subTreeStack.push(positions1);                 
    //             }
    //             break;
    //             default:
    //             tStack.add(node.value.getToken());
    //             break;
    //         }
    //     }
    // }
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
    public boolean belongs2Language(Integer index, String text)
    {
        System.out.println("Index:"+index);
        // Index is the index of the node
        for (TwoValues<Integer,String> index1 : nfa.get(index).getValues()) {
            String character = String.valueOf(text.toCharArray()[0]);
            if (index1.getVal2().equals(character) && text.length() == 1)
            {
                // If is the last character and the transition is equal to the char return true
                return true;
            }
            else if (index1.getVal2().equals("ε") && text.length() == 1)
            {
                // If is the last character and the transition is equal to epsilon
                return true;
            }
            else if (index1.getVal2().equals(character))
            {
                // If is not the last character but it is a valid character
                if (belongs2Language(index1.getVal1(), text.substring(1,text.length())))
                {
                    return true;
                }
            }
            else if (index1.getVal2().equals("ε"))
            {
                // If is not the last character but the transition is ε
                if (belongs2Language(index1.getVal1(), text))
                {
                    return true;
                }
            }
        }
        return false;
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

    public Stack<String> getTStack() {
        return this.tStack;
    }

    public void setTStack(Stack<String> tStack) {
        this.tStack = tStack;
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
