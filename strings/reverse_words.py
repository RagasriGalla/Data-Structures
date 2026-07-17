class Solution:
    def reverseWords(self, s):
        # code here
        ans=""
        last=len(s)-1
        while last>=0:
            while last>=0 and s[last]==".":
                last-=1
            if last<0:
                break
            end=last
            while last>=0 and s[last]!=".":
                last-=1
            word=s[last+1:end+1]
            if ans=="":
                ans+=word
            else:
                ans+="."+word
        return ans
