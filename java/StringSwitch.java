public class StringSwitch{
   public static final String MEDIUM = "Medium";
   public static final String HOT = "Hot";
   public static void main(String[] args) {
    String spiceLevel="Medium_Hot";
    switch(spiceLevel){
        case "Mild",MEDIUM+"_"+ HOT -> System.out.println("Please enjoy your meal");
        case HOT   -> System.out.println("Spice level is Hot");
        default -> System.out.println("Please select the spice level");
    }
   }
}
