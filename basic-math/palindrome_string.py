class Solution:
    def isPalindrome(self, s):
        l=list(s)
        start=0
        end=len(l)-1
        while start<end:
            l[start],l[end]=l[end],l[start]
            start+=1
            end-=1
        rev="".join(l)
        if(rev==s):
            return True
        else:
            return False
