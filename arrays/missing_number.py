class Solution:
    def missingNum(self, arr):
        n=max(arr)
        original=0
        total=0
        original=(n*(n+1)//2)
        for i in range(len(arr)):
            total+=arr[i]
        ans=original-total
        if(ans==0):
            return max(arr)+1
        else:
            return ans
