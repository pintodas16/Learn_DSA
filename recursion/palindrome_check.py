# using two pointer 

def is_palindrome(s,l,r):
    while(l<=r):
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True
      
s = input('Enter a string : ')
# s = s.lower() # handle case sensitivity 
length = len(s)
ans = is_palindrome(s,0,length-1)
print(ans)