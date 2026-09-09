class Solution:
    def longestSubstr(self, s, k):
        left=0
        right=0
        d={}
        max_val=0
        max_ans=0
        for right in range(len(s)):
            if s[right] not in d:
                d[s[right]]=1
            else:
                d[s[right]]+=1
            for key in d:
                val=d[key]
                if val>max_val:
                    max_val=val
            needed=(right-left+1)-max_val
            while needed>k:
                d[s[left]]-=1
                if d[s[left]]==0:
                    del d[s[left]]
                left+=1
                needed=(right-left+1)-max_val
            curr_ans=right-left+1
            max_ans=max(curr_ans,max_ans)
        return max_ans
