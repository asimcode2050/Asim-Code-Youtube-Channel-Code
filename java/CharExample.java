// https://youtu.be/13j2I28qxt4
public class CharExample{
    public static void main(String[] args) {
        char myChar1 = 'a';
        char myChar2= '3';
        char myChar3= 65; // 'A'
        char singleQ = '\'';
        char tab = '\t';
        char backspace = '\b';
        char newline = '\n';
        char carriageReturn ='\r';
        char formfeed = '\f';
        char doubleQ = '\"';
        char backslash = '\\';
        char heartSymb = '\u2764';
        System.out.println(Character.toString(heartSymb));
        for(int x = 0; x<=26;x++){
            char c = (char) ('a'+x);
            System.out.println(c);
         }


    }
}
