import java.io.EOFException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.stream.Stream;
public class EmptyFile{
    public static void main(String[] args) {
        try(var fInputS = new FileReader("emptyfile.txt");
            var buffReader = new BufferedReader(fInputS)){
                String text = buffReader.readLine();
                if(text!=null){
                   // System.out.println(text);
                   System.out.println("File is not Empty!");

                }
                else{
                    throw new EOFException("File is Empty");
                }

            }
            catch(FileNotFoundException | EOFException e){
                e.printStackTrace();
            }
            catch(IOException io){
                io.printStackTrace();
            }
    }
}
