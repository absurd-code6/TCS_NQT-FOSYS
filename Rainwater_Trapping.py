'''Given an array arr[] of size n consisting of non-negative integers, 
where each element represents the height of a bar in an elevation 
map and the width of each bar is 1, determine the total 
amount of water that can be trapped between the bars 
after it rains.

Trapping Rainwater Problem
Examples:  

Input: arr[] = [3, 0, 1, 0, 4, 0, 2]
Output: 10
Explanation: The expected rainwater to be trapped is shown 
in the above image.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.

Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides'''

#If you see these keywords or framing devices, it's secretly a 
# Trapping Rainwater problem:

#The Factory/Warehouse Problem: "You are given an array representing 
# the heights of adjacent storage containers. 
# If a liquid leak occurs, how much liquid is contained 
# in the gaps before it overflows?"

#The Skyline Silhouette: "Given a histogram silhouette, 
# find the volume of the largest 'lakes' formed if 
# the silhouette is submerged in water."

'''Intuition
To trap water at any index in the elevation map, there must be 
taller bars on both its left and right sides. The water that can be 
stored at each position is determined by the height of the shorter of 
the two boundaries (left and right), minus the height 
of the current bar.
We compute the trapped water at each 
index as: min(leftMax, rightMax) - height[i], if this value is positive.
The total trapped water is the sum of water stored at all valid indices.
If either side lacks a boundary, no water can be trapped at that position.
'''
#Naive Approach O(n^2) & O(1) space

def max_rain_water(arr):
    result=0
    for i in range(1,len(arr)-1):
        left=arr[i]
        for j in range(i):
            left=max(left,arr[j])
            
        right=arr[i]
        for j in range(i+1,len(arr)):
            right=max(right,arr[j]) 
        result+=(min(left,right)-arr[i])
    return result

print(max_rain_water([2, 1, 5, 3, 1, 0, 4]))#O/p=9

