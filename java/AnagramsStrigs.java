import java.util.*;
public class AnagramsStrigs {
    public static boolean checkAnagram(String str1, String str2){
        if(str1 == null || str2 == null || str1.isBlank() || str2.isBlank())
    {
        return false;
    }
    char[] cArr1 = str1.replaceAll("\\s","").toLowerCase().toCharArray();
    char[] cArr2 = str2.replaceAll("\\s","").toLowerCase().toCharArray();
       if(cArr1.length != cArr2.length){
           return false;
       } 
    Arrays.sort(cArr1);
    Arrays.sort(cArr2);
    return Arrays.equals(cArr1,cArr2);   
}
    public static void main(String[] args) {
        String s1 = "FRIED";
        String s2 = "FIRED";

        boolean result = checkAnagram(s1,s2);
        System.out.println("Strings are Anagrams : "+result);
    }

}