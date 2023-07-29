
class Ex3 {
    public static void main(String[] args)
    {
        // ShuntingYard shunt = new ShuntingYard("{ae03}+@{ae03}+.(com|net|org)(.{gt|cr|ci}+)?");
        // ShuntingYard shunt = new ShuntingYard("aicb*(a|c.a*)?ou");
        // shunt.printShuntingYard();
        //a+(c|b*)k
        // (a|t)c
        // (a|b)*
        // (a*|b*)*
        // ((z|a)|b*)*
        // (a|b)*abb(a|b)*
        // {ae03}+@{ae03}+.(com|net|org)(.{gt|cr|ci}+)?
        // [ae03]+@[ae03]+.(com|net|org)(.(gt|cr|co+))?
        tokenizer tokenizer = new tokenizer("aicb*(a|c.a*)?ou");

        // private Stack operatorStack = new Stack();
        // private Stack postfixStack = new Stack();
    }
}