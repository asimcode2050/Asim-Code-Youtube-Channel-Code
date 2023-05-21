import java.util.Arrays;
import java.util.Comparator;
import java.util.Collections;
public class ArraySortExamples{
    public static void main(String[] args) {
     String[] myArray = {"dog","mouse","tiger","big","Bigger","JAVA"};
     Arrays.sort(myArray);
     System.out.println("Natural Order: "+Arrays.toString(myArray));
     Arrays.sort(myArray, Comparator.comparing(String::length));
     System.out.println("Length Order: "+Arrays.toString(myArray));
     Arrays.sort(myArray,Collections.reverseOrder());
     System.out.println("Reverse Natural Order: "+Arrays.toString(myArray));
     Arrays.sort(myArray,String.CASE_INSENSITIVE_ORDER);
     System.out.println("CASE INSENSITIVE ORDER: "+Arrays.toString(myArray));
     Arrays.sort(myArray,Collections.reverseOrder(String.CASE_INSENSITIVE_ORDER));
     System.out.println("Reverse CASE INSENSITIVE ORDER: "+Arrays.toString(myArray));
       }
    }
    

