/*
How to Convert a String to Lowercase in Java
Please Subscribe to Asim Code
https://youtu.be/8yfBxZvhLZo
*/
public class ToLowerCase {
    public static void main(String[] args) {
        String text = "HELLO WORLD";
        StringBuffer result = new StringBuffer();
        for (int i = 0; i < text.length(); i++) {
            if ((text.charAt(i) > 'A') && (text.charAt(i) < 'Z'))
                result.append((char) (text.charAt(i) + 32));
            else
                result.append((char) (text.charAt(i)));
        }

        System.out.println(result.toString());
    }
}
