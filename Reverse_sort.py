tc=int(input())
for k in range(tc):
    ll=int(input())
    l=[int(x) for x in input().split()]
    tl=l.copy()
    tl.sort()
    i=0
    cost=0
    while(i<=len(l)-2):
        j=l.index(min(l[i:]))
        cost+=(j-i+1)
        temp=l[i:j+1]
        temp.reverse()
        for x in l:
            if x not in temp:
                temp.insert(l.index(x),x)
        l=temp
        i+=1
    print('Case '+'#'+str(k+1)+':',cost)