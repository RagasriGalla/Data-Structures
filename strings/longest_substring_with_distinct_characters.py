class Solution:
    def longestUniqueSubstr(self, s):
        left=0
        right=0
        curr_len=0
        max_len=0
        h_set=set()
        for right in range(len(s)):
            while s[right] in h_set:
                h_set.remove(s[left])
                left+=1
            h_set.add(s[right])
            curr_len=right-left+1
            max_len=max(curr_len,max_len)
        return max_len
