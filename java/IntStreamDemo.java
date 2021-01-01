import java.util.*;
import java.util.stream.*;
public class IntStreamDemo {
    public static void main(String[] args) {
        int[] numbers = {2,5,6,7,8,3,11};
        IntStream.of(numbers).forEach(number ->System.out.printf("%d ",number));
        System.out.println();
        System.out.printf("%n Count  =  %d%n",IntStream.of(numbers).count());
        System.out.printf("Min =  %d%n", IntStream.of(numbers).min().getAsInt());
        System.out.printf("Max =  %d%n", IntStream.of(numbers).max().getAsInt());
        System.out.printf("Sum =  %d%n", IntStream.of(numbers).sum());
        
    }

}