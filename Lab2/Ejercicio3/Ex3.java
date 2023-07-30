package Ejercicio3;
import java.util.ArrayList;
import java.util.Scanner;
class Ex3 {
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
        System.out.println("If in the regex there are dots that are used as normal characters and not like operator of concat press 1 else press any other: ");
        if (scanner.nextLine()!="1")
        {
            tokenizer.setDotSpecial(false);
        }
        else{
            tokenizer.setDotSpecial(true);
        }
        tokenizer.tokenize("(a|t)c");
        tokenizer.getShuntingYard();
        System.out.println("If in the regex there are dots that are used as normal characters and not like operator of concat press 1 else press any other: ");
        if (scanner.nextLine()!="1")
        {
            tokenizer.setDotSpecial(false);
        }
        else{
            tokenizer.setDotSpecial(true);
        }
        tokenizer.tokenize("(a|b)*");
        tokenizer.getShuntingYard();
        System.out.println("If in the regex there are dots that are used as normal characters and not like operator of concat press 1 else press any other: ");
        if (scanner.nextLine()!="1")
        {
            tokenizer.setDotSpecial(false);
        }
        else{
            tokenizer.setDotSpecial(true);
        }
        tokenizer.tokenize("(a*|b*)*");
        tokenizer.getShuntingYard();
        System.out.println("If in the regex there are dots that are used as normal characters and not like operator of concat press 1 else press any other: ");
        if (scanner.nextLine()!="1")
        {
            tokenizer.setDotSpecial(false);
        }
        else{
            tokenizer.setDotSpecial(true);
        }
        tokenizer.tokenize("((z|a)|b*)*");
        tokenizer.getShuntingYard();
        System.out.println("If in the regex there are dots that are used as normal characters and not like operator of concat press 1 else press any other: ");
        if (scanner.nextLine()!="1")
        {
            tokenizer.setDotSpecial(false);
        }
        else{
            tokenizer.setDotSpecial(true);
        }
        tokenizer.tokenize("(a|b)*abb(a|b)*");
        tokenizer.getShuntingYard();
        System.out.println("If in the regex there are dots that are used as normal characters and not like operator of concat press 1 else press any other: ");
        if (scanner.nextLine()!="1")
        {
            tokenizer.setDotSpecial(false);
        }
        else{
            tokenizer.setDotSpecial(true);
        }
        tokenizer.tokenize("0?(1?)?0*");
        tokenizer.getShuntingYard();
        System.out.println("If in the regex there are dots that are used as normal characters and not like operator of concat press 1 else press any other: ");
        if (scanner.nextLine()!="1")
        {
            tokenizer.setDotSpecial(false);
        }
        else{
            tokenizer.setDotSpecial(true);
        }
        tokenizer.tokenize("if\\([ae]+\\)\\{[ei]+\\}(\\n(else\\{[ji]\\}))");
        tokenizer.getShuntingYard();
        System.out.println("If in the regex there are dots that are used as normal characters and not like operator of concat press 1 else press any other: ");
        if (scanner.nextLine()!="1")
        {
            tokenizer.setDotSpecial(false);
        }
        else{
            tokenizer.setDotSpecial(true);
        }
        tokenizer.tokenize("[ae/* 03]+@[ae03]+.(com|net|org)(\\.(gt|cr|co+))?");
        tokenizer.getShuntingYard();
    }
}