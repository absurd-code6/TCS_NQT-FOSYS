n=int(input("Enter no of transactions:"))

#Alice Bob 1000 500.00 // 1st scenario diff<=60
#Charlie Dave 1020 300.00
#Eve Frank 1040 900.00

#Alice Bob 1000 500.00 //2nd scenario duplicate +nt
#Charlie Dave 1020 300.00
#Alice Bob 1055 200.00

#Alice Bob 1000 500.00 // 3rd scenario valid(no duplicate & diff > 60)
#Charlie Dave 1080 300.00
#Eve Frank 2080 900.00

senders=[]
receivers=[]
timestamp=[]
amt=[]

for i in range(n):
  parts =input(f"Transactions {i+1} (sender receiver timestamp amt) : ").split()
  senders.append(parts[0])
  receivers.append(parts[1]) 
  timestamp.append(int(parts[2]))
  amt.append(float(parts[3]))
seen = {}
for i in range(n):
    key=senders[i] + "|" +  receivers[i]
    if key in seen:
        print("Error: Duplicate Transaction")
        seen=None
        break
    seen[key]=i

if seen is not None:
    fraud = False
    for i in range(1,n):
        diff = abs(timestamp[i]-timestamp[i-1])
        if diff <= 60:
            print("Fraud Detected")
            fraud = True
            break
    if not fraud:
        print("All Transactions Valid")
