'''The "Min Cuts" Variation (Harder Exam/Interview Favorite)"Return the minimum number of cuts needed to partition the 
string such that every substring is a palindrome."

How it changes your approach:

While you can solve this with backtracking by finding all partitions and 
looking for the shortest one, doing so will result in a 
Time Limit Exceeded (TLE) error in interviews. 
This variation shifts the problem from pure Backtracking to 
Dynamic Programming (DP).'''

def min_cuts_palindrome(s):
    if not s or s == s[::-1]:
        return 0  # 0 cuts needed if the string is empty or already 
    #a palindrome

    n = len(s)
    
    # Step 1: Precompute a table to check if any substring s[i:j+1] is a palindrome in O(1) time
    is_pal = [[False] * n for _ in range(n)]
    for length in range(1, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                # A substring is a palindrome if outer chars match AND (it's short OR inner substring is a palindrome)
                if length <= 2 or is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True

    # Step 2: DP array to store the minimum cuts needed for prefix s[0:i+1]
    # Worst case: 'i' cuts for a string of length i+1 (e.g., "abc" needs 2 cuts: 
    # a|b|c)
    dp = [i for i in range(n)]

    for i in range(n):
        # If the entire prefix s[0:i+1] is already a palindrome, 0 cuts are 
        # needed
        if is_pal[0][i]:
            dp[i] = 0
        else:
            # Try every possible cut position 'j' between 0 and i
            for j in range(i):
                # If s[j+1:i+1] is a palindrome, we can cut right after index j
                if is_pal[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

    return dp[n - 1]


if __name__ == "__main__":
    test_string = "aab"
    print(f"Minimum cuts needed for '{test_string}': {min_cuts_palindrome(test_string)}")
    
    test_string_2 = "abacaba"
    print(f"Minimum cuts needed for '{test_string_2}': {min_cuts_palindrome(test_string_2)}")