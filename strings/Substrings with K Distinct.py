class Solution:
    def fun(self,s,k):
        left=0
        right=0
        count=0
        d={}
        for right in range(len(s)):
            if s[right] not in d:
                d[s[right]]=1
            else:
                d[s[right]]+=1
            while len(d)>k:
                d[s[left]]-=1
                if d[s[left]]==0:
                    d.pop(s[left])
                left+=1
            count+=right-left+1
        return count
    def countSubstr (self, s, k):
        return self.fun(s,k)-self.fun(s,k-1)
