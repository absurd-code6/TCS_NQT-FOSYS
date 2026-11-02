
def Permutations_Of_Strings(s:str):
    if not s:
        return ""
    chars=sorted(s)
    used=[False]*len(s)
    res=[]
    def backtrack(path:list):
        if len(path)==len(chars):
           res.append("".join(path))
           return
        for i in range(len(chars)):
            if used[i]:
                continue
            if i>0 and chars[i]==chars[i-1] and not used[i-1]:
                continue
            used[i]=True
            path.append(chars[i])
            backtrack(path)
            path.pop()
            used[i]=False
    backtrack([])
    print(len(res))
    return res

s=input().strip()
print(Permutations_Of_Strings(s))

#how the for loop and the recursive call work together for better understanding

'''Imagine you have a row of empty boxes (like slots in a word) and a pile of 
letter tiles. You want to fill those boxes one by one.

The for loop and the recursive call work together like a tireless worker 
who tries every possible path, and whenever they hit a dead 
end (or finish a word), they step back, swap a tile, and try again.

The Roles of the Three Main Players
The for loop (The "What can I pick right now?" engine):

Looks at your pile of tiles and goes through them one by one for the current 
position you are trying to fill.

The Recursive Call (The "Move on to the next box" trigger):

Once you place a tile in the current box, recursion says: "Great! Now 
freeze this moment, jump to the next box, and start the whole process 
over again for that box."

path.pop() (The "Undo" button):

When recursion finishes exploring a path and comes back, pop() takes the 
last tile off your word so the for loop can pick a different tile for that same box.

Step-by-Step Trace with "ab"
Let's see how they dance together using the string "ab".

Level 0: Filling Box 1
path = [] (Empty)

The for loop looks at available tiles: ['a', 'b'].

Iteration 1 (i = 0, picks 'a'):

It marks 'a' as used.

It adds 'a' to the path: path = ['a'].

Now, it hits the recursive call: “Okay, I locked in 'a' for Box 1.
Go figure out Box 2!”

Level 1: Filling Box 2 (Inside the recursive call)path = ['a']
A brand new for loop starts for Box 2, looking at remaining unused tiles: ['b'].
Iteration (i = 1, picks 'b'):It marks 'b' as used.
It adds 'b' to the path: path = ['a', 'b'].It hits another recursive call: 
“Box 2 is filled! Go figure out Box 3.”

Level 2: The Goal (Inside the second recursive call )path = ['a', 'b']
The function checks: "Are all boxes full? Yes (len(path) == len(chars)).
"It saves "ab" to the results list and returns (steps back to Level 1).
Backtracking: Undoing to try the next option

Back in Level 1, the code finishes the recursive call and hits the cleanup lines:
path.pop() removes 'b' -> path = ['a']used[1] = False 
(marks 'b' as available again).

The Level 1 loop ends because it ran out of tiles. 
It returns to Level 0.Back in Level 0, it hits its own cleanup lines:
path.pop() removes 'a' -> path = []used[0] = False (marks 'a' as available again).

Back to Level 0, Iteration 2
The Level 0 for loop moves to its next option: i = 1 (picks 'b').

It repeats the exact same dance: locks 'b', recurses to fill the next box with 'a', 
saves "ba", pops, and finishes!

In this function, duplicates are handled using a clever combination of sorting and a strict skipping rule during backtracking.

If you didn't handle duplicates, a string like "aab" would generate 6 permutations (treating the two 'a's as different), resulting in duplicate outputs like ("aab", "aab", "aba", "aba", "baa", "baa").

The code prevents this and ensures every generated permutation is entirely unique. Here is how it works step-by-step:

Step 1: Sorting the Characters First

chars = sorted(s)
Before the backtracking even starts, the function sorts all characters alphabetically.If s = "aba", chars becomes ['a', 'a', 'b'].This brings identical characters right next to each other, making them easy to track.Step 2: The Magic Guard Condition (The Core Logic)Inside the loop, right before deciding to pick a character, the code has this crucial check:Pythonif i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
  continue
This line stops the computer from creating duplicate branches. 
Let's break down its three parts:
i > 0 and chars[i] == chars[i-1]:Checks if the current letter (chars[i]) is identical 
to the letter immediately before it (chars[i-1]).and not used[i-1]:
This is the most important part. 
It asks: "Was the previous identical letter not used in the current path?"
In other words, did we just skip the previous identical letter at this 
same level of choices?If the answer is yes (the previous identical letter was skipped), 
the code immediately skips the current letter (continue).
A Concrete Example: Why This WorksImagine s = "aab". 
We label the two 'a's as $A_1$ and $A_2$, and the 'b' as B.
Sorted order: [$A_1, A_2, B$]

Without the rule (what would go wrong):At the very beginning, the loop can 
choose either $A_1$ or $A_2$ to start the word:Branch 1: Starts with A_1 -> leads to permutations like A_1 A_2 B ("aab") and A_1 B A_2 ("aba").
Branch 2: Starts with A_2 -> leads to permutations like A_2 A_1 B ("aab") 
and A_2 B A_1 ("aba").
Notice how both branches produce the exact same words! That's a duplicate.

What does not used[0] mean at that moment? When the loop moves from 
$A_1$ to $A_2$ (at index 1), we have just finished exploring everything 
that starts with $A_1$. As part of backtracking, the code cleaned up 
after itself by setting used[0] = False and popping $A_1$ off the path.
Because of this cleanup, when the loop tries to start a fresh choice 
at the root level, used[0] is False 
(meaning $A_1$ is currently marked as "not used/available").
2. Why does it trigger continue?
The code evaluates the rule:

if i > 0 and chars[i] == chars[i-1] and not used[i-1]:

i > 0 is true (we are looking at index 1).chars[1] == chars[0] is true 
($A_2$ is identical to $A_1$).not used[0] is true 
(because $A_1$ is currently unused/available at this level).
Because all three conditions are met, the code says: "Stop! Do not pick $A_2$ here."

Why must we skip $A_2$ here? (The Big Picture)If the code didn't skip $A_2$ here, 
it would start a brand-new, independent branch beginning with $A_2$.However, 
a branch starting with $A_2$ would end up generating the exact same set of 
permutations as the branch that just finished starting with $A_1$, 
just with the two identical letters swapping places.
'''