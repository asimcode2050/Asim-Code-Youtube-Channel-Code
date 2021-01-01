import java.io.*;
import java.net.*;
public class UDPClient{
    public static void main(String[] args) throws IOException {
       DatagramSocket client = new DatagramSocket();
       InetAddress add = InetAddress.getByName("localhost");
       String str = "Hello World";
       byte[] buf = str.getBytes();
       DatagramPacket p = new DatagramPacket(buf,buf.length,add,4160);
       client.send(p);
       client.close();


        
    }
}