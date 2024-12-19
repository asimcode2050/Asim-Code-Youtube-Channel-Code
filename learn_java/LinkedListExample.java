import java.util.LinkedList;
public class LinkedListExample {
    public static void main(String[] args) {
        LinkedList<String> fruits = new LinkedList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");
        fruits.addFirst("Mango");
        fruits.addLast("Pineapple");
        System.out.println("Fruits LinkedList: " + fruits);
        System.out.println("First element: " + fruits.getFirst());
        System.out.println("Last element: " + fruits.getLast());
        fruits.removeFirst();
        fruits.removeLast();
        System.out.println("After removal: " + fruits);
        System.out.println("Iterating through the list:");
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}
