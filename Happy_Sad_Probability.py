'''Problem (based on verified TCS NQT statement - "Happy/Sad State
* Probability"):
* You are given an integer N, representing the number of people
* initially in the Happy state (everyone else, if any, starts Sad).
* At each iteration (time step), state transitions happen as follows:
*   - From Happy: 70% become Sad, 30% remain Happy.
*   - From Sad:   50% remain Sad, 50% become Happy.
* Given a number of iterations K, compute how many people are in
* each state after K iterations.'''

happy=float(input())
k=int(input())
sad=0.0 #Initially 0 sad people
for _ in range(k):
    nxt_happy=0.3*happy + 0.5*sad
    nxt_sad=0.5*sad + 0.7*happy
    happy=nxt_happy
    sad=nxt_sad
# Output rounded to 2 decimal places (or as requested by test cases)
print(f"{happy:.2f}")
print(f"{sad:.2f}")

# This question is based on Law Of Total Probability
'''Approach (Simulation using expected-value transitions):
 We don't need to track individuals - we can track EXPECTED COUNTS.
At each iteration:
   newHappy = (0.30 * currentHappy) + (0.50 * currentSad)
   newSad   = (0.70 * currentHappy) + (0.50 * currentSad)
Repeat this update K times, then print the final expected counts.
(Assumes 0 people start Sad unless a separate "initial sad count"
input is provided - adjust the initial values below if your exact
version of the question supplies both a Happy count and a Sad count.)

Time Complexity: O(k), where k is the number of iterations.'''
