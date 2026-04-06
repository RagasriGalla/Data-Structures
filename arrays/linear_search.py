class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if(x==arr[i]):
                return i
        return -1
