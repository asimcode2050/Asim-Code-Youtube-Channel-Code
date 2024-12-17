public class Student {  

    private String name;
    private int age;
    private double[] grades; 
    private int gradeCount;
    public Student(String name, int age, int numberOfGrades) {
        this.name = name;
        this.age = age;
        this.grades = new double[numberOfGrades];
        this.gradeCount = 0;
    }

    public void addGrade(double grade) {
        if (gradeCount < grades.length) {
            grades[gradeCount] = grade;
            gradeCount++;
            System.out.println("Grade " + grade + " added.");
        } else {
            System.out.println("No more grades can be added.");
        }
    }

    public double calculateAverageGrade() {
        if (gradeCount == 0) {
            System.out.println("No grades available to calculate the average.");
            return 0;
        }
        double sum = 0;
        for (int i = 0; i < gradeCount; i++) {
            sum += grades[i];
        }
        return sum / gradeCount;
    }

    public void displayDetails() {
        System.out.println("Student Name: " + name);
        System.out.println("Student Age: " + age);
        System.out.println("Grades: ");
        for (int i = 0; i < gradeCount; i++) {
            System.out.println(grades[i]);
        }
    }

    public static void main(String[] args) {
        Student student = new Student("Alice", 20, 5);

        student.addGrade(85.5);
        student.addGrade(92.0);
        student.addGrade(78.3);
        student.addGrade(88.8);
        student.addGrade(91.5);
        student.addGrade(75.0);
        student.displayDetails();

        double average = student.calculateAverageGrade();
        System.out.println("Average grade: " + average);
    }
}
