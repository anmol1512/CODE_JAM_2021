t=int(input())
import itertools
for k in range(t):
    sc=[int(x) for x in input().split()]
    com=itertools.permutations(list(range(1,sc[0]+1)))
    for x in com:
        l=list(x)
        i=0
        cost=0
        while(i<=len(l)-2):
            j=l.index(min(l[i:]))
            cost+=(j-i+1)
            temp=l[i:j+1]
            temp.reverse()
            for t in l:
                if t not in temp:
                    temp.insert(l.index(t),t)
            l=temp
            i+=1
        if cost==sc[1]:
            print('Case '+'#'+str(k+1)+':',*x)
            break
    else:
        print('Case '+'#'+str(k+1)+':','IMPOSSIBLE')