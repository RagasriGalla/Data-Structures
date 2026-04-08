class Solution:
    def maxConsecBits(self, arr):
        max_streak=0
        streak=1
        if(len(arr)==1):
            return 1
        else:
            for i in range(1,len(arr)):
                if(arr[i]==arr[i-1]):
                    streak+=1
                if(streak>max_streak):
                    max_streak=streak
                if(arr[i]!=arr[i-1]):
                    streak=1
            return max_streak
