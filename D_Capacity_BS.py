'''A conveyor belt has packages that must be shipped from one port to another 
within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load 
the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages 
on the conveyor belt being shipped within days days.
Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days 
like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 
and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is 
not allowed.
Example 2:

Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days 
like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
'''
def Ship_Capacity(weights:list[int],D:int):
    if not weights or D<=0:
        return -1
    l=max(weights)
    h=sum(weights)
    while l<=h:
        mid=(l+h)//2
        if No_of_Days(weights,mid,D):
            h=mid-1
        else:
            l=mid+1
    return l

def No_of_Days(weights,mid,D):
    '''If adding this package exceeds the ship's capacity (mid)
    We must ship it on the next day
    It becomes the first package of the new day
    Otherwise, keep loading it onto the current day'''
    cur_load=0
    days=1
    for i in weights:
        if cur_load + i > mid:
            days+=1
            cur_load=i
        else:
            cur_load+=i
    if days<=D:
        return True
    else:
        return False
#or return days<=D

if __name__=="__main__":
   print(No_of_Days.__doc__,end=" \n")
   #help(No_of_Days)
   weights=list(map(int,input().split()))
   D=int(input())
   print(Ship_Capacity(weights,D))