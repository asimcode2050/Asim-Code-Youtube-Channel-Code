import java.util.*;
public class DequeDemo {
    public static void main(String[] args) {
        Deque<String> dq = new LinkedList<>();
        dq.add("3");
        dq.addFirst("2");
        dq.addLast("1");
        String first = dq.element();
        System.out.println(first);
        String last = dq.getLast();
        System.out.println(last);
        String lastRemove = dq.removeLast();
        System.out.println(lastRemove);

    }

}