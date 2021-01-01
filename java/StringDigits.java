
public class StringDigits {
    public static boolean checkforDigits(String s){
        if(s == null || s.isBlank())
    {
           return false;
    }
    for(int x =0; x< s.length() ;x++){
        if(!Character.isDigit(s.charAt(x))){
            return false;
        }
    }
    
return true;
    }
    public static void main(String[] args) {
        String digitString = "123";
        String textString ="abc";
boolean result = checkforDigits(digitString);
System.out.println(result);

 result = checkforDigits(textString);
System.out.println(result);

}
}