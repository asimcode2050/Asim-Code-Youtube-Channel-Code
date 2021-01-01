public class RevInt{
    public static void main(String[] args) {
        System.out.println(RevInt.reverse(123));
    }
   public static int reverse(int number){
       int result = 0;
       while(number > 0){
           result = result * 10 + number %10;
           number = number /10;
       }
       return result;
   }
}