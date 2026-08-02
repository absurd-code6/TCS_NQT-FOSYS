'''Problem (verified TCS NQT statement - "Minimum Battery Charge for
* Laptops"):
* You are given an integer N (minimum charge required) and an array
* of integers representing the charge percentage in each laptop.
* Count how many laptops have charge >= N'''

min_charge=int(input())
charge_percentage=list(map(int,input().split()))
count=0
for i in range(charge_percentage):
    if charge_percentage[i]>=min_charge:
        count+=1
print(count)
