import java.util.*;
public class IteratorExample {
    public static void main(String[] args) { 
        List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        Iterator<Integer> iterator = numbers.iterator();
        while (iterator.hasNext()) {
            Integer number = iterator.next();
            System.out.println(number); 
        }

        iterator = numbers.iterator();
        while (iterator.hasNext()) {
            Integer number = iterator.next();
            if (number == 3) {
                iterator.remove();
            }
        }

        System.out.println("Modified List: " + numbers);
    }
}
