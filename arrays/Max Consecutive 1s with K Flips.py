class Solution:
    def maxOnes(self, arr, k):
        left=0
        right=0
        zero_count=0
        curr_len=0
        max_len=0
        for right in range(len(arr)):
            if arr[right]==0:
                zero_count+=1
            while zero_count>k:
                if arr[left]==0:
                    zero_count-=1
                left+=1
            curr_len=right-left+1
            max_len=max(curr_len,max_len)
        return max_len
