t=int(input())
for k in range(t):
    n=int(input())
    l=[int(x) for x in input().split()]
    cost=0
    for i in range(1,n):
        if l[i-1]>l[i]:
            diff=len(str(l[i-1]))-len(str(l[i]))
            x=str(l[i-1])[-diff:]
            if l[i]>int(str(l[i-1])[:len(str(l[i]))]):
                l[i]=int(str(l[i])+x)
                cost+=diff
            else:
                l[i]=int(str(l[i])+x+'0')
                cost+=diff+1
        elif l[i-1]==l[i]:
            l[i]=int(str(l[i])+'0')
            cost+=1
    print('Case '+'#'+str(k+1)+':',cost)