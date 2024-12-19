import java.util.ArrayList;
public class Main {

    public static void main(String[] args) {

        ArrayList<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");

        System.out.println("Fruits List: " + fruits);
        String firstFruit = fruits.get(0);
        System.out.println("First fruit: " + firstFruit);
        fruits.remove("Banana");
        System.out.println("Updated Fruits List (after removal): " + fruits);
        System.out.println("Size of the ArrayList: " + fruits.size());
        if (fruits.contains("Orange")) {
            System.out.println("Orange is in the list!");
        } else {
            System.out.println("Orange is not in the list.");
        }

        fruits.clear();

        System.out.println("Fruits List after clearing: " + fruits);
    }
}
