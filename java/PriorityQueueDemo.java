import java.util.*;
public class PriorityQueueDemo {
    public static void main(String[] args) {
        PriorityQueue<Integer> q = new PriorityQueue<Integer>();
        q.addAll(Arrays.asList(10,9,8,4,12,3,2,1));
        System.out.println(q);
        q.remove();
        System.out.println(q);
    }

}