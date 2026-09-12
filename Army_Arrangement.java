
import java.util.*;

public class Army_Arrangement {
public static void main(String[] args) {

Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
int r = sc.nextInt();
int end = sc.nextInt();
int total_arrangements=arrangements(1, 1, n, r, end);
System.out.println(total_arrangements);
sc.close();
}
static int arrangements(int posn,int last,int n,int r,int end){
    if(posn==n) {
    return (last==end) ? 1:0;
    }
    int total=0;
    for(int i=1;i<=r;i++){
    if (i!=last) { // no adjacent element is same
    total += arrangements(posn+1,i,n,r,end);
    }
    }
    return total;
    }
}
/* By Dynamic Programming
public class Army_Arrangement {
public static void main(String[] args) {

Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
int r = sc.nextInt();
int end = sc.nextInt();
dp = new int [n+1][r+1];
//Initializing with -1
for(int i=0;i<=n;i++){
Arrays.fill(dp[i],-1);
}
//Starting from posn 1 with value 1
int total_arrangements=arrangements(1, 1, n, r, end);
System.out.println(total_arrangements);
sc.close();

}
static int [][] dp;
static int arrangements(int posn,int last,int n,int r,int end){
    if(posn==n) {
    return (last==end) ? 1:0;
}
// If already computed
if(dp[pos][last] != -1) {
return dp[pos][last]
}
    int total=0;
    for(int i=1;i<=r;i++){
    if (i!=last) { // no adjacent element is same
    total += arrangements(posn+1,i,n,r,end);
  }
}
//Storing Result
dp[pos][last] = total;
return total;
}*/
