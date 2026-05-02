'''Write a program to find the difference between the 
highest occurrence and the least occurrence of any number 
in a given array and print it. 

For example, if array=7,8,4,5,4,1,1,7,7,2,5 ,then 
output= 2 because 7 occur 3 times in array means 
highest occurrence element
and 2 or 8 occur 1 time means least occurrence element so 
difference between them = 3 - 1 = 2 '''

def findDiff(arr):
    freq={}
    for i in arr:
        if i in freq:
         freq[i]+=1
        else:
            freq[i]=1
    highest_occurence=max(freq.values())
    least_occurence=min(freq.values())
    return highest_occurence-least_occurence

print("Enter an array:")
arr=map(int,input().split())
print(f"Difference between highest and least occurence is {findDiff(arr)}")
