
public class MulLong {
    public static void main(String[] args) {
        int a = 5000;
        int b = 10;
        long result = Math.multiplyFull(a,b);
        System.out.println("Result = "+result);
        a = Integer.MAX_VALUE;
        b = Integer.MAX_VALUE;
         result = Math.multiplyFull(a,b);
        System.out.println("Result Of Max_Value  = "+result);
        long x = Long.MAX_VALUE;
        long y = Long.MAX_VALUE;
        long prod = Math.multiplyHigh(x,y);
        System.out.println("Result Of Long Max_Value  = "+prod);

    }

}