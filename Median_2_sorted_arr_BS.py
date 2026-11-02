'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the 
median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
def Median_BF(nums1:list[int],nums2:list[int],m:int,n:int):
    i=0
    j=0
    res=[]
    while i<m and j<n:
        if nums1[i]<nums2[j]:
            res.append(nums1[i])
            i+=1
        else:
            res.append(nums2[j])
            j+=1

    while i<m:
        res.append(nums1[i])
        i+=1

    while j<n:
        res.append(nums2[j])
        j+=1

    k=n+m
    if k==0:
        return 0
    return float(res[k//2]) if k%2==1 else (res[k//2]+res[(k//2)-1])/2.0
#TC=O(m+n),SC=O(m+n)


def Median_BS(nums1:list[int],nums2:list[int],m:int,n:int):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    imin, imax, half_len = 0, m, (m + n + 1) // 2
    
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        
        # i is too small, must increase it
        if i < m and nums2[j - 1] > nums1[i]:
            imin = i + 1
        # i is too big, must decrease it
        elif i > 0 and nums1[i - 1] > nums2[j]:
            imax = i - 1
        # i is perfect
        else:
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])
                
            # If total length is odd, return the max of the left partition
            if (m + n) % 2 == 1:
                return float(max_of_left)
                
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
                
            # If total length is even, return the average of the middle two elements
            return (max_of_left + min_of_right) / 2.0


m=int(input())
nums1=[int(input()) for _ in range(m)]
n=int(input())
nums2=[int(input()) for _ in range(n)]
print(Median_BF(nums1,nums2,m,n))
print(Median_BF(nums1,nums2,m,n))