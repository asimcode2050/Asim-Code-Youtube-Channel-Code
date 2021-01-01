import java.util.*;
import java.util.stream.*;
public class AverageDemo{
    public static double compute_avg(int[] arr){
        return sum(arr)/arr.length;
    }
public static double sum(int[] myArr){
    double sum =0;
    for(int x : myArr){
        sum += x;
    }
    return sum;
}
    public static void main(String[] args) {
      int[] intArray = new int[] {1,2,3,4,5,6,7,8};
       double avg =  AverageDemo.compute_avg(intArray);      
       System.out.println("Array Average: "+avg);
       
    }
}