public class VariableScope {
    static int classVariable = 10;
    int instanceVariable;
    public VariableScope(int value) {
        this.instanceVariable = value;
    }
    public void demonstrateScope() {
        int localVariable = 5;
        System.out.println("Local Variable: " + localVariable);
        System.out.println("Instance Variable: " + instanceVariable);
        System.out.println("Class Variable: " + classVariable);
        if (localVariable > 0) {
            int blockLocalVariable = 7;
            System.out.println("Block Local Variable: " + blockLocalVariable);
        }
    }

    public static void main(String[] args) {
        VariableScope obj = new VariableScope(20);
      obj.demonstrateScope();
        System.out.println("Class Variable (Accessed directly from main): " + classVariable);
        classVariable = 15;
        System.out.println("Updated Class Variable: " + classVariable);
    }
}
