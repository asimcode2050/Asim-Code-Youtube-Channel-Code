import java.util.Scanner;
public class PowerOfTwo{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Please enter the number :");
        int n = sc.nextInt();
        boolean result = isPowerOfTwo(n);
        if(result){
            System.out.println("This number is a power of two");
        }
        else{
            System.out.println("This number is not power of two");
        }
        sc.close();
    }
public static boolean isPowerOfTwo(int numb){
    return numb !=0 && ((numb & (numb-1))==0);
}
}
