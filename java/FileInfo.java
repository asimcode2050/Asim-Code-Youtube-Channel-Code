/*
Java Program For Displaying File Information
YouTube Channel : Asim Code
https://youtu.be/eZPDr0BIeKQ
Please like and subscribe to my Channel
*/
import java.io.*;

public class FileInfo {
    public static void main(String[] args) {
        var myFile = new File("d:\\youtube\\java\\Entry.java");
        System.out.println("File Exists : " + myFile.exists());
        if (myFile.exists()) {
            System.out.println("Absolute Path : " + myFile.getAbsolutePath());
            System.out.println("Is Directory : " + myFile.isDirectory());
            System.out.println("Parent Path : " + myFile.getParent());

            if (myFile.isFile()) {
                System.out.println("File Size: " + myFile.length());
                System.out.println("Last Modified: " + myFile.lastModified());

            } else {
                for (File file : myFile.listFiles()) {
                    System.out.println(" " + myFile.getName());
                }
            }

        }

    }
}
