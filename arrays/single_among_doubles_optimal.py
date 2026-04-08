#User function Template for python3
class Solution:
    def search(self, n, arr):
        n=len(arr)
        low=0
        high=n-1
        while low<high:
            mid=(low+high)//2
            if(mid%2!=0):
                mid-=1
            if(arr[mid]==arr[mid+1]):
                low=mid+2
            else:
                high=mid
        return arr[low]
