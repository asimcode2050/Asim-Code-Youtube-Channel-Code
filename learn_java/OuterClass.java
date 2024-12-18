public class OuterClass {
    private int outerVariable = 10;
    public OuterClass() {
        System.out.println("OuterClass constructor called");
    }

    public void display() {
        InnerClass innerObj = new InnerClass();
        innerObj.displayInner();
    }

    class InnerClass {
        private int innerVariable = 5;
        public InnerClass() {
            System.out.println("InnerClass constructor called");
        }

        public void displayInner() {
            System.out.println("Outer variable: " + outerVariable);
            System.out.println("Inner variable: " + innerVariable);
        }
    }

    public static void main(String[] args) {
        OuterClass outerObj = new OuterClass();

        outerObj.display();
    }
}
