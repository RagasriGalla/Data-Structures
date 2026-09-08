class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        right=0
        k=2
        d={}
        curr_len=0
        max_len=0
        for right in range(len(fruits)):
            if fruits[right] not in d:
                d[fruits[right]]=1
            else:
                d[fruits[right]]+=1
            while len(d)>2:
                d[fruits[left]]-=1
                if d[fruits[left]]==0:
                    del d[fruits[left]]
                left+=1
            curr_len=right-left+1
            max_len=max(curr_len,max_len)
        return max_len
