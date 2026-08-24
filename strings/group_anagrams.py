def fun(arr):
    l=[]
    d={}
    for i in range(len(arr)):
        l.append(''.join(sorted(arr[i])))
    for i in range(len(l)):
        if l[i] not in d:
            d[l[i]]=[arr[i]]
        else:
            d[l[i]].append(arr[i])
    return list(d.values())
arr=input().split()
print(fun(arr))
