"""Understanding problem statement:
Inputs:
N:Length of NUM array
X: Upper bound of valid range
Y:Lower bound of valid range
NUM:Array of numbers

Operations:
Form pairs(NUM[i],NUM[j])
Concatenate them(like 5 becomes 55)
Check if X<=Concatenated No<=Y
Count how many such valid pairs exist
Eg.   N=4,X=10,Y-99
NUM=[5,15,1,9]
Pairs & Concatenations:
scss
Copy
Edit
(5,5) -> 55 Allowed(1
(5,15) -> 515 Out Of Range! Not Allowed (0)
(5,1) -> 51 (1)
(5,9) -> 59 (1)
(15,5) ->  155 (0)"""
def concat(N,NUM,X,Y):
    count=0;
    for i in range(N):
        for j in range(N):
            concatenated_sum=int(str(NUM[i])+str(NUM[j]))
            if concatenated_sum>=X and concatenated_sum<=Y:
                count+=1;
            ''' if i!=j:
                sum=int(str(NUM[j])+str(NUM[i]))
                if sum>=X and sum<=Y:
                    count+=1'''
                
    return count;
        
    
        
NUM=[]
N=int(input("Enter the size of the array:\n")) #4
print("Enter the elements\n")
for i in range(N):
    x=input()
    NUM.append(x)
X=int(input("Enter lower bound of valid range:"))#10
Y=int(input("Enter upper bound of valid range:"))#99
print(f"Total Number of valid possible concatenated numbers is {concat(N,NUM,X,Y)}")
