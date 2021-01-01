
public class UnsignedNumbers {
    public static void main(String[] args) {
    int signed = Integer.compare(Integer.MIN_VALUE,Integer.MAX_VALUE);
    int unsigned = Integer.compareUnsigned(Integer.MIN_VALUE,Integer.MAX_VALUE);
    System.out.println("Signed Result : "+signed);
    System.out.println("Unsigned Result : "+unsigned);

    }

}