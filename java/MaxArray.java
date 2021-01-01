import java.util.Arrays;
public class MaxArray{
    public static int findMax(int[] my_arr){
        int max = my_arr[0];
        for(int el : my_arr){
            max = Math.max(max,el);
        }
        return max;
    }
  public static void main(String[] args) {
      int[] intArray = new int[]{4,5,6,7,8,10,100};
        int m = MaxArray.findMax(intArray);
        System.out.println(m);
       int maxVal = Arrays.stream(intArray).max().getAsInt();
       System.out.println(maxVal);
    }

}