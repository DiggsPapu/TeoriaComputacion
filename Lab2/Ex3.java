
class Ex3 {
    public static void main(String[] args)
    {
        // ShuntingYard shunt = new ShuntingYard("{ae03}+@{ae03}+.(com|net|org)(.{gt|cr|ci}+)?");
        ShuntingYard shunt = new ShuntingYard("b*(a|c.a*)?");
        //a+(c|b*)k
        // (a|t)c
        // (a|b)*
        // (a*|b*)*
        // ((z|a)|b*)*
        // (a|b)*abb(a|b)*
        // {ae03}+@{ae03}+.(com|net|org)(.{gt|cr|ci}+)?
        shunt.printShuntingYard();
    }
}