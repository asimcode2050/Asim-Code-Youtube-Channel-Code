import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.stream.*;
public class StreamDemo{
    public static void main(String[] args) {
       Stream<String> myStream = Stream.of("tom","peter","mike","robert");
       myStream.filter(s->s.contains("t"))
       .map(String::toUpperCase)
       .sorted()
       .forEach(System.out::println);
        
    }
}