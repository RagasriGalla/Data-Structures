def fun(arr,target):
    d={0:1}
    prefix=[]
    ans=0
    prefix.append(arr[0])
    for i in range(1,len(arr)):
        prefix.append(arr[i]+prefix[i-1])
    for i in range(len(prefix)):
        needed=prefix[i]-target
        if needed in d:
            ans+=d[needed]
        if prefix[i] not in d:
            d[prefix[i]]=1
        else:
            d[prefix[i]]+=1
    return ans
arr=list(map(int,input().split()))
target=int(input())
print(fun(arr,target))
