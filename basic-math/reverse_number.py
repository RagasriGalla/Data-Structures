class Solution:
	def reverseDigits(self, n):
	    ans=0
	    while n>0:
	        d=n%10
	        ans=ans*10+d
	        n=n//10
	    return ans
