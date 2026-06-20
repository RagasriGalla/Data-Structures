class Solution:
    def largestOddNumber(self, num: str) -> str:
        end=-1
        for i in range(len(num)-1,-1,-1):
            if(int(num[i])%2!=0):
                end=i
                break
        if end==-1:
            return ""
        start=0
        while start<=end and num[start]=='0':
            start+=1
        return num[start:end+1]
