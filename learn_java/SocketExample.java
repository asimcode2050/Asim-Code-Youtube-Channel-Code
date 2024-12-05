
import java.net.*;
import java.io.*;

public class SocketExample {

    public static void tcpServer() {
        try {
            ServerSocket serverSocket = new ServerSocket(1234);
            System.out.println("TCP Server is waiting for client connection...");

            Socket clientSocket = serverSocket.accept();
            System.out.println("Client connected!"); // Confirmation message that the client is connected.
            BufferedReader inputReader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            String message = inputReader.readLine();
            System.out.println("Message from client: " + message); // Display the clients message.
            PrintWriter outputWriter = new PrintWriter(clientSocket.getOutputStream(), true);
            outputWriter.println("Hello, client! This is the server.");
            clientSocket.close();
            serverSocket.close();
        } catch (IOException e) {
            System.out.println("Error in TCP server: " + e.getMessage()); // Handling any I/O errors.
        }
    }

    public static void tcpClient() {
        try {
            Socket socket = new Socket("localhost", 1234
            );
            PrintWriter outputWriter = new PrintWriter(socket.getOutputStream(), true);
            outputWriter.println(
                    "Hello, server! This is the client."
            );
            BufferedReader inputReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String response = inputReader.readLine();
            System.out.println("Response from server: " + response);
            socket.close();
        } catch (IOException e) {
            System.out.println("Error in TCP client: " + e.getMessage());
        }
    }

    public static void udpServer() {
        try {
            DatagramSocket udpSocket = new DatagramSocket(1234);
            System.out.println("UDP Server is waiting for client message...");
            byte[] buffer = new byte[1024];
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            udpSocket.receive(packet);
            String clientMessage = new String(packet.getData(), 0, packet.getLength());
            System.out.println("Message from client: " + clientMessage);
            String responseMessage = "Hello, client! This is the UDP server.";
            byte[] responseData = responseMessage.getBytes();
            DatagramPacket responsePacket = new DatagramPacket(responseData, responseData.length, packet.getAddress(), packet.getPort());
            udpSocket.send(responsePacket);
            udpSocket.close();
        } catch (IOException e) {
            System.out.println("Error in UDP server: " + e.getMessage());
        }
    }

    public static void udpClient() {

        try {
            DatagramSocket udpSocket = new DatagramSocket();
            String message
                    = "Hello, server! This is the UDP client.";
            byte[] messageData = message.getBytes();
            InetAddress serverAddress = InetAddress.getByName("localhost");
            DatagramPacket packet = new DatagramPacket(messageData, messageData.length, serverAddress, 1234);
            udpSocket.send(packet);
            byte[] buffer = new byte[1024];
            DatagramPacket responsePacket = new DatagramPacket(buffer, buffer.length);
            udpSocket.receive(
                    responsePacket
            );
            String responseMessage = new String(responsePacket.getData(), 0, responsePacket.getLength());
            System.out.println("Response from server: " + responseMessage);
            udpSocket.close();
        } catch (IOException e) {
            System.out.println("Error in UDP client: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        Thread tcpServerThread = new Thread(() -> tcpServer());
        tcpServerThread.start();
        Thread udpServerThread = new Thread(() -> udpServer());
        udpServerThread.start();

        try {
            Thread.sleep(1000);
            tcpClient();
            udpClient();
        } catch (InterruptedException e) {
            System.out.println("Error in main thread: " + e.getMessage());
        }
    }
}
