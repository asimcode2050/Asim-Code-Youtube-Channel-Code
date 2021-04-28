// https://youtu.be/pLCky7y83vA
import java.util.*;
public class MapsExample{
    final static Map<String, String> map5;
    static{
        map5 = new HashMap<String, String>();
        map5.put("a","b");
        map5.put("c","d");

    }
        public static void main(String[] args) {
            Map map = new HashMap();
            map.put("name","first");
            map.put("city","Houston");
            System.out.println(map);

            Map<String, Object> map2 = new HashMap<>();
            map2.put("name","robert");
            map2.put("city","Austin");
            System.out.println(map2);

            Map<String, Object> map3 = new HashMap<String,Object>(){{
                put("name","bill");
                put("city","boston");
            }};
            System.out.println(map3);
            Map<String, Object> map4 = new TreeMap<String,Object>();
            map4.put("name","rick");
            map4.put("city","denver");
            System.out.println(map4);



    }
}
