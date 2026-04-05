class Solution:
    def armstrongNumber (self, n):
        ans=0
        temp=n
        while n>0:
            d=n%10
            ans+=d**(len(str(temp)))
            n//=10
        if(ans==temp):
            return True
        else:
            return False
