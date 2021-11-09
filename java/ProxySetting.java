/*
YouTube Channel : Asim Code
Setting Up Proxy Connection In Java
https://youtu.be/SzhbnGOSgbM
*/
import java.io.IOException;
import java.net.ProxySelector;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.InetSocketAddress;

public class ProxySetting {
    public static void main(String[] args) throws IOException, InterruptedException
     {
         HttpClient http_client = HttpClient.newBuilder().
         proxy(ProxySelector.of(new InetSocketAddress("proxyhost",80))).build();

         HttpRequest http_request = HttpRequest.newBuilder()
         .uri(URI.create("https://github.com")).build();

         HttpResponse<String> response = http_client.send(http_request,HttpResponse.BodyHandlers.ofString());
         System.out.println("Status Code : "+response.statusCode());
         System.out.println("\n Body: "+response.body());

    }
}
