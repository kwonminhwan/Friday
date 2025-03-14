n=int(input())
lst=list(map(int,input().split()))
Max_lst=[-28e8]*(n+2)
for i in range(2,n+2):
    if i==n+1:
        ret1=Max_lst[i-2]
        ret2=Max_lst[i-6]
    else:
        if i-2==0:
            ret1=lst[i-1]
            ret2=-28e8
        elif i-2>0 and i-7<0:
            ret1=lst[i-1]+Max_lst[i-2]
            ret2=-28e8
        elif i-2>0 and i-7>0:
            ret1=lst[i-1]+Max_lst[i-2]
            ret2 = lst[i - 1] + Max_lst[i - 7]
        if i-7==0:
            ret2=lst[i-1]
            ret1=-28e8

    Max=max(ret1,ret2)
    if Max>Max_lst[i]:
        Max_lst[i]=Max
result=-28e8
for i in range(n-6,n+2):
    if result<Max_lst[i]:
        result=Max_lst[i]
print(result)