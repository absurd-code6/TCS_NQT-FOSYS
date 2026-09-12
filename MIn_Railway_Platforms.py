#Greedy Problem(Skwz)
'''Given arrival and departure times of all trains that reach a 
railway station. Your task is to find the minimum number of 
platforms required for the railway station so that no train waits. 
We can have arrival time of one train equal to departure of the other. 
In such cases, we need different platforms, i.e at any 
given instance of time, same platform can not be used for 
both departure of a train and arrival of another.
Note: Time intervals are in the 24-hour format(hhmm) 
where the first two characters represent hour (between 00 to 23 ) 
and last two characters represent minutes (between 00 to 59). 
Consider that all the trains arrive on the same day and leave 
on the same day.'''

def findPlatform(arr,dep,n):
    arr.sort()
    dep.sort()
    platform_needed=1
    max_platform=1
    i=1
    j=0
    while i<n and j<n:
        if arr[i]<=dep[j]:
            platform_needed+=1
            i+=1
        else:
            platform_needed-=1
            j+=1
        max_platform=max(max_platform,platform_needed)
    return max_platform

n = int(input())
arr = input().split()
for i in range(n):
    arr[i]=int(arr[i])
dep = input().split()
for i in range(n):
    dep[i] = int(dep[i])
print(findPlatform(arr, dep, n))

'''1. Input handling
n → number of trains
arr → arrival times
dep → departure times
Both lists are converted to integers.
2. Sorting
arr.sort()
dep.sort()
Arrival and departure times are sorted independently.
This allows us to process events in chronological order.
3. Initialization
plat_needed = 1
max_platform = 1
i = 1
j = 0
plat_needed: current number of platforms in use
max_platform: maximum platforms needed at any time (final answer)
i: pointer for arrivals
j: pointer for departures

We assume the first train has already arrived, so:

platforms needed = 1
start comparing from the second arrival (i = 1)
4. Main loop
while i < n and j < n:

We compare:

next arrival → arr[i]
next departure → dep[j]
5. Case 1: Train arrives before earlier departure
if arr[i] <= dep[j]:
    plat_needed += 1
    i += 1
A new train arrives before the previous one leaves
So we need one more platform
6. Case 2: Train departs first
else:
    plat_needed -= 1
    j += 1
A train leaves before the next arrives
So a platform gets freed
7. Track maximum platforms
max_platform = max(max_platform, plat_needed)
Keep updating the maximum platforms needed at any moment
8. Return result
return max_platform

Key Insight

This algorithm essentially simulates a timeline:

Arrival → increase platforms
Departure → decrease platforms

The maximum overlap of trains at any time = minimum platforms required

Important Detail
if arr[i] <= dep[j]:
If arrival time == departure time → treated as overlap
So separate platforms are needed (as per problem statement)

Example
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = 6
Step 1: Sort both arrays
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1120, 1130, 1200, 1900, 2000]
Step 2: Initialize
plat_needed = 1
max_platform = 1
i = 1, j = 0
Step 3: Traverse

We compare arr[i] and dep[j] at each step:

🔹 Iteration 1
Compare: arr[1] = 940 vs dep[0] = 910
940 > 910 → train departs first

plat_needed = 0
j = 1
🔹 Iteration 2
Compare: arr[1] = 940 vs dep[1] = 1120
940 ≤ 1120 → ट्रेन आ गई

plat_needed = 1
i = 2
max_platform = 1
🔹 Iteration 3
Compare: arr[2] = 950 vs dep[1] = 1120
950 ≤ 1120

plat_needed = 2
i = 3
max_platform = 2
🔹 Iteration 4
Compare: arr[3] = 1100 vs dep[1] = 1120
1100 ≤ 1120
 overlap:

plat_needed = 3
i = 4
max_platform = 3
🔹 Iteration 5
Compare: arr[4] = 1500 vs dep[1] = 1120
1500 > 1120 → departure

plat_needed = 2
j = 2
🔹 Iteration 6
Compare: 1500 vs 1130
departure again
plat_needed = 1
j = 3
🔹 Iteration 7
Compare: 1500 vs 1200
departure again
plat_needed = 0
j = 4
🔹 Iteration 8
Compare: 1500 vs 1900
arrival
plat_needed = 1
i = 5
🔹 Iteration 9
Compare: 1800 vs 1900
arrival
plat_needed = 2
i = 6
Final Answer
max_platform = 3'''