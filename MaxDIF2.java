//Finding Max Difference b/w 2 elements in an array
import java.util.*;

public class MaxDIF2 {
public static int maxdiff(int[] arr,int n){
 int max_diff=arr[1]-arr[0];
for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
        if(arr[j]-arr[i]>max_diff)
         max_diff=arr[j]-arr[i];
    }
}
return max_diff;
}
public static void main(String[] args) {
Scanner sc= new Scanner(System.in);
System.out.println("Enter the number of elements in the array:");
int size=sc.nextInt();
int[] arr = new int[size];
System.out.printf("Enter %d elements:\n",size);
for(int i=0;i<size;i++){
System.out.printf("Enter element [%d]: ",i);
arr[i]=sc.nextInt();
}
System.out.println("Maximum Difference is:"+ maxdiff(arr,size));
sc.close();
}
}
