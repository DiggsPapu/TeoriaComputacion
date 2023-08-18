package Classes;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Stack;

public class Tree {
    private Node<token> root;
    private int count;
    private ArrayList<Node<token>> binaryTree = new ArrayList<>();
    private Stack<Integer> nodesStack = new Stack<>();
    private Stack<Integer> tokenStack = new Stack<>();

    public Tree(token postfix[]) {
        createSyntaxTree(postfix);
    }
    public ArrayList<Node<token>> getBinaryTree() {
        return binaryTree;
    }

    private void createSyntaxTree(token postfix[]) {
        count = 0;
        binaryTree = new ArrayList<>();
        nodesStack = new Stack<>();
        tokenStack = new Stack<>();
        if(postfix.length>1)
        {
            for (token token : postfix) {
                Node<token> node = new Node<token>(token);
                node.setPos(binaryTree.size());
                binaryTree.add(node);
                if (count > 0) {
                    switch (token.getPrecedence()) {
                        case 3:
                            if (!tokenStack.isEmpty()) {
                                node.left = binaryTree.get(tokenStack.pop());
                                nodesStack.push(binaryTree.size() - 1);
                            } else {
                                node.left = binaryTree.get(nodesStack.pop());
                                nodesStack.push(binaryTree.size() - 1);
                            }
                            break;
                        case 2:
                            if (!tokenStack.isEmpty()) {
                                if(tokenStack.size()>1)
                                {
                                    node.right = binaryTree.get(tokenStack.pop());
                                    node.left = binaryTree.get(tokenStack.pop());
                                    nodesStack.push(binaryTree.size() - 1);
                                }
                                else
                                {
                                    node.right = binaryTree.get(tokenStack.pop());
                                    node.left = binaryTree.get(nodesStack.pop());
                                    nodesStack.push(binaryTree.size() - 1);
                                }
                            } else {
                                node.right = binaryTree.get(nodesStack.pop());
                                node.left = binaryTree.get(nodesStack.pop());
                                nodesStack.push(binaryTree.size() - 1);
                            }
                            break;
                        case 1:
                            if (tokenStack.size() == 1) {
                                node.right = binaryTree.get(tokenStack.pop());
                                node.left = binaryTree.get(nodesStack.pop());
                                nodesStack.push(binaryTree.size() - 1);
                            } else if (tokenStack.size() > 1) {
                                node.right = binaryTree.get(tokenStack.pop());
                                node.left = binaryTree.get(tokenStack.pop());
                                nodesStack.push(binaryTree.size() - 1);
                            } else {
                                node.right = binaryTree.get(nodesStack.pop());
                                node.left = binaryTree.get(nodesStack.pop());
                                nodesStack.push(binaryTree.size() - 1);
                            }
                            break;
                        default:
                            tokenStack.push(binaryTree.size() - 1);
                            break;
                    }
                    count++;
                } else {
                    tokenStack.push(binaryTree.size() - 1);
                    count++;
                }
            }
            root = binaryTree.get(nodesStack.pop());
        }
        else
        {
            Node<token> node = new Node<token>(postfix[0]);
            binaryTree.add(node);
            root = binaryTree.get(0);
        }
    }

    public void generateGraphicTree(String archive) {
        try {
            FileWriter myWriter = new FileWriter(archive, true);
            if (binaryTree.size() > 0) {
                myWriter.append("digraph Tree{\nnode [shape=circle];\n");
                for (Node<token> node : binaryTree) {
                    myWriter.append("node" + node.getPos() + " [label=\"" + node.value.getToken() + "\"];\n");
                }
                for (Node<token> node : binaryTree) {
                    if (node.left != null) {
                        myWriter.append("node" + node.getPos() + "->" + "node" + node.left.getPos() + ";\n");
                    }
                    if (node.right != null) {
                        myWriter.append("node" + node.getPos() + "->" + "node" + node.right.getPos() + ";\n");
                    }
                }
                myWriter.append("}\n");
            }
            myWriter.close();
        } catch (Exception e) {
            System.out.println("couldn't be done");
        }
    }
}
