
class Ex3 {
    public static void main(String[] args)
    {
        ShuntingYard shunt = new ShuntingYard("[ae03]+@[ae03]+.(com|net|org)(.(gt|cr|ci))?");
        shunt.printShuntingYard();
    }
}