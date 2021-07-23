import java.util.Scanner;

/**
     * Write a method readString that reads a string from the keyboard.
     *
     * Write a method upperCaseString to change the first letter of each word to uppercase
     *
     * Display the result on the screen.
     *
     * Example input:
     * sam i am.
     *
     * Example output:
     * Sam I Am.
     *
     * Requirements:
     * •The method readString should read a string from the keyboard.
     * •The method upperCaseString should change the first letter of each word to uppercase
     * •The main method displays the result to screen.
     */
    public class Task3 {
        String chuoi;
        public String readString()  {
            Scanner sc = new Scanner(System.in);
            System.out.println("Nhập vào chuỗi bất kỳ từ bàn phím: ");
            chuoi = sc.nextLine();
            System.out.println("chuỗi nhập là:"+chuoi );
            return null;
        }

        public String upperCaseString (String chuoi){
            chuoi = chuoi.trim();
            chuoi = chuoi.replaceAll("\\s+", " ");
            String[] array = chuoi.split(" ");
            StringBuilder output = new StringBuilder();
            for (int i = 0; i < array.length; i++) {
                String temp = String.valueOf(array[i].charAt(0));
                output.append(temp.toUpperCase() + array[i].substring(1));
                output.append(" ");
            }
            return output.toString().trim();
        }

        public static void main(String[] args) {
            Task3 t3= new Task3();
            t3.readString();
            String chuoi = t3.upperCaseString(t3.chuoi);
            System.out.println("Chuỗi in hoa chữ đầu: " +chuoi);

        }

    }

