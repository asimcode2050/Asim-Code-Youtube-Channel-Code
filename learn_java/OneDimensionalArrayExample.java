import java.util.Arrays;

public class OneDimensionalArrayExample {

    public static void main(String[] args) {
        int[] numbers = new int[5];
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        numbers[3] = 40;
        numbers[4] = 50;
        System.out.println("The numbers in the array are: " + Arrays.toString(numbers));
        System.out.println("\nUsing a for loop to print each element:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("Element at index " + i + ": " + numbers[i]);
        }

        int thirdElement = numbers[2];
        System.out.println("\nThe third element (index 2) is: " + thirdElement);
        numbers[2] = 60;
        System.out.println("\nAfter modification, the third element (index 2) is: " + numbers[2]);
        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            sum += numbers[i];
        }
        System.out.println("\nThe sum of all elements is: " + sum);

        int max = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > max) {
                max = numbers[i]; 
            }
        }
        System.out.println("\nThe maximum value in the array is: " + max);

        double average = (double) sum / numbers.length;
        System.out.println("\nThe average value of the elements is: " + average);
        Arrays.sort(numbers); 
        System.out.println("\nAfter sorting, the array is: " + Arrays.toString(numbers));
        int index = Arrays.binarySearch(numbers, 60);
        System.out.println("\nElement 60 is found at index: " + index);
        int[] copyOfNumbers = Arrays.copyOf(numbers, numbers.length); 
        System.out.println("\nThe copied array is: " + Arrays.toString(copyOfNumbers));
        boolean areEqual = Arrays.equals(numbers, copyOfNumbers);
        System.out.println("\nAre the original and copied arrays equal? " + areEqual);
    }
}
