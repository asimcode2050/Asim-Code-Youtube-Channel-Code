import java.lang.management.ManagementFactory;

public class GetProcID{
    public static long getPid(){
        final String jvmName = ManagementFactory.getRuntimeMXBean().getName();
        final int index = jvmName.indexOf('@');
        if(index < 1)
            return -1;
        try{
            return Long.parseLong(jvmName.substring(0,index));
        }catch(NumberFormatException nfe){
            return -1;
        }
    }

   public static void main(String[] args) {
    System.out.println(GetProcID.getPid());
   } 
}
