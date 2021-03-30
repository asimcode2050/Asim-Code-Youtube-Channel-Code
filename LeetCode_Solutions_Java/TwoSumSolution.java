// https://www.youtube.com/watch?v=_N9kQ4moV5w&ab_channel=AsimCode
import java.util.*;
public class TwoSumSolution{
    public static void main(String[] args) {
        int[] myArr = new int[]{2,7,11,15};
        int target = 9;
        TwoSumSolution ts = new TwoSumSolution();
        System.out.println(Arrays.toString(ts.twoSum(myArr,target)));
        
    }
    public int[] twoSum(int[] numbers, int target){
        Map<Integer, Integer>map = new HashMap<>();
        for(int i=0;i<numbers.length;i++){
            int x = numbers[i];
            if(map.containsKey(target - x)){
                return new int[]{ map.get(target-x), i
                };
            }
            map.put(x,i);

        }
        throw new IllegalArgumentException("No solution!");
    }

}
