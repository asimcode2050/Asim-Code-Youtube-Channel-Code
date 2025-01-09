public class ForLoopExample {
    public static void main(String[] args) {
        /*
         for (initialization; condition; update) {
         }
         */
        for (int i = 1; i <= 5; i++) {
            System.out.println("Current value of i: " + i);
        }

        int[] numbers = {10, 20, 30, 40, 50};

        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            sum += numbers[i];
        }

        System.out.println("The sum of the array elements is: " + sum);

        
    }
}
