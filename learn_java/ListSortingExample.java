import java.util.*;
public class ListSortingExample {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Banana");
        fruits.add("Apple");
        fruits.add("Cherry");
        fruits.add("Mango");
        fruits.add("Pineapple");
        System.out.println("Original List: " + fruits);
        Collections.sort(fruits);
        System.out.println("Sorted List (Ascending): " + fruits);
        Collections.sort(fruits, Collections.reverseOrder());
        System.out.println("Sorted List (Descending): " + fruits);
        fruits.sort(Comparator.naturalOrder());
        System.out.println("Sorted List (Ascending using List.sort): " + fruits);  // This should print: [Apple, Banana, Cherry, Mango, Pineapple]
        fruits.sort(Comparator.reverseOrder());
        System.out.println("Sorted List (Descending using List.sort): " + fruits);
    }
}
