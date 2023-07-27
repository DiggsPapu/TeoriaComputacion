
import java.io.*;
import java.util.Scanner;

class Ex3 {
    public static void main(String[] args)
    {
        Stack stack = new Stack();
        stack.count();
        stack.push('a');
        System.out.println(stack.peek());
        stack.print();
        stack.push('0');
        stack.print();
        System.out.println(stack.peek());
        stack.pop();
        stack.print();
        System.out.println(stack.peek());
    }
}