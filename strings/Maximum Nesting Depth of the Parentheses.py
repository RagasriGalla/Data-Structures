class Solution:
    def maxDepth(self, s):
        # code here
        curr_depth=0
        max_depth=0
        i=0
        while i<len(s):
            if(s[i]=="("):
                curr_depth+=1
                max_depth=max(curr_depth,max_depth)
            if(s[i]==")"):
                curr_depth-=1
            i+=1
        return max_depth
