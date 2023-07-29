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
        // tokenizer.tokenize("if\\([ae]+\\)\\{[ei]+\\}(\\n(else\\{[ji]\\}))");
        tokenizer.tokenize("[ae03]+@[ae03]+.(com|net|org)(.(gt|cr|co+))?");
        ArrayList<token> list = tokenizer.getList();
        TokenStack operatorStack = new TokenStack();
        TokenStack postfixStack = new TokenStack();
        for (int i = 0; i < list.size(); i++) {
            System.out.print(i+".) Postfix stack:");
            postfixStack.print();
            System.out.print(" Operator:");
            operatorStack.print();System.out.print("\n");
            token token = list.get(i);
            switch (token.getToken())
            {
                case "(":
                    operatorStack.push(token);
                    break;
                case ")":
                    if (!operatorStack.isEmpty())
                    {
                        while (operatorStack.peek().getPrecedence()!=0) {
                            postfixStack.push(operatorStack.pop());
                        }
                        operatorStack.pop();
                    }
                    break;
                default:
                    if(token.getPrecedence()>0)
                    {
                        if (!operatorStack.isEmpty())
                        {
                            if (token.getPrecedence()<=operatorStack.peek().getPrecedence())
                            {
                                while(!operatorStack.isEmpty()&&operatorStack.peek().getPrecedence()!=0)
                                {
                                    postfixStack.push(operatorStack.pop());
                                }
                            }
                        }
                        operatorStack.push(token);
                    }
                    else
                    {
                        postfixStack.push(token);
                    }
                    break;  
            }
        }
         while(!operatorStack.isEmpty())
        {
            postfixStack.push(operatorStack.pop());
        }
        token array[] = postfixStack.totokenArray();
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i].getToken());
        }
    }
}