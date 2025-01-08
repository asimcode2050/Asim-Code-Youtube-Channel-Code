public class TypeConversionExample {

    public static void main(String[] args) {
        int intValue = 100;
        long longValue = intValue;  // Java automatically converts int to long
        System.out.println("Implicit Casting (int to long): " + longValue);  // Output: 100
        float floatValue = intValue;  // int is implicitly cast to float
        System.out.println("Implicit Casting (int to float): " + floatValue);  // Output: 100.0
        double doubleValue = 9.78;  // This is a double data type
        int narrowedIntValue = (int) doubleValue;  // Manually casting double to int
        System.out.println("Explicit Casting (double to int): " + narrowedIntValue);  // Output: 9
        long largeLongValue = 10000000000L;  // A large long value
        int narrowedIntFromLong = (int) largeLongValue;  // Casting long to int manually
        System.out.println("Explicit Casting (long to int): " + narrowedIntFromLong);  // Output: -1610612736 (overflow)
        char charValue = 'A';  // A character
        int charToInt = charValue;  // Implicit conversion from char to int (ASCII value)
        System.out.println("Implicit Casting (char to int): " + charToInt);  // Output: 65 (ASCII of 'A')
        int num = 123;
        String strValue = Integer.toString(num);
        System.out.println("int to String Conversion: " + strValue);  // Output: "123"
        String stringNum = "456";
        int parsedInt = Integer.parseInt(stringNum);
        System.out.println("String to int Conversion: " + parsedInt);  // Output: 456
    }
}
