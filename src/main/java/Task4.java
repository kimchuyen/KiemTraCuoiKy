import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;
/**
 * 1. Use the keyboard to enter the number N.
 *
 * 2. Use the keyboard to enter N integers and put them in a list: the getIntegerList method.
 *
 * 3. Find the minimum among the list items: the getMinimum method.
 *
 * Requirements:
 * •The program should read values from the keyboard.
 * •The getIntegerList() method should read the number N from the keyboard and then return a list of N elements, which has been filled with numbers read from the keyboard.
 * •The getMinimum() method must return the minimum among the list items.
 * •The main() method should call the getIntegerList() method.
 * •The main() method should call the getMinimum() method.
 */
public class Task4 {
    public List<Integer> getIntegerList() {
        Scanner sc = new Scanner(System.in);
        int n;
        n = sc.nextInt();
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(sc.nextInt());
        }
        return list;
    }
    public int getMinimum(List<Integer> list) {
        if (list.isEmpty()) return 0;
        int min = list.get(0);
        for (int num : list) {
            min = Math.min(min, num);
        }
        return min;
    }
    public static void main(String[] args) {
        Task4 t4 = new Task4();
        List<Integer> list = t4.getIntegerList();
        System.out.println(t4.getMinimum(list));
    }
}
