import java.util.*;
public class EvenRand{
  public static void main(String[] args) {
     int[] rand_array = new int[10];
     for(int i=0; i<10 ;i++){
       Random random = new Random();
       int rand_number = random.nextInt(101);
       while(rand_number %2 !=0 || rand_number == 0){
         rand_number = random.nextInt(101);
       }
       rand_array[i] = rand_number;
     }
     for(int x=0;x<rand_array.length;x++){
       System.out.print(rand_array[x]+" ");
     }
      
  }
        
    
}