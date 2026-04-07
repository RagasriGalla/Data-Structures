class Solution:
    def findUnion(self, a, b):
        i=0
        j=0
        res=[]
        while i<len(a) and j<len(b):
            if(a[i]<b[j]):
                if(len(res)==0 or res[-1]!=a[i]):
                    res.append(a[i])
                i+=1
            elif(b[j]<a[i]):
                if(len(res)==0 or res[-1]!=b[j]):
                    res.append(b[j])
                j+=1
            else:
                if(len(res)==0 or res[-1]!=b[j]):
                    res.append(b[j])
                i+=1
                j+=1
        while i<len(a):
            if(len(res)==0 or res[-1]!=a[i]):
                res.append(a[i])
            i+=1
        while j<len(b):
            if(len(res)==0 or res[-1]!=b[j]):
                res.append(b[j])
            j+=1
        return res
