class Solution:
    def isBalanced(self, s):
        stack=[]
        pairs={
            "}":"{",
            ")":"(",
            "]":"["
        }
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                stack.append(s[i])
            elif s[i]==")" or s[i]=="}" or s[i]=="]":
                if len(stack)==0 or stack[-1]!=pairs[s[i]]:
                    return False
                stack.pop()
            else:
                return False
        return len(stack)==0
        
