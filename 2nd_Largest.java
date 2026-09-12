import java.util.Scanner;

public class 2nd_Largest {
    public static int findSecondSmallest(int[] arr) {
        // Initialize smallest and secondSmallest to the maximum possible integer value
        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;
        for (int num : arr) {
            if (num < smallest) {
                // If current element is smaller than smallest,
                // the old smallest becomes secondSmallest, and current becomes smallest
                secondSmallest = smallest;
                smallest = num;
            } else if (num < secondSmallest && num != smallest) {
                // If current element is smaller than secondSmallest but not equal to smallest,
                // it becomes the new secondSmallest
                secondSmallest = num;
            }
        }
    
        return secondSmallest;
    }

public static int find2ndLargest(int[] arr){
    int largest=Integer.MIN_VALUE;
    int second_largest=Integer.MIN_VALUE;
for(int num:arr){
    if(num<largest){
        second_largest=largest;
        largest=num;
    }
    else if(num<second_largest && num!=largest){
    second_largest=num;
    }
}
return second_largest;
}

public static void main(String[] args) {
    


        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the elements in array");
        int size=100;
        int[] array = new int[size];

        // Take input for array elements
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < size; i++) {
            System.out.print("Element " + (i + 1) + ": ");
            array[i] = scanner.nextInt();
        }

        // Call the method to find the second smallest element
        int secondSmallest = findSecondSmallest(array);
        
        if (secondSmallest == Integer.MAX_VALUE) {
            System.out.println("Could not find a distinct second smallest element (e.g., all elements are the same).");
        } else {
            System.out.println("The second smallest element in the array is: " +
             secondSmallest);
        }
        System.out.println("Second Largest element is:"+ find2ndLargest(array));
        scanner.close();
    }
}