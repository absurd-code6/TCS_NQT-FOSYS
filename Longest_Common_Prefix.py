'''Write a function to find the longest common prefix 
string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def LCP(strs):
    empty=""
    if not strs:
        return ""
    for i in range(len(str[0])):
        #chars=str[0][i]
        for s in strs:
            if i>=len(s) or s[i]!=strs[0][i]: #s[i]!=chars
                return ""
        res+=strs[0][i] # chars
    
#Alternative
'''def LCP(strs: list[str]) -> str:
  if not strs:
    return ""

  # Take the first string as a reference
  first_str = strs[0]

  for i in range(len(first_str)):
    char = first_str[i]
    
    # Check this character against all other strings
        
    for string in strs[1:]:
      # If out of bounds or characters don't match
      
      if i >= len(string) or string[i] != char:
        return first_str[:i]

  return first_str'''

