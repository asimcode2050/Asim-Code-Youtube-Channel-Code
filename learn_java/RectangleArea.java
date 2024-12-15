
public class RectangleArea {

    public static void main(String[] args) {
        double width = 5.0;
        double height = 3.0;
        double area = calculateArea(width, height);
        System.out.println("The area of the rectangle is: " + area + " square meters");
    }

    public static double calculateArea(double width, double height) {
        return width * height;
    }
}
