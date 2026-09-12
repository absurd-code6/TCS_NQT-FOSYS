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

'''In most coding platforms (like LeetCode, HackerRank, or 
standard CLI programs), each transaction is passed on 
its own line:

Plaintext
Alice Bob 100 50.5
Charlie Dave 120 30.0
Eve Frank 200 99.9
Because input() reads only up to the end of the line 
(newline character \n), calling input() once will only grab 
"Alice Bob 100 50.5". 
To read the remaining lines, you have to call input() multiple times 
— which requires a loop.'''

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
