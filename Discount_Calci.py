purchase=float(input("Enter the total purchase amount:"))
discount=0
purchase_amt=int(purchase)
if purchase_amt <=0:
    print("Error X")
elif purchase_amt < 1000:
    discount=0.05
elif 1000 <= purchase_amt and purchase_amt <= 5000:
    discount=0.10
elif purchase_amt >5000:
    discount=0.15
payable_amt=purchase_amt*(1-discount)
print(int(payable_amt))
