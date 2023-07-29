import java.util.ArrayList;
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
        tokenizer tokenizer = new tokenizer();
        tokenizer.tokenize("(a|t)c");
        tokenizer.getShuntingYard();
        tokenizer.tokenize("(a|b)*");
        tokenizer.getShuntingYard();
        tokenizer.tokenize("(a*|b*)*");
        tokenizer.getShuntingYard();
        tokenizer.tokenize("((z|a)|b*)*");
        tokenizer.getShuntingYard();
        tokenizer.tokenize("(a|b)*abb(a|b)*");
        tokenizer.getShuntingYard();
        tokenizer.tokenize("0?(1?)?0*");
        tokenizer.getShuntingYard();
        tokenizer.tokenize("if\\([ae]+\\)\\{[ei]+\\}(\\n(else\\{[ji]\\}))");
        tokenizer.getShuntingYard();
        tokenizer.tokenize("[ae/* 03]+@[ae03]+.(com|net|org)(\\.(gt|cr|co+))?");
        tokenizer.getShuntingYard();
    }
}