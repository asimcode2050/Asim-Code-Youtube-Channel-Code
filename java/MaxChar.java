import java.util.*;
public class MaxChar {
    public static void main(String[] args) {
        String str ="abcabbdab";
        Map<Character, Integer> map = new HashMap<>();
        char[] chArr = str.toCharArray();
        for(int i=0; i < chArr.length;i++){
            char c = chArr[i];
            if(!Character.isWhitespace(c)){
               Integer val =  map.get(c);
               if(val == null){
                   map.put(c,1);
               }
               else{
                   map.put(c,++val);
               }
            }
        }
        int maxValue = Collections.max(map.values());
        char maxChar = Character.MIN_VALUE;
        for(Map.Entry<Character, Integer> e : map.entrySet()){
            if(e.getValue() == maxValue){
                maxChar = e.getKey();
            }

        }

        System.out.println("Max Char: "+maxChar);
        System.out.println("Max Value: "+maxValue);

    }

}