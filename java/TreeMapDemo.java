import java.util.*;
public class TreeMapDemo {
    public static void main(String[] args) {
        TreeMap tMap = new TreeMap();
        tMap.put("Tom",Integer.valueOf(100));
        tMap.put("Mike",Integer.valueOf(500));
        tMap.put("Jack",Integer.valueOf(300));
        Set s = tMap.entrySet();
        Iterator it = s.iterator();
        while(it.hasNext()){
            Map.Entry me = (Map.Entry)it.next();
            System.out.print(me.getKey() + ":");
            System.out.println(me.getValue() );
        }
int val = ((Integer)tMap.get("Tom")).intValue();
tMap.put("Tom" ,Integer.valueOf(val+100));
System.out.println("Tom Value = "+ tMap.get("Tom"));




    }

    
    }

