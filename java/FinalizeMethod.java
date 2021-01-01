
public class FinalizeMethod {
    protected void finalize() throws IOException{
    if((fd != null) && (fd != FileDescriptor.in)){
        close();
        
    }


    }


}