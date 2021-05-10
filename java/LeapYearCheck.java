/*
Java program that lets the user enter a year and checks whether it is a leap
year. Learn to Code Subscribe to Asim Code. 
https://youtu.be/nfWlolz8EE0
*/
import java.util.Scanner;
public class LeapYearCheck{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Please enter a year: ");
        int year = input.nextInt();
        boolean is_leap_year = (year % 4 == 0 && year % 100 !=0) || (year % 400 == 0);
        System.out.println(year + " is a Leap Year? "+is_leap_year);

    }
}
