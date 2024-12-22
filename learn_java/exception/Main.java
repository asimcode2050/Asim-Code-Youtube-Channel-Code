public class Main {
    public static void main(String[] args) {
        try {
            int result = 10 / 0; 
            System.out.println("The result is: " + result);
        } // Here comes the 'catch' block. If an error happens in the 'try' block, we catch it here.
        catch (ArithmeticException e) {
            System.out.println("Oops! There was an error: " + e.getMessage());
        } 
        finally {
            System.out.println("This always runs - whether there was an error or not. Neat, right?");
        }
        System.out.println("The program continues running smoothly...");
    }
}
