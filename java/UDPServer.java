import java.io.*;
import java.net.*;
public class UDPServer {
    public static void main(String[] args) throws IOException{
        DatagramSocket server = new DatagramSocket(4160);
        byte[] buf = new byte[256];
        DatagramPacket packet = new DatagramPacket(buf,buf.length);
        server.receive(packet);
        String response = new String(packet.getData());
        System.out.println("Reponse Data : "+response);
        server.close();
    }
}