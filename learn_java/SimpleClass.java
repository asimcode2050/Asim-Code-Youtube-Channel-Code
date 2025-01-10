public class SimpleClass { 
    private int number;
    private String text;
    public SimpleClass() {
        this.number = 0;
        this.text = ""; 
    }

    public void printGreeting() {
        System.out.println("Hello, welcome to Java!");
    }

    public void setNumber(int newNumber) {
        this.number = newNumber;
    }

    public int getNumber() {
        return this.number;
    }

    public void setText(String newText) {
        this.text = newText;
    }

    public String getText() {
        return this.text;
    }

    public static void main(String[] args) {
        SimpleClass myObject = new SimpleClass();
        myObject.printGreeting();
        myObject.setNumber(25);
        System.out.println("Current number: " + myObject.getNumber());
        myObject.setText("This is a sample text.");
        System.out.println("Current text: " + myObject.getText());
    }
}
