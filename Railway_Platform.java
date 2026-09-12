/*Given arrival and departure times of all trains that reach a railway 
station. Your task is to find the minimum number of platforms required 
for the railway station so that no train waits. We can have 
arrival time of one train equal to departure of the other. 
In such cases, we need different platforms, i.e at any given 
instance of time, same platform can not be used for both 
departure of a train and arrival of another.
Note: Time intervals are in the 24-hour format(hhmm) 
where the first two characters represent hour (between 00 to 23 ) 
and last two characters represent minutes (between 00 to 59). 
Consider that all the trains arrive on the same day and 
leave on the same day. */

import java.util.*;

public class Railway_Platform{
public static void main(String[] args) {

Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n];
        int[] dep = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            dep[i] = sc.nextInt();
        }

        System.out.println(findPlatform(arr, dep, n));
        sc.close();
}
public static int findPlatform(int[] arr,int[] dep,int n){
int plaform_needed=1;
int max_platform=1;
int i=1;
int j=0;
while(arr[i]<n && dep[j]<n){
if(arr[i]<=dep[j]){
plaform_needed++;
i++;
}
else{
plaform_needed--;
j++;
}
max_platform=Math.max(max_platform,plaform_needed);
}
return max_platform;
}
}