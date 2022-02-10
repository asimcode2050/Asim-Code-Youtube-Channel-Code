/*
Socket programming for TCP in Java Server and Client Sockets
Please Subscribe to Asim Code.
YouTube Channel: Asim Code
https://youtu.be/k3Yxw93NXJ0
*/
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;

public class SimpleSocketClient {

  public static void main(String[] args) throws IOException {
    Socket socket = new Socket("localhost", 1286);
    InputStream inStream = socket.getInputStream();
    DataInputStream dis = new DataInputStream(inStream);
    String text = new String(dis.readUTF());
    System.out.println(text);
    dis.close();
    socket.close();
  }
}
