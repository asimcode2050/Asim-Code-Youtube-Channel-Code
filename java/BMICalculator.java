// https://youtu.be/88zBUQUMUiA
import java.util.Scanner;
public class BMICalculator{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Please enter weight in pounds: ");
        double weight = input.nextDouble();
        System.out.print("Please enter height in inches: ");
        double height = input.nextDouble();
        final double kilo_per_pound = 0.45359237;
        final double meters_per_inch = 0.0254;
        double weight_in_kilo = weight * kilo_per_pound;
        double height_in_meters = height * meters_per_inch;
        double bmi = weight_in_kilo / (height_in_meters * height_in_meters);
        System.out.println("BMI is : "+ bmi);
        if(bmi < 18.5)
            System.out.println("Underweight");
        else if (bmi < 25)
            System.out.println("Normal");
        else if (bmi < 30)
            System.out.println("Overweight");
        else
            System.out.println("Obese");

        
    }

}
