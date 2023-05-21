public class CharFrequency{
    public static void main(String[] args) {
       int[] freqData = new int [Character.MAX_VALUE];
       String str = "Count the frequency of each character";
       for(int i =0; i< str.length();i++){
        try{
            freqData[str.charAt(i)]++;
        } catch(StringIndexOutOfBoundsException e){
            e.printStackTrace();

        }
    }
        System.out.println("Character frequency:");
        for(int j =0; j< freqData.length;j++){
            if(freqData[j]!=0)
            System.out.println((char)j + " (code " +j+"): "+freqData[j]);

            }

        }

       }
    

