/*
Use of static variables in counting the number of instances in JAVA
Please like and subscribe my Channel
https://youtu.be/dSBAOaNCxO8
*/
public class Counter {
    private static int count;

    public Counter() {
        count++;
    }

    public static void main(String[] args) {
        Counter c1 = new Counter();
        Counter c2 = new Counter();
        Counter c3 = new Counter();
        Counter c4 = new Counter();
        Counter c5 = new Counter();

        System.out.println(count);

    }
}
