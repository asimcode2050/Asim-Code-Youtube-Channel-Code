
public class TestClone implements Clonable{
    int i;
    Strng str;
    float[] f;
    Date d;
    public TestClone clone(){
        try{
        TestClone tc = new testClone();
        tc.i = this.i;
        tc.str = this.str;
        if(this.f !=null){
            tc.f = this.f.clone;
        }
        if(thiz.d != null){
            tc.d = this.d.clone();
        }
        return tc;
    }catch(CloneNotSupportedException ex){
        
    }

    }
}