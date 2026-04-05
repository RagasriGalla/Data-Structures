class Solution:
    def largest(self, arr):
        large=float('-inf')
        for i in arr:
            if i>large:
                large=i
        return large
