import java.util.*;
public class Pyramid {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int j =0, sum =0;
        for(int i=1;i<=n;++i,j=0){
            for(int k=1; k<=n-i ;++k){
                System.out.print(" ");
            }
            while(j!=2*i -1){
                System.out.print("* ");
                sum = sum+1;
                ++j;
            }
            System.out.println();

        }
                   System.out.println(sum);

    }
    
}