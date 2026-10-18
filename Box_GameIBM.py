'''Aryan and Ankit play a game with N boxes. There are an even number 
of boxes arranged in a row, and each box has a positive integer number of 
stone balls, denoted by balls(i). The objective of the game is to end 
with the most balls. The total number of balls across all the boxes is odd, 
so there are no ties.

Rules:

Aryan and Ankit take turns picking all the balls from either the 
beginning or the end of the row of boxes. Aryan always plays first. 
Both players play optimally, meaning they make decisions to maximize their number of balls.

The game ends when there are no more boxes left. Assume Aryan and Ankit play optimally. 
Print Aryan if Aryan wins, and print Ankit if Ankit wins.

Input Format
The first line of input contains an integer N, representing the size of the array.

The second line of input contains N space separated integers representing the 
number of balls in the boxes.

Output Format
Display "Aryan" if Aryan wins or Display"Ankit" if Ankit wins.
'''
def BallGame(balls):
    n=len(balls)
    dp=[[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i]=balls[i]

    for l in range(2,n+1):
        for i in range(n-l+1):
            j=i+l-1
            # Player takes either start box (i) or end box (j)
            left=balls[i]-dp[i+1][j]
            right=balls[j]-dp[i][j-1]
            dp[i][j]=max(left,right)
    return "Aryan" if dp[0][n-1]>0 else "Ankit"

n=int(input())
balls=[int(input()) for _ in range(n)]
print(BallGame(balls))
#TC=O(n^2)

evensum=sum(balls[0::2]) #0,2,4,...
oddsum=sum(balls[1::2]) #1,3,5,...
if evensum>oddsum:
    print("Aryan") 
    exit(0)

else: "Aryan" 
exit(0)
#TC=O(n),SC=O(1)
'''
Imagine you have a line of boxes with numbers on them.When it is your turn, 
you can pick either the first box or the last box.Whatever box you 
pick, you add its value to your score.Whatever box your opponent picks 
on their turn, it subtracts from your net advantage.Because both players 
are equally smart, every choice you make assumes the opponent 
will also make the best possible choice on their turn.To figure out the best move 
for a row of boxes, the DP algorithm uses a simple trick:
"If I take the left box, my net gain is (Left Box Value - Opponent's 
best gain from the remaining boxes).""If I take the right box, my net gain is 
(Right Box Value - Opponent's best gain from the remaining boxes).
"The DP algorithm starts with tiny subproblems (1 box), then builds up 
to 2 boxes, 3 boxes, and finally all $N$ boxes.

2. Dry Run ExampleLet's trace the algorithm with a small array of 4 boxes:
balls = [3, \, 7, \, 2, \, 4] 
Indices: 0 (val 3), 1 (val 7), 2 (val 2), 3 (val 4).
We build a table dp[i][j] which stores:
"The maximum point advantage Player 1 can get from the 
sub-array starting at index i and ending at index j.
"Step A: Subarrays of Length 1 (Base Cases)If there is only 1 box remaining, 
the current player simply takes it. No boxes are left for the opponent.
dp[0][0] (Box [3]): gain = 3 dp[1][1] (Box [7]): gain = 7 dp[2][2] 
(Box [2]): gain = 2dp[3][3] (Box [4]): gain = 4

Step B: Subarrays of Length 2Now we consider all sub-chains of 
2 adjacent boxes.1. Range [0...1] (Boxes: [3, 7])
Take Left (3): You get $3$, leaving [7] for the opponent (dp[1][1] = 7). 
Net gain = $3 - 7 = -4$.
Take Right (7): You get $7$, leaving [3] for the opponent (dp[0][0] = 3). 
Net gain = $7 - 3 = +4$.
Best choice: $\max(-4, 4) =$ 4. So dp[0][1] = 4.2. 
Range [1...2] (Boxes: [7, 2])
Take Left (7): Net gain = $7 - 2 = +5$.
Take Right (2): Net gain = $2 - 7 = -5$.
Best choice: $\max(5, -5) =$ 5. 
So dp[1][2] = 5.3. Range [2...3] (Boxes: [2, 4])
Take Left (2): Net gain = $2 - 4 = -2$.
Take Right (4): Net gain = $4 - 2 = +2$.
Best choice: $\max(-2, 2) =$ 2. So dp[2][3] = 2

Step C: Subarrays of Length 3Now we look at sub-chains of 3 boxes.1. 
Range [0...2] (Boxes: [3, 7, 2])
Take Left (3): Leaves [7, 2] for opponent. 
Opponent's advantage on [7, 2] is dp[1][2] = 5.
Your net gain = $3 - 5 = -2$.Take Right (2): Leaves [3, 7] for opponent. 
Opponent's advantage on [3, 7] is dp[0][1] = 4.
Your net gain = $2 - 4 = -2$.
Best choice: $\max(-2, -2) =$ -2. So dp[0][2] = -2.2. Range [1...3] (Boxes: [7, 2, 4])
Take Left (7): Leaves [2, 4] for opponent (dp[2][3] = 2).
Your net gain = $7 - 2 = 5$.
Take Right (4): Leaves [7, 2] for opponent (dp[1][2] = 5).
Your net gain = $4 - 5 = -1$.
Best choice: $\max(5, -1) =$ 5. So dp[1][3] = 5.

Step D: Subarray of Length 4 (Full Game: [0...3])
This gives the final outcome for the full game with boxes [3, 7, 2, 4].
Option A — Take Left box (3):Leaves [7, 2, 4] (range [1...3]) for Ankit.
Ankit's best advantage on [1...3] is dp[1][3] = 5.
Aryan's net advantage = $3 - 5 = -2
Option B — Take Right box (4):Leaves [3, 7, 2] (range [0...2]) for Ankit.
Ankit's best advantage on [0...2] is dp[0][2] = -2.
Aryan's net advantage = (4 - (-2) = 6.
Aryan's Choice: max(-2, 6) = 6. 
So dp[0][3] = 6.


dp[i][j]	Index 0 (3)	Index 1 (7)	Index 2 (2)	Index 3 (4)
Index 0 (3)	3	4	-2	6
Index 1 (7)	—	7	5	5
Index 2 (2)	—	—	2	2
Index 3 (4)	—	—	—	4

Conclusion & OutputThe value at dp[0][3] is 6.Since 6 > 0, it means 
Aryan can finish the game with 6 more balls than Ankit.The program checks 
if dp[0][3] > 0: and outputs "Aryan".
'''