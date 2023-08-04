package Ejercicio3.Classes;
import java.util.ArrayList;
import java.util.Stack;

public class Tree {
    private Node<token> root;
    private int count;
    private ArrayList<Node<token>> binaryTree = new ArrayList<>();
    private Stack<Integer> nodesStack = new Stack<>();
    private Stack<Integer> tokenStack = new Stack<>();
    public Tree(token postfix[])
    {    
        createSyntaxTree(postfix);
    }
    private void createSyntaxTree(token postfix[])
    {
        count = 0;
        binaryTree = new ArrayList<>();nodesStack = new Stack<>();tokenStack = new Stack<>();
        for (token token : postfix) {
            Node<token> node = new Node<token>(token);
            node.setPos(binaryTree.size());
            binaryTree.add(node);

            if(count>0)
            {
                switch(token.getPrecedence())
                {
                    case 3:
                        if (!tokenStack.isEmpty())
                        {
                            node.left = binaryTree.get(tokenStack.pop());
                            nodesStack.push(binaryTree.size()-1);
                        }
                        else
                        {
                            node.left = binaryTree.get(nodesStack.pop());
                            nodesStack.push(binaryTree.size()-1);
                        }
                    break;
                    case 2:
                        if (!tokenStack.isEmpty())
                        {
                            node.right = binaryTree.get(tokenStack.pop());
                            node.left = binaryTree.get(nodesStack.pop());
                            nodesStack.push(binaryTree.size()-1);
                        }
                        else
                        {
                            node.right = binaryTree.get(nodesStack.pop());
                            node.left = binaryTree.get(nodesStack.pop());
                            nodesStack.push(binaryTree.size()-1);
                        }
                    break;
                    case 1:
                        if (tokenStack.size()==1)
                        {
                            node.right = binaryTree.get(tokenStack.pop());node.left = binaryTree.get(nodesStack.pop());
                            nodesStack.push(binaryTree.size()-1);
                        }
                        else if (tokenStack.size()>1)
                        {
                            node.right = binaryTree.get(tokenStack.pop());node.left = binaryTree.get(tokenStack.pop());
                            nodesStack.push(binaryTree.size()-1); 
                        }
                        else 
                        {
                            node.right = binaryTree.get(nodesStack.pop());node.left = binaryTree.get(nodesStack.pop());
                            nodesStack.push(binaryTree.size()-1);
                        }              
                    break;
                    default:
                    tokenStack.push(binaryTree.size()-1);
                    break;   
                }
                count++;
            }
            else
            {
                tokenStack.push(binaryTree.size()-1);
                count++;
            }
        }
        root = binaryTree.get(nodesStack.pop());
    }
    public void generateGraphicTree()
    {
        if (binaryTree.size()>0)
        {
            for (Node<token> node : binaryTree) {
                
            }
        }
    }
}
