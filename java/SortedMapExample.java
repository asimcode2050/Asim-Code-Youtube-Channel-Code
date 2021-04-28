// https://youtu.be/Gs_NVAXS2D4
import java.util.*;
public class SortedMapExample{
    
        public static void main(String[] args) {
          TreeMap tm = new TreeMap();
          tm.put("robert", Double.valueOf(99.50));
          tm.put("mike", Double.valueOf(130.80));
          tm.put("john", Double.valueOf(550.25));
          
          
          Set set = tm.entrySet();
          Iterator it = set.iterator();
          while(it.hasNext()){
              Map.Entry me = (Map.Entry)it.next();
              System.out.print(me.getKey() + " : ");
              System.out.println(me.getValue());

                }
            System.out.println();



    }
}
