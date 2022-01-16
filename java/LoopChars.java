/*
How to Process a String One Character at a Time in Java
Please Subscribe to Asim Code.
YouTube Channel: Asim Code
https://youtu.be/LAkTOtyQSng
*/
public class LoopChars {

  public static void main(String[] args) {
    String text = "Hello World";
    System.out.println("Using toCharArray:");
    for (char c : text.toCharArray()) {
      System.out.println(c);
    }

    System.out.println("By using Streams: ");
    text.chars().forEach(c -> System.out.println((char) c));
  }
}
