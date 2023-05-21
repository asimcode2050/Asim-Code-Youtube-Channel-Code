public class Average{
   public static void main(String[] args) {
    System.out.println("Average Value: "+ printAvg(200,20));
    
   }
   public static int printAvg(int sum , int total){
    int avg = 0;
    try{
        avg = calculateAvg(sum, total);
        System.out.println("Average = "+ sum + " / "+ total + " = " + avg);
        return avg;
    }
    finally{
        System.out.println("Inside finally");
        return avg * 2;
    }

   }


public static int calculateAvg(int sum, int count){
    System.out.println("Computing Average");
    return sum/count;
}
}
