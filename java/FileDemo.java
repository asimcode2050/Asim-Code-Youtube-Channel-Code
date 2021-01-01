import java.io.*;
import java.nio.file.*;
import java.io.*;
import java.nio.charset.*;

public class FileDemo{
    public static void main(String[] args) {
        writeToFile();
        readFromFile();    
    }
    private static void writeToFile(){
        try{
            File file = new File("helloworld.txt");
            if(!file.isFile()){
                file.createNewFile();
            }
            Files.writeString(file.toPath(),"Hello World",Charset.defaultCharset(),StandardOpenOption.WRITE);


        }catch(IOException e){
            e.printStackTrace();
        }
    }
        private static void readFromFile(){
            try{
                File fileRead =  new File("helloworld.txt");
                String data = Files.readString(fileRead.toPath(),Charset.defaultCharset());
                System.out.println(data);

            }catch(IOException e){
                e.printStackTrace();
            }
        }
    }
