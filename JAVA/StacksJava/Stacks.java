package Java.StacksJava;

public class Stacks {

    public static void main(String[] args) {
        StackApp my_stack = new StackApp(10);

        my_stack.push(10);
        my_stack.push(20);
        my_stack.push(40);
        my_stack.push(30);
        System.out.println(my_stack.peek());
        my_stack.display();
        my_stack.push(60);
        my_stack.push(80);
        my_stack.display();
        System.out.println(my_stack.pop());
        my_stack.display();
        my_stack.push(100);
        my_stack.push(50);
        my_stack.push(90);
        my_stack.display();

        while (!my_stack.isEmpty()) {
            long value = my_stack.pop();
            System.out.print(value);
            System.out.print(" ");

        }
        System.out.println("");
    }

}