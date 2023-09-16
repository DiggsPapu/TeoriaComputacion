package Classes;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Stack;
public class AFN {
    protected ArrayList<GraphNode<String>> nfa = new ArrayList<>();
    protected ArrayList<GraphNode<String>> afd = new ArrayList<>();
    protected ArrayList<GraphNode<String>> afdSimplified = new ArrayList<>();
    protected ArrayList<Integer> finalStatesAfdSimplified = new ArrayList<>();
    protected ArrayList<Integer> finalStatesAfd = new ArrayList<>();
    protected Stack<TwoValues<Integer,Integer>> subTreeStack = new Stack<>();
    protected ArrayList<String> alphabet = new ArrayList<>();
    protected int s0 = 0;
    protected int sf = 1;
    protected ArrayList<ArrayList<ArrayList<Integer>>> afnTransTable =new ArrayList<>();
    protected ArrayList<ArrayList<Integer>> afdTransTable =new ArrayList<>();
    protected ArrayList<ArrayList<Integer>> afdSimplifiedTransTable =new ArrayList<>();
    public AFN(Tree tree)
    {
        int i = 0;
        // subTreeStack will store the positions and then will just get the data from the array.
        for (int j = 0; j < tree.getBinaryTree().size(); j++) {
            // Hace recorrido postfix
            Node<token> node = tree.getBinaryTree().get(j);
            if (!alphabet.contains(node.value.getToken())&&!node.value.getToken().equals("*")&&!node.value.getToken().equals(".")&&!node.value.getToken().equals("|"))
            {
                alphabet.add(node.value.getToken());
            }
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
        if(!this.alphabet.contains("ε"))
        {
            alphabet.add("ε");
        }
        else if (this.alphabet.indexOf("ε")!= alphabet.size()-1)
        {
            alphabet.remove(this.alphabet.indexOf("ε"));
            alphabet.add("ε");
        }
    }

    public boolean isAccepted(String input) {
        ArrayList<Integer> currentStateSet = new ArrayList<>();
        currentStateSet.add(s0);
        ArrayList<Integer> epsilonClosure = computeEpsilonClosure(currentStateSet);
        for (char c : input.toCharArray()) {
            ArrayList<Integer> nextStateSet = new ArrayList<>();
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
    private ArrayList<Integer> computeEpsilonClosure(ArrayList<Integer> states) {
        Stack<Integer> stack = new Stack<>();
        ArrayList<Integer> visited = new ArrayList<>();
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
    private ArrayList<ArrayList<Integer>> computeTransition(GraphNode<String> state, int val)
    {
        ArrayList<ArrayList<Integer>> transitionSet = new ArrayList<>();
        // Epsilon 
        for (int index = 0; index < alphabet.size()-1; index++) {
            ArrayList<Integer> t = new ArrayList<>();
            transitionSet.add(t);
        }
        for (int i = 0; i < state.values.size(); i++) {
            TwoValues<Integer,String> transition = state.values.get(i);
            for (int index = 0; index < alphabet.size()-1; index++) {
                if(transition.getVal2().equals(alphabet.get(index)))
                {
                    // System.out.println(index);
                    transitionSet.get(index).add(transition.getVal1());
                }
            }
        }
        ArrayList<Integer> stt = new ArrayList<>();
        stt.add(val);
        transitionSet.add(computeEpsilonClosure(stt));
        return transitionSet;
    }
    void generateAFNTransTable(){
        for (int i = 0; i < this.nfa.size(); i++) 
        {
            afnTransTable.add(computeTransition(this.nfa.get(i), i));
        }
    }
    public void generateAFDTransitionTable(){
        generateAFNTransTable();
        this.afdTransTable.add(0,this.afnTransTable.get(s0).get(alphabet.size()-1));
        if(this.afnTransTable.get(s0).get(alphabet.size()-1).contains(sf))
        {
            finalStatesAfd.add(0);
        }
        // Entra en bucle para evaluar cada estado en el estado de transiciones del afd.
        for (int i = 0; i < this.afdTransTable.size(); i++) {
            ArrayList<TwoValues<Integer,String>> transitions = new ArrayList<>();
            GraphNode<String> node = new GraphNode<String>(String.valueOf(Character.toChars(65+i)), transitions);
            afd.add(node);
            ArrayList<Integer> vals = this.afdTransTable.get(i);
            ArrayList<ArrayList<Integer>> possibleV = new ArrayList<>();
            for (int j= 0; j < alphabet.size()-1; j++)
            {
                ArrayList<Integer> val = new ArrayList<>();
                possibleV.add(val);
            }
            for (int u = 0; u < vals.size(); u++) {
                int index = vals.get(u);
                for (int x = 0; x < alphabet.size()-1; x++)
                {
                    ArrayList<Integer> values = this.afnTransTable.get(index).get(x);
                    if (values.size()>0)
                    {
                        for (int y = 0; y < values.size(); y++)
                        {
                            ArrayList<Integer> possibleVals = this.afnTransTable.get(values.get(y)).get(alphabet.size()-1); 
                            for (int j = 0; j < possibleVals.size(); j++)
                            {
                                if (!possibleV.get(x).contains(possibleVals.get(j)))
                                {
                                    possibleV.get(x).add(possibleVals.get(j));
                                }
                            }
                        }
                    }
                }
            }
            for (int n = 0; n < possibleV.size(); n++) {
                if (!this.afdTransTable.contains(possibleV.get(n)))
                {
                    this.afdTransTable.add(possibleV.get(n));
                    TwoValues<Integer,String> trans = new TwoValues<Integer,String>(this.afdTransTable.indexOf(possibleV.get(n)), this.alphabet.get(n%this.alphabet.size())); 
                    this.afd.get(i).getValues().add(trans);
                    if(possibleV.get(n).contains(sf))
                    {
                        finalStatesAfd.add(this.afdTransTable.indexOf(possibleV.get(n)));
                    }
                }
                else if(this.afdTransTable.contains(possibleV.get(n)))
                {
                    TwoValues<Integer,String> trans = new TwoValues<Integer,String>(this.afdTransTable.indexOf(possibleV.get(n)), this.alphabet.get(n%this.alphabet.size())); 
                    this.afd.get(i).getValues().add(trans);
                }
            }
        }
        // for (int index = 0; index < this.afnTransTable.size(); index++) {
        //     System.out.println("\nNodeNum:"+index);
        //     printSet(this.afnTransTable.get(index));
        // }
        // for (int index = 0; index < this.afdTransTable.size(); index++) {
        //     System.out.println("\nNodeNum:"+index);
        //     for (int x = 0; x < this.afdTransTable.get(index).size(); x++)
        //     {
        //         System.out.print(" "+this.afdTransTable.get(index).get(x)+" ");
        //     }
        // }
        // for (int index = 0; index<this.afd.size(); index++)
        // {
        //     System.out.println("\n"+this.afd.get(index).value+": ");
        //     for (int e = 0; e < this.afd.get(index).getValues().size(); e++) {
        //         System.out.println("* "+this.afd.get(index).getValues().get(e).val2+"->"+this.afd.get(index).getValues().get(e).val1);
        //     }
        // }
    }
    public boolean isAcceptedByAFD(String input, ArrayList<GraphNode<String>> newAfd) {
        int currentState = 0;  // Start from the initial state
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            int nextState = getNextState(currentState, c, newAfd);
            if (nextState == -1) {
                // No transition defined for the input character, not accepted
                return false;
            }
            currentState = nextState;
        }
        // Check if the final state is reached
        return finalStatesAfd.contains(currentState);
    }
    private int getNextState(int currentState, char inputSymbol, ArrayList<GraphNode<String>> newAfd) {
        for (TwoValues<Integer, String> transition : newAfd.get(currentState).getValues()) {
            if (transition.getVal2().equals(String.valueOf(inputSymbol))) {
                return transition.getVal1();
            }
        }
        return -1;
    }
    public void generateAfdSimplifiedTransTable(){
        int iteracion = 0;
        System.out.println("Iteración: " + iteracion++ );
        ArrayList<Integer> notFinalState = new ArrayList<>();
        for (int index = 0; index < this.afd.size(); index++) {
            if(!this.finalStatesAfd.contains(index)) {
                notFinalState.add(index);
            }
        }
        this.afdSimplifiedTransTable.add(notFinalState);
        this.afdSimplifiedTransTable.add(this.finalStatesAfd);
        // Creo unas transiciones, de manera que la posicion indicara el terminal, el primer valor la direccion y la segunda a que grupo pertenece
        ArrayList<ArrayList<TwoValues<Integer,Integer>>> transitions = new ArrayList<>();
        for (int index = 0; index < this.afd.size(); index++) {
            // Obtiene las transiciones
            ArrayList<TwoValues<Integer, String>>  nodeTrans = this.afd.get(index).getValues();
            ArrayList<TwoValues<Integer, Integer>> trans = new ArrayList<>();
            for (int index2 = 0; index2 < nodeTrans.size(); index2++ ) {
                for (int index3 = 0; index3 < this.afdSimplifiedTransTable.size(); index3++){
                    // Determina a que grupo pertenece
                    if (this.afdSimplifiedTransTable.get(index3).contains(nodeTrans.get(index2).getVal1())) {
                        TwoValues<Integer,Integer> tr = new TwoValues<Integer,Integer>(nodeTrans.get(index2).getVal1(), index3);
                        trans.add(index2, tr);
                    }
                }
            }
            transitions.add(index, trans);
        }
        printSet(this.afdSimplifiedTransTable);
        printTransitions2(transitions);        
        boolean stillLoop = true;
        while (stillLoop) {
            System.out.println("Iteración: " + iteracion++ );
            // Determinar a que grupo pertenece el nodo
            ArrayList<ArrayList<Integer>> pi = new ArrayList<>();
            for (int index = 0; index < transitions.size(); index++){
                System.out.println("Nodo a evaluar:"+index);
                ArrayList<TwoValues<Integer, Integer>> tr = transitions.get(index);
                if (index==0){
                    // en caso de que sea indice 0 se crea un nuevo grupo por default
                    ArrayList<Integer> trns = new ArrayList<>();
                    trns.add(0);
                    pi.add(trns);
                }
                else {
                    // obtener el nodo prueba del grupo a comparar
                    boolean added = false;
                    for (int index2 = 0; index2 < pi.size(); index2++) {
                        int compareNode = pi.get(index2).get(0);
                        ArrayList<TwoValues<Integer, Integer>> tr1 = transitions.get(compareNode);
                        // pertenecen al mismo grupo anterior
                        for (int index3 = 0; index3 < this.afdSimplifiedTransTable.size(); index3++) {
                            // grupo anterior
                            ArrayList<Integer> grupoAnterior = this.afdSimplifiedTransTable.get(index3);
                            // Si el grupo anterior contiene a ambos
                            if (grupoAnterior.contains(compareNode) && grupoAnterior.contains(index)) {
                                // tienen las transiciones iguales
                                boolean equalTransition = true;
                                for (int index4 = 0; index4 < tr.size(); index4++) {
                                    if (tr.get(index4).getVal2() != tr1.get(index4).getVal2()) {
                                        equalTransition = false;
                                    }
                                }
                                // Se aniade al mismo grupo si tienen transiciones iguales
                                if (equalTransition) {
                                    pi.get(index2).add(index);
                                    added = true;
                                }
                            }
                        }
                    }
                    // Si no se aniadio a ninguno se crea un nuevo grupo y se aniade el indice
                    if (!added) {
                        ArrayList<Integer> trns = new ArrayList<>();
                        trns.add(index);
                        pi.add(trns);
                    }
                }
            }
            // Crear las transiciones
            for (int index = 0; index < transitions.size(); index++) {
                ArrayList<TwoValues<Integer, Integer>> trans = new ArrayList<>();
                // Obtiene las transiciones
                ArrayList<TwoValues<Integer,Integer>> nT = transitions.get(index);
                for (int index2 = 0; index2 < nT.size(); index2++) {
                    // Me devuelve el hacia donde apunta el nodo de la transicion index2
                    Integer node = this.afd.get(nT.get(index2).getVal1()).getValues().get(index2).getVal1();
                    for (int index3 = 0; index3 < this.afdSimplifiedTransTable.size(); index3++){
                        // Determina a que grupo pertenece
                        if (this.afdSimplifiedTransTable.get(index3).contains(node)) {
                            TwoValues<Integer,Integer> tr = new TwoValues<Integer,Integer>(node, index3);
                            trans.add(index2, tr);
                        }
                    }
                }
                transitions.add(index, trans);
                transitions.remove(index+1);
            }
            printTransitions2(transitions);
            printSet(pi);
            if (pi.equals(this.afdSimplifiedTransTable)) {
                stillLoop = false;
            }
            this.afdSimplifiedTransTable = pi;
        }

        for (int index = 0; index < this.afdSimplifiedTransTable.size(); index++) {
            ArrayList<TwoValues<Integer, String>>transition = new ArrayList<>();
            // Obtengo las transiciones para uno de los valores del grupo porque son iguales.
            ArrayList<TwoValues<Integer, String>> values = this.afd.get(this.afdSimplifiedTransTable.get(index).get(0)).getValues();
            // recorrer las transiciones
            for (int index2 = 0; index2 < values.size(); index2++) {
                // ir comparando en cada posible grupo
                for (int index3 = 0; index3 < this.afdSimplifiedTransTable.size(); index3++) {
                    if(this.afdSimplifiedTransTable.get(index3).contains(values.get(index2).getVal1())){
                        TwoValues<Integer, String> trans = new TwoValues<Integer,String>(index3, values.get(index2).getVal2());
                        transition.add(trans);
                    }
                }
            } 
            // construir el afd simplificado
            GraphNode<String> node = new GraphNode<>(String.valueOf("S"+index), transition);
            this.afdSimplified.add(node);
            
            // aniadir los estados de aceptacion
            if(this.finalStatesAfd.contains(this.afdSimplifiedTransTable.get(index).get(0))) {
                this.finalStatesAfdSimplified.add(index);
            }
        }
        for (int i = 0; i < this.afdSimplified.size(); i++) {
            System.out.println(this.afdSimplified.get(i).getValue());
            for (int j = 0; j< this.afdSimplified.get(i).getValues().size(); j++){
                System.out.println("    "+alphabet.get(j)+"->"+this.afdSimplified.get(i).getValues().get(j).getVal1());
            }
        }
        // while (stillLoop) {     
        //     // Iteracion
        //     System.out.println("\n  Iteracion: "+iteracion);
        //     iteracion++;       
        //     // recorre la las transiciones y chequea a que grupo pertenece cada una
        //     for (int index = 0; index < transitions.size(); index++) {
        //     }
        //     for (int index = 0; index < transitions.size(); index++) {
        //         // hace la suplementacion de la nueva iteracion de las transiciones
        //         for (int i = 0; i < transitions.get(index).size(); i++) {
        //             TwoValues<Integer, String> val = transitions.get(index).get(i);
        //             // System.out.println("alphabet:"+val.getVal2()+" pointer:"+val.getVal1());
        //             if ( val.val1 != null) {
        //                 // Reemplazo
        //                 transitions.get(index).add(i, this.afd.get(val.getVal1()).values.get(i));
        //                 transitions.get(index).remove(i+1);
        //             }
        //         }
        //         // Se determina a que grupo pertenece
        //         pi = whichGroupE(pi, transitions, index);
        //     }
        //     // Si son iguales entonces se acaba sino prosigue repitiendose el ciclo
        //     if(!stillInCycle(pi)){
        //         stillLoop = false;
        //     }
        //     this.afdSimplifiedTransTable = pi;
        //     printSet(pi);
        //     printTransitions(transitions);
        //     pi = new ArrayList<>();
        // }
    }
    private void printSet2(ArrayList<Integer> set){
        for (int i = 0; i < set.size(); i++){
            System.out.print(set.get(i)+" ");
        }
    }
    private boolean stillInCycle(ArrayList<ArrayList<Integer>> pi){
        // Si son iguales entonces se acaba sino prosigue repitiendose el ciclo
            if (!pi.equals(this.afdSimplifiedTransTable)) {
                return true;
            }
            return false;
    }
    private ArrayList<ArrayList<Integer>> whichGroupE(ArrayList<ArrayList<Integer>> pi, ArrayList<ArrayList<TwoValues<Integer,String>>> transitions, int index)
    {
        if(index>0) {
            // for (int index = 0; index < array.length; index++) {
                
            // }
            for (int x = 0; x < pi.size();x++) {
                for (int y = 0; y < this.afdSimplifiedTransTable.size(); y++) {
                    int comparator = 1;
                    for (int z = 0; z < this.alphabet.size()-1; z++) {
                        
                        if (transitions.get(pi.get(x).get(0)).get(z).getVal1() == transitions.get(index).get(z).getVal1() && transitions.get(pi.get(x).get(0)).get(z).getVal2() == transitions.get(index).get(z).getVal2()) {
                            comparator *=1;
                        }
                        else{
                            comparator *=0;
                        }
                    }
                    if (this.afdSimplifiedTransTable.get(y).contains(index) && this.afdSimplifiedTransTable.get(y).contains(pi.get(x).get(0)) && comparator!=0) {
                        pi.get(x).add(index);
                        return pi;
                    }
                }
            }
        }
        ArrayList<Integer> newL = new ArrayList<>();
        newL.add(index);
        pi.add(newL);
        return pi;
    }
    void printTransitions(ArrayList<ArrayList<TwoValues<Integer, String>>> transitions) {
        for (int index = 0; index < transitions.size(); index++) {
            System.out.println("Nodo#"+index);
            for (int index2 = 0; index2 < transitions.get(index).size(); index2++) {
                System.out.println("    "+transitions.get(index).get(index2).getVal2()+"->"+transitions.get(index).get(index2).getVal1());
            }
        }
    }

    void printTransitions2(ArrayList<ArrayList<TwoValues<Integer, Integer>>> transitions) {
        for (int index = 0; index < transitions.size(); index++) {
            System.out.println("Nodo#"+index);
            for (int index2 = 0; index2 < transitions.get(index).size(); index2++) {
                System.out.println("    terminal:"+alphabet.get(index2)+"->"+transitions.get(index).get(index2).getVal1()+"     Group:"+transitions.get(index).get(index2).getVal2());
            }
        }
    }
    void printSet(ArrayList<ArrayList<Integer>>set)
    {
        for (int i = 0; i < set.size(); i++) {
            System.out.print("\nGrupo #"+i+": ");
            for (int k = 0; k < set.get(i).size(); k++)
            {
                System.out.print(set.get(i).get(k)+" ");
            }
        }
        System.out.println("");
    }
    void printArray(ArrayList<Integer> array)
    {
        for (int index = 0; index < array.size(); index++) {
            System.out.print(" "+array.get(index)+" ");
        }
    }

    public void generateAFDSimplified(String archive) {
        try {
            FileWriter myWriter = new FileWriter(archive, true);
            if (afdSimplified.size() > 0) {
                myWriter.append("digraph AFD{\nnode [shape=circle];\nrankdir=LR;\n");
                for (int i = 0; i<afdSimplified.size(); i++) {
                    GraphNode<String> node = afdSimplified.get(i);
                    if (finalStatesAfdSimplified.contains(i))
                    {
                        myWriter.append(node.getValue() + "[shape=doublecircle] [label=\"" + node.getValue() + "\"];\n");
                    }
                    else {
                        myWriter.append(node.getValue() + " [label=\"" + node.getValue() + "\"];\n");
                    }
                }
                myWriter.append("init [label=\"\", shape=point];\n");
                for (int i = 0; i<afdSimplified.size(); i++) {
                    GraphNode<String> node = afdSimplified.get(i);
                    if (i==0)
                    {
                        myWriter.append("init->"+node.getValue()+";\n");
                    }
                    for (TwoValues<Integer,String> transition : node.getValues()) {
                        // System.out.println("node:"+node.getValue()+" transition1:"+transition.getVal2()+" index:"+transition.getVal1());
                        afdSimplified.get(transition.getVal1());
                        myWriter.append(node.getValue()+"->"+afdSimplified.get(transition.getVal1()).getValue()+"[label=\""+transition.getVal2()+"\"];\n");
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
    public void generateAFD(String archive) {
        try {
            FileWriter myWriter = new FileWriter(archive, true);
            if (afd.size() > 0) {
                myWriter.append("digraph AFD{\nnode [shape=circle];\nrankdir=LR;\n");
                for (int i = 0; i<afd.size(); i++) {
                    GraphNode<String> node = afd.get(i);
                    if (finalStatesAfd.contains(i))
                    {
                        myWriter.append(node.getValue() + "[shape=doublecircle] [label=\"" + node.getValue() + "\"];\n");
                    }
                    else {
                        myWriter.append(node.getValue() + " [label=\"" + node.getValue() + "\"];\n");
                    }
                }
                myWriter.append("init [label=\"\", shape=point];\n");
                for (int i = 0; i<afd.size(); i++) {
                    GraphNode<String> node = afd.get(i);
                    if (i==0)
                    {
                        myWriter.append("init->"+node.getValue()+";\n");
                    }
                    for (TwoValues<Integer,String> transition : node.getValues()) {
                        // System.out.println("node:"+node.getValue()+" transition1:"+transition.getVal2()+" index:"+transition.getVal1());
                        afd.get(transition.getVal1());
                        myWriter.append(node.getValue()+"->"+afd.get(transition.getVal1()).getValue()+"[label=\""+transition.getVal2()+"\"];\n");
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
                    GraphNode<String> node  = nfa.get(i);
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
