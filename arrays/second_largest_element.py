class Solution:
    def getSecondLargest(self, arr):
        large=float('-inf')
        sec_large=float('-inf')
        for i in range(len(arr)):
            if(arr[i]>large):
                sec_large=large
                large=arr[i]
            elif(arr[i]>sec_large and arr[i]!=large):
                sec_large=arr[i]
        if(sec_large==float('-inf')):
            return -1
        else:
            return sec_large
