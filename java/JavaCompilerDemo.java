import javax.tools.JavaCompiler;
import javax.tools.ToolProvider;
public class JavaCompilerDemo{
    public static void main(String[] args) {
        System.out.println(System.getProperty("user.dir"));
        JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
        int result = compiler.run(null,null,null,"/home/asim/HelloWorld.java");
        System.out.println("Result Code: "+result);
    }

}