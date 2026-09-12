'''  '''

def convert(s):
    new_s=[]
    for i in s:
        new_s.append(ord(i))
    for i in range(len(new_s)):
        if new_s[i]==65 or new_s[i]==69 or new_s[i]==73 or new_s[i]==79 or new_s[i]==85:
           new_s[i]+=1
        else:
            new_s[i]-=1
    res=""
    for j in new_s:
        res+=str((chr(j)))
    return res
    
s=input().upper()# Neighbours
print(convert(s))
