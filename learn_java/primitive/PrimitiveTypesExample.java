/*
 +------------+------------+--------------------------------------------+
 | Data Type  | Size       | Range                                      |
 +------------+------------+--------------------------------------------+
 | byte       | 1 byte     | -128 to 127                                |
 +------------+------------+--------------------------------------------+
 | short      | 2 bytes    | -32,768 to 32,767                          |
 +------------+------------+--------------------------------------------+
 | int        | 4 bytes    | -2,147,483,648 to 2,147,483,647            |
 +------------+------------+--------------------------------------------+
 | long       | 8 bytes    | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
 +------------+------------+--------------------------------------------+
 | float      | 4 bytes    | Approx. 3.4  10^38 (7 digits precision)  |
 +------------+------------+--------------------------------------------+
 | double     | 8 bytes    | Approx. 1.8  10^308 (15 digits precision)|
 +------------+------------+--------------------------------------------+
 | char       | 2 bytes    | 0 to 65,535 (Unicode characters)           |
 +------------+------------+--------------------------------------------+
 | boolean    | 1 bit      | true or false                             |
 +------------+------------+--------------------------------------------+ 
*/
public class PrimitiveTypesExample {
    
    public static void main(String[] args) {
        byte myByte = 100;
        System.out.println("Byte value: " + myByte);
        short myShort = 2000;
        System.out.println("Short value: " + myShort);
        int myInt = 50000;
        System.out.println("Int value: " + myInt);
        long myLong = 123456789L;
        System.out.println("Long value: " + myLong);
        float myFloat = 5.99f;
        System.out.println("Float value: " + myFloat);
        double myDouble = 19.99;
        System.out.println("Double value: " + myDouble);
        char myChar = 'A';
        System.out.println("Char value: " + myChar);
        boolean myBool = true; // A boolean value (either true or false)
        System.out.println("Boolean value: " + myBool);
    }
}
