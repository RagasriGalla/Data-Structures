class Solution:
    def frequencySort(self, s):
        ans=""
        d={}
        l=[]
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        for key in d:
            val=d[key]
            l.append((val,key))
        l.sort()
        for i in range(len(l)):
            val=l[i][0]
            key=l[i][1]
            ans+=key*val
        return ans
