'''Given a binary array arr[] consisting of only 0s and 1s, 
find the length of the longest contiguous sequence of 
either 1s or 0s in the array.

Examples : 

Input: arr[] = [0, 1, 0, 1, 1, 1, 1]
Output: 4
Explanation: The maximum number of consecutive 1's in 
the array is 4 from index 3-6.

Input: arr[] = [0, 0, 1, 0, 1, 0]
Output: 2
Explanation: The maximum number of consecutive 0's in 
the array is 2 from index 0-1.

Input: arr[] = [0, 0, 0, 0]
Output: 4
Explanation: The maximum number of consecutive 0's in the array is 4.
'''
def consec(arr):
    if not arr:
        return 0
    count=1
    max_count=1 # Start at 1, because a single element is a streak of 1
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            count+=1
        else:
            max_count=max(max_count,count)
            count=1
    # CRITICAL FIX: Update max_count one last time after the loop ends
    max_count = max(max_count, count)
    return max_count

print("Enter a binary aray:")
arr=list(map(int,input().split()))
print("Max no of consecutive 0's or 1's is ",consec(arr))

'''What happens without the else block?
You asked what happens if we completely remove this section:

Python
else:
    max_count = max(max_count, count)
    count = 1
If you delete that block, your code completely loses the ability to "reset" 
when a streak breaks. Two bad things will happen:

count never resets: Instead of counting consecutive i
dentical numbers, count will simply increment every time 
any number matches its immediate neighbor. 
For example, in [1, 1, 0, 0], it matches at index 1 and index 3. 
count would just keep climbing to 3.

max_count is never updated mid-array: If a streak breaks, 
you wouldn't save the high score of that streak.

Without the else block to log the maximum streak and 
reset the counter back to 1, the code would fail to 
accurately measure anything except a perfectly uniform array.'''

#Why do we have to update max_count one last time after the loop ends ?

'''Let's trace a simple example to see this in 
action: arr = [0, 1, 1, 1]

Step-by-Step Trace Without the Final Update
Start: count = 1, max_count = 1

Index 1 (Value 1): Is 1 == 0? No.

We hit the else block!

max_count = max(1, 1) -> 1

count resets to 1.

Index 2 (Value 1): Is 1 == 1? Yes!

count becomes 2.

Index 3 (Value 1) — Last Element: Is 1 == 1? Yes!

count becomes 3.

The Loop Ends Here. Notice what just happened. 
The loop ran out of elements. Because index 3 was the end of the array, 
the code never reached the else block to 
evaluate that final count of 3.

If we don't have that final line outside the loop, 
the function returns max_count, which is still stuck at 1, 
completely missing the streak of 3 at the end.'''