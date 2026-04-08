#User function Template for python3
class Solution:
    def search(self, n, arr):
        for i in range(len(arr)-1):
            if(i%2==0):
                if(arr[i]!=arr[i+1]):
                    return arr[i]
            else:
                if(arr[i]!=arr[i-1]):
                    return arr[i]
        return arr[-1]
