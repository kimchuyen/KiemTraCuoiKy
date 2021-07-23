import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

/**
 Write a program that will read a string containing numbers from the keyboard, each number is separated by comma ","

 Display to screen the whole list of number in decreasing sorting order.

 If string contains alphabetical character instead of a number, then the method should catch an exception and display to screen the message "String contains character which cannot be converted into number".

 Requirements:
 •The program must read a string of numbers from the keyboard.
 •The readData method is to read numbers from the keyboard
 •The readData method must contain a try-catch block.
 •The sortNumber method is to sorting list of numbers into decreasing order.
 •The readData method calls sortNumber method.
 •If the user enters alphabetical character rather than a number, the program should display message "String contains character which cannot be converted into number".
 */

public class Task1 {

    public List<Integer> readData() {
        try {
            Scanner sc = new Scanner(System.in);
            System.out.println("nhap phan tu chuoi");
            String input = sc.nextLine();
            String[] Strings = input.split(",");
            List<Integer> numbers = new ArrayList<>();
            for (String numStr : Strings) {
                int number = Integer.parseInt(numStr);
                numbers.add(number);
            }
            sortNumberList(numbers);
            for (int number : numbers) {
                System.out.println(number);
            }
        } catch (Exception e) {
            System.out.println("String contains character which cannot be converted into number");
        }
        return null;
    }
    public List<Integer> sortNumberList(List<Integer> list) {
        list.sort(Collections.reverseOrder());
        return null;
    }
    public static void main(String[] args) {
       Task1 t1 = new Task1();
       t1.readData();
    }
}




