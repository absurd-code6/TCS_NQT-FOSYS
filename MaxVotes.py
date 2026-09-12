'''For a given an array of names of candidates in an election 
and a candidate name in the array represents a vote cast to the 
candidate, write a program to print the name of the candidate who 
received max votes and if there is a tie then print lexicographically 
smaller name (means one which comes in a dictionary first). '''

def Max_vote(list):
    votes={} #Empty set ==> Dictionary/Hash Map
    for name in list:
        if name in votes:
            votes[name]+=1
        else:
            votes[name]=1
    max_votes=max(votes.values())
    candidates=[]
    for name in votes:
        if votes[name]==max_votes:
            candidates.append(name)
    candidates.sort()
    print(candidates[0])
            
list=["john", "mary", "john", "alice", "mary", "john"]
Max_vote(list)

'''Step 1: Understand the problem

You are given a list like:

["john", "mary", "john", "alice", "mary", "john"]

Each name = one vote.

👉 Goal:

Find who got the maximum votes
If tie, return the lexicographically smallest name (dictionary order)
🧠 Step 2: First naive thought

An amateur programmer might think:

“Let me check how many times each name appears.”

So you’d want something like:

john → 3
mary → 2
alice → 1
🧠 Step 3: How to count votes?

At first, you might try something like:

for each name:
    count how many times it appears

But that would repeat work again and again 😬

So a better idea:

👉 Use a dictionary (hash map)

key = candidate name
value = vote count
🧠 Step 4: Build the vote count
votes = {}

for name in arr:
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1

Now you have all counts stored neatly.

🧠 Step 5: Find the maximum votes

Now think:

“Let me find the highest vote count.”

max_votes = max(votes.values())
🧠 Step 6: Handle tie case

Now comes the tricky part 🤔

Multiple candidates might have the same max_votes.

So:

Collect all candidates with max_votes
Then pick the smallest (dictionary order)
candidates = []

for name in votes:
    if votes[name] == max_votes:
        candidates.append(name)

Now sort:

candidates.sort()

Pick first:

print(candidates[0])

How are we able to sort a list of strings?

Good question—this often feels a bit “magical” at first.

🧠 Why can we sort strings?

In Python, strings are compared lexicographically, which basically means dictionary order.

So when you do:

candidates.sort()

Python compares strings character by character.

🔍 How comparison works

Example:

"apple" < "banana"

Why?

Compare first letters: 'a' vs 'b'
Since 'a' comes before 'b', "apple" is smaller
🔍 If first letters are same
"bat" < "ball"

Compare step by step:

'b' == 'b'
'a' == 'a'
't' > 'l' → so "bat" is greater
🔡 What defines this order?

Python uses Unicode (ASCII for basic letters) values:

ord('a')  # 97
ord('b')  # 98

So sorting is basically happening based on these numeric values behind 
the scenes.

⚠️ Important detail (case sensitivity)
["apple", "Banana", "cat"]

Sorted result:

['Banana', 'apple', 'cat']

Why?

'B' (66) comes before 'a' (97)
✅ Back to your problem

When you do:

candidates.sort()

It ensures:

Names are arranged in alphabetical order
So the first element is the lexicographically smallest
💡 Small demo
candidates = ["john", "mary", "alice"]
candidates.sort()
print(candidates)

Output:

['alice', 'john', 'mary']
🚀 Bonus (ignore case)

If you ever want case-insensitive sorting:

candidates.sort(key=str.lower)'''