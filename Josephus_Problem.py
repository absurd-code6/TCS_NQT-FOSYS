'''Problem (classic - "Josephus Problem"):
N people are standing in a circle, numbered 1 to N. 
Starting from
person 1, every K-th person is eliminated going around the circle
(repeatedly), until only ONE person remains. 
Find the position (1-indexed) of that final survivor.'''

n=int(input())
k=int(input())
people=[]
for i in range(1,n+1):
    people.append(i)
idx=0
while len(people)>1:
    idx=(idx+k-1)%len(people)
    eliminated=people.pop(idx)
    print("Person " + str(eliminated) + " was eliminated.")
print("\nThe final survivor is person:", people[0])

'''How it works:Building the circle: We make a list [1, 2, 3, ..., N].
Finding the target: (index + k - 1) moves forward by K 
steps (the -1 accounts for 0-based list indexing in Python).
Wrapping around: % len(people) acts like a circle—when the 
count goes past the end of the list, it loops back to the start.
Eliminating: .pop(index) removes that person and shrinks 
the list until only one survivor is left.'''