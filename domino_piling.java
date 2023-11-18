import java.util.Scanner;
 
public class Main {
	static int solution(int n, int m){
		return n*m/2;
	}
	public static void main(String[] args) {
			Scanner input=new Scanner(System.in);
			int n=input.nextInt();
			int m=input.nextInt();
			System.out.println(solution(n,m));
	}
}
