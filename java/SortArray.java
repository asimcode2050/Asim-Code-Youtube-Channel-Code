import java.util.*;
public class SortArray {
    public static void sortArrayAsc(String[] str ) {
        Arrays.sort(str,Comparator.comparingInt(String::length));
        System.out.println(Arrays.toString(str));
        
    }
    public static void sortArrayD(String[] str ) {
        Arrays.sort(str,Comparator.comparingInt(String::length).reversed());
        System.out.println(Arrays.toString(str));
        
    }
    public static void main(String[] args) {
        String[] myStr = {"ab","a","abcd","ef","b"};
        sortArrayAsc(myStr);
        sortArrayD(myStr);
    }
}