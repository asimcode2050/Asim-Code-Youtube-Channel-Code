import java.math.BigInteger;
public class BigIntConvert{
    public static void main(String[] args) {
        BigInteger bi = BigInteger.valueOf(Long.MAX_VALUE);
        long longVar = bi.longValue();
        System.out.println("Prim Long value = "+longVar);
        long longVar2 = bi.longValueExact();
        System.out.println("Prim Long value2 = "+longVar);


    }

}