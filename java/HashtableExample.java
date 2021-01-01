import java.util.*;
public class HashtableExample {
public static void main(String[] args) {
   Hashtable<Integer, String> ht = new Hashtable<Integer,String>();
   ht.put(1,"Java");
   ht.put(2,"Python");
   ht.put(3,"C++");
   System.out.println(ht);
    ht.remove(2);
   System.out.println(ht);

}
}