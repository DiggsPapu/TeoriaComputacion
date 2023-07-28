
public class ShuntingYard {
    private char[] specialChar = {'*','\\','(',')','.','+','?','^','|'};
    private Stack operatorStack = new Stack();
    private Stack postfixStack = new Stack();
    
    public ShuntingYard(String string)
    {
        char[] chars = string.toCharArray();
        translateToValidRegex(chars);
        // for (int i = 0; i < chars.length; i++) {
        //     switch (chars[i]) {
        //         case '(':
        //             operatorStack.push('(');
        //             break;
        //         case ')':
        //             while (operatorStack.peek()!='(') {
        //                 postfixStack.push(operatorStack.pop());
        //             }operatorStack.pop();
        //             break;
        //         case '\\':
        //             postfixStack.push(chars[i++]);                    
        //             break;
        //         case '+':
                    
        //         default:
        //             postfixStack.push(chars[i]);
        //             break;
        //     }
        // }
    }
    private char[] translateToValidRegex(char[]chars)
    {
        Stack temp = new Stack();
        for (int i = 0; i < chars.length; i++) {
            switch (chars[i])
            {
                case '+':
                    if(chars[i-1]==')'||chars[i-1]==']'||chars[i-1]=='}')
                    {
                        char[] temporal = temp.toCharArray();
                        int j = getTheOtherParenthesis(temporal,chars[i-1]);
                        for (int k2 = j ;k2 < temporal.length; k2++) {
                            temp.push(temporal[k2]);
                        }
                    }
                    else
                    {
                        temp.push(temp.peek());
                    }
                    temp.push('*');
                    break;
                case '.':
                    if (chars[i-1]=='\\')
                    {
                        temp.push('.');
                    }
                    break;
                case '?':
                    if(chars[i-1]==')'||chars[i-1]==']'||chars[i-1]=='}')
                    {
                        int j = getTheOtherParenthesis(temp.toCharArray(),chars[i-1]);
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
                        char temporal = temp.pop();
                        temp.push('(');
                        temp.push(temporal);
                        temp.push('|');
                        temp.push('ε');
                        temp.push(')');//a?=a|ε a+=aa*
                    }
                break;
                default:
                    temp.push(chars[i]);
                break;
            }
        }
        temp.print();
        return chars;
    }
    private int getTheOtherParenthesis(char[] chars, char symbol)
    {
        int j = chars.length-2;int k = 1;// k is the value that indicates equality in parenthesis and j will tell me where the pattern starts
        while(true)
        {
            if(symbol == ')')
            {
                if(chars[j]==')')
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
    public void printShuntingYard()
    {
        postfixStack.print();
    }  
    public boolean isSpecialChar(char character){
        for (char c : this.specialChar) {
            if(c == character)
            {
                return true;
            }
        }
        return false;
    }
    private int getPrecedence(char c)
    {
        switch (c)
        {
            case '(':
                return 0;
            case '|':
                return 1;
            case '.':
                return 2;
            case '\\':
                return -3;
            
            case '^':
                return 5;
            default:
                return 0;
        }
    }

}
