'''There is a biker going on a road trip. The road trip consists 
of n + 1 points at various altitudes. The biker starts his trip on 
point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] 
is the net gain in altitude between points i and i + 1 
for all (0 <= i < n). Return the highest altitude of a point.

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. 
The highest is 0.
'''
gain=list(map(int,input().split()))
curr_altitude=0
max_altitude=0
for g in gain:
    curr_altitude+=g
    if curr_altitude>max_altitude:
        max_altitude=curr_altitude
print(max_altitude)

'''Start at altitude 0
curr_altitude = 0

The biker always starts at altitude 0.

Think of this as:

Current altitude = 0
Store the highest altitude
max_altitude = 0

Since the trip starts at altitude 0, the highest altitude 
seen so far is also 0.

Visit every gain value
for g in gain:

This loop takes each number one by one.

For our example,

gain = [-5, 1, 5, 0, -7]

the values of g will be

-5
1
5
0
-7
Update the current altitude
curr_altitude += g

This means

curr_altitude = curr_altitude + g

If the biker climbs, the altitude increases.

If the biker goes downhill, the altitude decreases.

Check if this is the highest altitude
if curr_altitude > max_altitude:
    max_altitude = curr_altitude

If the current altitude is greater than the highest altitude 
seen before, update it.'''
#Dry Run
'''Starting altitude

0

After first gain (-5)

0 → -5

After second gain (+1)

-5 → -4

After third gain (+5)

-4 → 1

After fourth gain (+0)

1 → 1

After fifth gain (-7)

1 → -6

All altitudes are

0, -5, -4, 1, 1, -6

Highest altitude

1

Time Complexity: O(n), where n is the number of gains.
Space Complexity: O(1), because only two variables (curr_altitude and max_altitude) are used regardless of the input size.'''