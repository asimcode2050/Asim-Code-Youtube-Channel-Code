import java.util.HashMap; 
public class HashMapExample {
    public static void main(String[] args) {
        HashMap<String, Integer> studentScores = new HashMap<>();
        studentScores.put("John", 85);
        studentScores.put("Emma", 92);
        studentScores.put("Sophia", 88);
        int johnScore = studentScores.get("John");
        System.out.println("John's score: " + johnScore);
        if (studentScores.containsKey("Emma")) {
            System.out.println("Emma's score found!");
        }

        studentScores.remove("Sophia");
        if (!studentScores.containsKey("Sophia")) {  
            System.out.println("Sophia's entry has been removed!"); 
        }
        for (String key : studentScores.keySet()) {
            int score = studentScores.get(key);  
            System.out.println(key + "'s score: " + score);
        }
    }
}
