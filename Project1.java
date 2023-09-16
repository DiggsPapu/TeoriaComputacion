import Classes.AFN;
import Classes.Tree;
import Classes.tokenizer;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;


public class Project1 {
     public static void main(String[] args)
    {
        // a+(c|b*)k
        // (a|t)c
        // (a|b)*
        // (a*|b*)*
        // ((ε|a)|b*)*
        // (a|b)*abb(a|b)*
        // 0?(1?)?0*
        // if\\([ae]+\)\\{[ei]+\\})
        // [ae03]+@[ae03]+.(com|net|org)(.(gt|cr|co+))?
        // aicb*(\\*a|c.a*\\))?ou
        // (ao|ba(a|e)|i|(o|u)*o)
        // ( (ao)|((ba)(a|e))|(i)|((o|u)*o) )
        Scanner scanner = new Scanner(System.in);
        tokenizer tokenizer = new tokenizer();
        BufferedReader reader;
		try {
			reader = new BufferedReader(new FileReader("./sample.txt"));
			String line = reader.readLine();
			while (line != null) {
				System.out.println(line);
				// System.out.println("If in the regex there are dots that are used as normal characters and not like operator of concat press 1 else press any other: ");
                // if (!scanner.nextLine().equals("1"))
                // {
                //     tokenizer.setDotSpecial(false);
                // }
                // else{
                //     tokenizer.setDotSpecial(true);
                // }
                tokenizer.setDotSpecial(false);
                tokenizer.tokenize(line);
                tokenizer.getShuntingYard();
                Tree tree = new Tree(tokenizer.getPostfixStack().totokenArray());
                AFN afn = new AFN(tree);
                afn.generateAFDTransitionTable();
                afn.generateAfdSimplifiedTransTable();
                // System.out.println("Enter the filename where you want to save an archive with a graph of the AST:");
                // tree.generateGraphicTree(scanner.nextLine());
                // System.out.println("Enter the filename where you want to save an archive with a graph of the AFN generated:");
                // afn.generateAFN(scanner.nextLine());
                // System.out.println("Enter the filename where you want to save an archive with a graph of the AFD generated:");
                // afn.generateAFD(scanner.nextLine());
                System.out.println("Enter the filename where you want to save an archive with a graph of the AFD Simplified generated:");
                afn.generateAFDSimplified(scanner.nextLine());
                // while (true)
                // {
                //     System.out.println("Enter a chain to determine whether it is accepted");
                //     if (afn.isAccepted(scanner.nextLine()))
                //     {
                //         System.out.println("w∈L(r)?\nYes");
                //     }
                //     else{
                //         System.out.println("No");
                //     }
                //     System.out.println("Do you want to continue checking if strings are part of the lenguage? (y/n):");
                //     if(scanner.nextLine().equals("n"))
                //     {
                //         break;
                //     }
                // }
                line = reader.readLine();
			}
			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
       scanner.close();
    }
// ./Graphs/Tree/ast1.dot
// ./Graphs/Tree/ast2.dot
// ./Graphs/Tree/ast3.dot
// ./Graphs/Tree/ast4.dot
// ./Graphs/Tree/ast5.dot

// ./Graphs/AFN/afn1.dot
// ./Graphs/AFN/afn2.dot
// ./Graphs/AFN/afn3.dot
// ./Graphs/AFN/afn4.dot
// ./Graphs/AFN/afn5.dot

// ./Graphs/AFD/afd1.dot
// ./Graphs/AFD/afd2.dot
// ./Graphs/AFD/afd3.dot
// ./Graphs/AFD/afd4.dot
// ./Graphs/AFD/afd5.dot

// ./Graphs/SimplifiedAFD/afd1.dot
// ./Graphs/SimplifiedAFD/afd2.dot
// ./Graphs/SimplifiedAFD/afd3.dot
// ./Graphs/SimplifiedAFD/afd4.dot
// ./Graphs/SimplifiedAFD/afd5.dot


}
