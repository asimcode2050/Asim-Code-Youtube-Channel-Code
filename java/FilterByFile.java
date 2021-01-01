import java.nio.file.*;
import java.io.*;
public class FilterByFile{
    
    
    public static void main(String[] args) throws IOException {
        Path dir = Paths.get("/home/asim");
        PathMatcher fileMatcher = FileSystems.getDefault().getPathMatcher("regex:.*(?i:jpg|jpeg|png|gif|bmp|jpe|jfif)");
        try(DirectoryStream<Path> stream = Files.newDirectoryStream(dir, entry-> fileMatcher.matches(entry.getFileName()))){
            for(Path p : stream){
                System.out.println(p.getFileName());


            }

        }
        
    }
}