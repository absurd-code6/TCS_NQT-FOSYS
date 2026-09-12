'''Problem (verified TCS NQT statement - "Balloon Capacity"):
* Given the weights of N people and a maximum balloon capacity,
* find the maximum NUMBER of people that can board the balloon
* without exceeding the capacity. Always pick the lightest person
* first, since prioritizing lighter people first lets us fit the
* greatest possible headcount before capacity runs out'''
 
N=int(input())
wt=[int(input()) for _ in range(N)]
max_capacity=int(input())
wt.sort()
count=0

for i in range(N):
    if wt[i]<=max_capacity:
        count+=1
        max_capacity-=wt[i]
    else:
        break  
# Since the list is sorted, no one remaining will fit 
# either(optional but good optimization technique)
print(count)  
  
#Using While loop
'''i=0
while i<N and wt[i]<=max_capacity:
    count+=1
    max_capacity-=wt[i]
    i+=1'''