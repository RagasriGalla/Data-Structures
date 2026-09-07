class Solution:
    def helper(self,s,left,right,max_len,max_pal_str):
        curr_len=right-left+1
        curr_pal_str=s[left:right+1]
        if(curr_len>max_len):
            max_len=curr_len
            max_pal_str=curr_pal_str
        return max_len,max_pal_str
    def getLongestPal(self, s):
        curr_len=0
        curr_pal_str=""
        max_len=0
        max_pal_str=""
        for i in range(len(s)):
            left=i
            right=i
            while left>=0 and right<len(s):
                if(s[left]==s[right]):
                    max_len,max_pal_str=self.helper(s,left,right,max_len,max_pal_str)
                    left-=1
                    right+=1
                else:
                    break
            left=i
            right=i+1
            while left>=0 and right<len(s):
                if(s[left]==s[right]):
                    max_len,max_pal_str=self.helper(s,left,right,max_len,max_pal_str)
                    left-=1
                    right+=1
                else:
                    break
        return max_pal_str
