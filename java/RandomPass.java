import java.util.*;
public class RandomPass{
    public static void main(String[] args) {
        String our_pass = genPass(8,16);
        System.out.println("Random password : "+our_pass);

        
    }
    static String genPass(int min , int max){
        Random random = new Random();
        String up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String low = "abcdefghijklmnopqrstuvwxyz";
        String numb = "0123456789";
        String specialChars ="!@#$%&*(){}?";
        String all = up+low+numb+specialChars;
        List<Character> lettersList = new ArrayList<Character>();
        for(char c: all.toCharArray()){
            lettersList.add(c);
        
        }
        Collections.shuffle(lettersList);
        String pass="";
        for(int i=random.nextInt(max-min)+ min;i>0;--i){
            pass +=lettersList.get(random.nextInt(lettersList.size()));
        }
        return pass;
    }
}
