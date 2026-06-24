''' Given a string str, Find the number of distinct subsequences 
that can be formed from it.
A subsequence is a sequence derived from the original string 
by deleting zero or more characters without changing the 
relative order of the 
remaining characters.

Note: Answer can be very large, so, ouput will be answer modulo 109+7.

Examples: 

Input: str = "gfg"
Output: 7
Explanation: The seven distinct subsequences are "", "g", "f", "gf", "fg", 
"gg" and "gfg" 

Input: str = "ggg"
Output: 4
Explanation: The four distinct subsequences are "", "g", "gg" and "ggg"'''

mod=1000000007
def generateSubseq(idx,curr,s,st):
    n=len(s)
    # if the end of string is reached
    # store the subsequence in set
    if idx==n:
        st.add(curr)
        return
    # skip the current character
    generateSubseq(idx+1,curr,st)
    # add the character s[i]
    generateSubseq(idx+1,curr+s[idx],s,st)
    
def distinctSubseq(s):
    # to store the unique subsequences
    st=set()
    
    # to store current subsequence
    curr = ""
    
    generateSubseq(0, curr, s, st)

    ans = len(st)
    return ans % mod

'''1. Line-by-Line ExplanationThe Main FunctionPythondef distinctSubseq(s):
    st = set()
    cur = ""
    generateSubseq(0, cur, s, st)
    ans = len(st)
    return ans % mod
st = set(): We use a set because sets automatically ignore duplicate values. If our string has repeating characters (like "aba"), the set ensures we only count unique subsequences.generateSubseq(0, cur, s, st): This kicks off our recursive helper function, starting at index 0 with an empty current string ("").ans % mod: It calculates the total number of unique subsequences found and applies modulo $10^9 + 7$ (a standard practice in competitive programming to prevent integer overflow).The Recursive Helper FunctionPythondef generateSubseq(ind, cur, s, st):
    n = len(s)
    if ind == n:
        st.add(cur)
        return
Base Case: If ind == n, it means we have made a decision for every single character in the string. We've reached the end, so we save whatever string we built (cur) into our set st and return to go back up the chain.Python    # skip the current character
    generateSubseq(ind + 1, cur, s, st)

    # add the character s[i]
    generateSubseq(ind + 1, cur + s[ind], s, st)
The Core Logic (Two Choices): For every character at index ind, the computer forks into two parallel universes:Don't Pick: It moves to the next index (ind + 1) without adding the current character to cur.Pick: It moves to the next index (ind + 1) and appends the current character (cur + s[ind]).

Dry Run ExampleLet's trace the code with a short string: s = "ab".Initially, ind = 0, cur = "", and st = {}.Here is how the recursion tree unfolds step-by-step:Start at ind = 0 (character 'a'):Choice 1 (Skip 'a'): Calls generateSubseq(1, "")At ind = 1 (character 'b'):Choice 1a (Skip 'b'): Calls generateSubseq(2, "").Base case reached (ind == 2): st.add("") $\rightarrow$ st = {""}Choice 1b (Pick 'b'): Calls generateSubseq(2, "b").Base case reached (ind == 2): st.add("b") $\rightarrow$ st = {"", "b"}Choice 2 (Pick 'a'): Calls generateSubseq(1, "a")At ind = 1 (character 'b'):Choice 2a (Skip 'b'): Calls generateSubseq(2, "a").Base case reached (ind == 2): st.add("a") $\rightarrow$ st = {"", "b", "a"}Choice 2b (Pick 'b'): Calls generateSubseq(2, "ab").Base case reached (ind == 2): st.add("ab") $\rightarrow$ st = {"", "b", "a", "ab"}Final ResultOnce all recursive paths finish, the set st contains: {"", "b", "a", "ab"}.ans = len(st) which is 4.4 % 1000000007 = 4.The function returns 4'''