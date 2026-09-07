class Solution:
    def beautySum(self, s: str) -> int:
        ans=0
        beauty=0
        for i in range(len(s)):
            d={}
            for j in range(i,len(s)):
                if s[j] not in d:
                    d[s[j]]=1
                else:
                    d[s[j]]+=1
                max_freq=None
                min_freq=None
                for key in d:
                    val=d[key]
                    if min_freq is None:
                        min_freq=val
                        max_freq=val
                    else:
                        if val<min_freq:
                            min_freq=val
                        if val>max_freq:
                            max_freq=val
                beauty=max_freq-min_freq
                ans+=beauty
        return ans
