import java.io.FileWriter;
import java.util.ArrayList;
public class tokenizer {
    private boolean dotSpecial = true;
    private char[] specialChar = {'*','(',')','.','|'};
    private ArrayList<token> list = new ArrayList<token>();
    private TokenStack operatorStack = new TokenStack();
    private TokenStack postfixStack = new TokenStack();
    public void setDotSpecial(boolean dotSpecial) {
        this.dotSpecial = dotSpecial;
    }
    public void tokenize(String string)
    {
        list = new ArrayList<>();
        char[] chars = translateToValidRegex(string.toCharArray());
        for (int j = 0; j < chars.length; j++) {
            token tok = new token(String.valueOf(chars[j]));
            if(chars[j]=='\\')
            {
                j++;
                tok = new token(String.valueOf(chars[j-1])+String.valueOf(chars[j]));
                list.add(tok);
            }
            else
            {
                list.add(tok);
            }
            if (j!=chars.length-1 && (tok.getPrecedence()<0 || chars[j]=='*' || chars[j]==')') && (!isOperator(chars[j+1]) || chars[j+1]=='('))
            {
                token dot = new token(".");
                list.add(dot);
            }
        }
        System.out.print("Initial value: "+string+"\nConversion to Acceptable Regex: ");
        for (int index = 0; index < list.size(); index++) {
            token token = list.get(index);
            // System.out.println("Value: "+token.getToken()+" Precedence: "+token.getPrecedence());
            System.out.print(token.getToken());
        }
        System.out.print("\n");
    }
    public ArrayList<token> getList() {
        return list;
    }
    private int getTheOtherParenthesis(char[] chars, char symbol)
    {
        int j = chars.length-2;int k = 1;// k is the value that indicates equality in parenthesis and j will tell me where the pattern starts
        while(true)
        {
            if(symbol == ')')
            {
                if(chars[j]==')' && j==0)
                {
                    k++;
                }
                else if (chars[j]==')' && chars[j-1]!='\\')
                {
                    k++;
                }
                else if(chars[j]=='(')
                {
                    k--;
                }
                if(k==0)
                {
                    return j;
                }
            }
            else if(symbol == ']')
            {
                if(chars[j]==']')
                {
                    k++;
                }
                else if(chars[j]=='[')
                {
                    k--;
                }
                if(k==0)
                {
                    return j;
                }
            }
            else if(symbol == '}')
            {
                if(chars[j]=='}')
                {
                    k++;
                }
                else if(chars[j]=='{')
                {
                    k--;
                }
                if(k==0)
                {
                    return j;
                }
            }
            j--;
        }
    }
    private char[] translateToValidRegex(char[]chars)
    {
        Stack temp = new Stack();
        for (int i = 0; i < chars.length; i++) {
            switch (chars[i])
            {
                case '[':
                    i++;
                    temp.push('(');
                    while(chars[i]!=']')
                    {
                        temp.push(chars[i]);
                        if (chars[i+1]!=']')
                        {
                            temp.push('|');
                        }
                        i++;
                    }
                    temp.push(')');
                    break;
                case '+':
                    char[] temporal = temp.toCharArray();
                    if(temp.peek()==')')
                    {
                        int j = getTheOtherParenthesis(temporal,temp.peek());
                        for (int k2 = j ;k2 < temporal.length; k2++) 
                        {
                            temp.push(temporal[k2]);
                        }
                    }
                    else
                    {
                        temp.push(temp.peek());
                    }
                    temp.push('*');
                    break;
                case '?':
                    if(temp.peek()==')')
                    {
                        int j = getTheOtherParenthesis(temp.toCharArray(),temp.peek());
                        Stack temp2 = new Stack();
                        for (int k2 = temp.count() ;k2 > j; k2--) {
                            temp2.push(temp.pop());
                        }
                        temp.push('(');
                        int len = temp2.count();
                        for (int k2 = 0 ;k2 < len; k2++) {
                            temp.push(temp2.pop());
                        }
                        temp.push('|');temp.push('ε');temp.push(')');
                    }
                    else
                    {
                        char tempo = temp.pop();
                        temp.push('(');
                        temp.push(tempo);
                        temp.push('|');
                        temp.push('ε');
                        temp.push(')');
                        //a?=a|ε a+=aa*
                    }
                break;
                case '.':
                    if (!dotSpecial)
                    {
                        temp.push('\\');
                    }
                    temp.push('.');
                    break;
                default:
                    temp.push(chars[i]);
                    break;
            }
        }
        chars = temp.toCharArray();
        return chars;
    }
    private boolean isOperator(char c)
    {
        for (int i = 0; i < specialChar.length; i++) {
            if(c==specialChar[i])
            {
                return true;
            }
        }
        return false;
    }
    void getShuntingYard()
    {
        try {
            FileWriter myWriter = new FileWriter("filename.txt");
            operatorStack = new TokenStack();
            postfixStack = new TokenStack();
            for (int i = 0; i < list.size(); i++) {
                myWriter.write(i+".) Postfix stack: ");
                postfixStack.writeStack(myWriter);
                myWriter.write(" Operator:");
                operatorStack.writeStack(myWriter);
                myWriter.write("\n");
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
            myWriter.write("The postfix expression is:");
            for (int i = 0; i < array.length; i++) {
                myWriter.write(array[i].getToken());
            }
            myWriter.write("\n\n");
            myWriter.close();
        } catch (Exception e) {
            // TODO: handle exception
        }
    }
}
