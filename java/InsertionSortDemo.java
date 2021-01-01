import java.util.*;
public class InsertionSortDemo {
   public static void main(String[] args) {
       int[] arr= {50,10,2,60,90,3,100};
       System.out.println("Before Insertion Sort");
       System.out.println(Arrays.toString(arr));
       int size = arr.length;
       for(int i=0;i<size;++i){
           for(int y=i;y>0;--y){
               if(arr[y-1]>arr[y]){
                   int temp = arr[y];
                   arr[y] = arr[y-1];
                   arr[y-1] = temp;
               }
           }
       }
       System.out.println("After Insertion Sort");
       System.out.println(Arrays.toString(arr)); 
    }
    
}