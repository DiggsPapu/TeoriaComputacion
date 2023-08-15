import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

import Classes.Tree;
import Classes.tokenizer;

public class Lab4 {
     public static void main(String[] args)
    {
        // a+(c|b*)k
        // (a|t)c
        // (a|b)*
        // (a*|b*)*
        // ((z|a)|b*)*
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
			reader = new BufferedReader(new FileReader("/home/dieggspapu/UVG/TeoriaComputacion/sample.txt"));
			String line = reader.readLine();
			while (line != null) {
				System.out.println(line);
				System.out.println("If in the regex there are dots that are used as normal characters and not like operator of concat press 1 else press any other: ");
                if (!scanner.nextLine().equals("1"))
                {
                    tokenizer.setDotSpecial(false);
                }
                else{
                    tokenizer.setDotSpecial(true);
                }
                tokenizer.tokenize(line);
                tokenizer.getShuntingYard();
                Tree tree = new Tree(tokenizer.getPostfixStack().totokenArray());
                System.out.println("Enter the filename where you want to save an archive with a graph of the AST:");
                tree.generateGraphicTree(scanner.nextLine());
                line = reader.readLine();
			}
			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
       scanner.close();
    }
    // /home/dieggspapu/UVG/TeoriaComputacion/Graphs/graph1.dot
    // /home/dieggspapu/UVG/TeoriaComputacion/Graphs/graph2.dot
    // /home/dieggspapu/UVG/TeoriaComputacion/Graphs/graph3.dot
    // /home/dieggspapu/UVG/TeoriaComputacion/Graphs/graph4.dot
    // /home/dieggspapu/UVG/TeoriaComputacion/Graphs/graph5.dot
    
}
