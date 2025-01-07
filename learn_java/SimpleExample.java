public class SimpleExample { 

    public static void main(String[] args) {
        int number = 10;
        System.out.println("The number is: " + number);
        double price = 5.99;
        System.out.println("The price is: " + price); 
        String greeting = "Hello, Java!";
        System.out.println(greeting);
        int sum = addNumbers(5, 7);
        System.out.println("The sum is: " + sum);
    }
    public static int addNumbers(int num1, int num2) {  // Function definition with two integer parameters
        return num1 + num2;
    }
}
