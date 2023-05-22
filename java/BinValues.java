import java.io.*;
public class BinValues{
    public static void main(String[] args) throws IOException {
        try(
            FileOutputStream fOS =  new FileOutputStream("bin.data");
            DataOutputStream dOS = new DataOutputStream(fOS)
        ){

            dOS.writeBoolean(true);
            dOS.writeChar('B');
            dOS.writeByte(Byte.MAX_VALUE);
            dOS.writeShort(Short.MIN_VALUE);
            dOS.writeInt(Integer.MAX_VALUE);
            dOS.writeLong(Long.MIN_VALUE);
            dOS.writeFloat(Float.MAX_VALUE);
            dOS.writeDouble(Math.PI);
        }
        try(
            FileInputStream fis = new FileInputStream("bin.data");
            DataInputStream dis = new DataInputStream(fis)
        ){
            System.out.println(dis.readBoolean());
            System.out.println(dis.readChar());
            System.out.println(dis.readByte());
            System.out.println(dis.readShort());
            System.out.println(dis.readInt());
            System.out.println(dis.readLong());
            System.out.println(dis.readFloat());
            System.out.println(dis.readDouble());
            int value = dis.readByte();
            System.out.println(value);
        }
        catch(FileNotFoundException fx){
            System.out.println("File not found!");
        }
        catch(EOFException eof)
        {
            System.out.println("End of input stream.");
        }
    }

}
