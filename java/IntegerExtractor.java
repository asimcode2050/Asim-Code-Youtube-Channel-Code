/*
Youtube Channel : Asim Code
How to extract all integers from the given string in Java
https://youtu.be/G9h43prT0Jw
*/
import java.util.*;
public class IntegerExtractor{
    public static void main(String[] args) {
        String str = "abc12 3ghb t5d 6s";
        List l = extractInt(str);
        l.stream().forEach(System.out.println);
        
    }
public static List<Integer> extractInt(String myStr){
    List<Integer> intList = new ArrayList<>();
    StringBuilder temp = new StringBuilder(String.valueOf(Integer.MAX_VALUE).length());

    for(int i =0; i< myStr.length();i++){
        char ch = myStr.charAt(i);
        if(Character.isDigit(ch)){
            temp.append(ch);

        }
        else{
          if(temp.length() > 0){
            intList.add(Integer.parseInt(temp.toString()));
            temp.delete(0,temp.length());
          }  
        }

    }
    return intList;

}
}
