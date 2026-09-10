class Solution:
    def numberOfSubarrays(self, arr, target):
        left=0
        count=0
        h_sum=0
        for right in range(len(arr)):
            h_sum+=arr[right]
            while h_sum>target:
                h_sum-=arr[left]
                left+=1
            if h_sum==target:
                count+=1
                temp=left
                while arr[temp]==0:
                    count+=1
                    temp+=1
        return count
