import java.util.Scanner;
public class Test{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=sc.nextInt();
        int d=sc.nextInt();
        int e=sc.nextInt();
        int Sum=(a+b+c+d+e);
        int sum=(Sum/5);
         if(sum>=90)
         {
            System.out.println("Grade A");
         }
         else if(sum>=80)
         {
            System.out.println("Grade B");
         }
         else if(sum>=70)
         {
            System.out.println("Grade C");
         }
         else if(sum>=60)
         {
            System.out.println("Grade D");
         }
         else if(sum>=40)
         {
            System.out.println("Grade E");
         }
         else
         {
            System.out.println("Grade F");
         }
    }
}