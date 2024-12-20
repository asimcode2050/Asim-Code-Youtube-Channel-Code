import java.util.HashSet;
public class HashSetExample {
    public static void main(String[] args) {
        HashSet<Integer> numbersSet = new HashSet<>();
        numbersSet.add(10);
        numbersSet.add(20);
        numbersSet.add(10);
        numbersSet.add(30);
        System.out.println("HashSet contains: " + numbersSet);
        boolean contains10 = numbersSet.contains(10);
        System.out.println("Contains 10: " + contains10);
        numbersSet.remove(20);
        System.out.println("After removing 20: " + numbersSet);
        boolean isEmpty = numbersSet.isEmpty();
        System.out.println("Is the HashSet empty? " + isEmpty);
        int setSize = numbersSet.size();
        System.out.println("Size of HashSet: " + setSize);
    }
}
