t=int(input())
for k in range(t):
    n=int(input())
    l=[int(x) for x in input().split()]
    cost=0
    for i in range(1,n):
        if l[i-1]>=l[i]:
            diff=len(str(l[i-1]))-len(str(l[i]))
            x=str(l[i-1])[-diff:]
            if diff>0:
                if l[i]>int(str(l[i-1])[:len(str(l[i]))]):
                    l[i]=l[i]*(10**len(x))
                    cost+=len(x)
                elif l[i]==int(str(l[i-1])[:len(str(l[i]))]):
                    x=str(int(x)+1)
                    l[i]=int(str(l[i])+x)
                    cost+=len(x)
                else:
                    l[i]=(l[i]*(10**len(x)))*10
                    cost+=len(x)+1
            else:
                l[i]=l[i]*10
                cost+=1
                    
    print('Case '+'#'+str(k+1)+':',cost)