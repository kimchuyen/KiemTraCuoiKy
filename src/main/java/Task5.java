
/**
 Create a set of numbers (Set<Integer>) and add 10 different numbers to it.

 Remove from the set all numbers greater than 10 .

 Requirements:
 •Create createSet() method to create and return a HashSet containing 10 different numbers.
 •Create removeAllNumbersGreaterThan10() method to remove from the set all numbers greater than 10.
 •Write unit test for the removeAllNumbersGreaterThan10() method
 */
import java.util.HashSet;
import java.util.Random;
import java.util.Set;
public class Task5 {
    public Set<Integer> createSet() {
        Random rand = new Random();
        Set<Integer> set = new HashSet<>();
        while (set.size() < 10) {
            set.add(rand.nextInt(20));
        }
        return set;
    }
    public void removeAllNumbersGreaterThan10(Set<Integer> set) {
        set.removeIf(num -> num > 10);
    }
    public static void main(String[] args) {
        Task5 t5 = new Task5();
        Set<Integer> so = t5.createSet();
        System.out.println("Chuỗi ban đầu:");
        for (int e : so) {
            System.out.print(e+"  ");
        }
        t5.removeAllNumbersGreaterThan10(so);
        System.out.println("chuoi sau khi remove:");
        for (int e : so) {
            System.out.print(e+"  ");
        }
    }
}
