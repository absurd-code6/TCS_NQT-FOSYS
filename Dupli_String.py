import cv2
path=r"C:\Users\KGN\Documents\TCS_NQT\Ques_4_Dupli_String.png"
img=cv2.imread(path)
#cv2.imshow(path,img)
#cv2.waitKey(0)

def duplicate_remover(s):
    if not s:
        return ""
    result=s[0]
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
          result+=s[i]

    '''Why s[i] != s[i-1] works
       if s[i] != s[i - 1]:
       You compare the current character with the previous one
       This is safe because when you're at index i, i-1 always exists 
       (starting from i = 1)
       It naturally preserves order and avoids duplicates
       Problem with s[i] != s[i+1]:At the last character:s[i + 1]
       doesn't exist → IndexError'''
    return result

str=input("Enter your duplicate string:")
print((f"The string after removing consecutive duplicates: {duplicate_remover(str)}"))

