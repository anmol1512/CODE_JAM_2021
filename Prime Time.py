import math
t=int(input())
for k in range(t):
    m=int(input())
    decklist=[]
    maxscore=[]
    for i in range(m):
        p,n=[int(x) for x in input().split()]
        decklist.extend((p,)*n)
    if m>1:
        for i in range(0,len(decklist)-1):
            for j in range(i+1,len(decklist)):
                if sum(decklist)-(decklist[i]+decklist[j])==decklist[i]*decklist[j]:
                    maxscore.append(decklist[i]*decklist[j])
    elif m==1:
        pro=1
        s=sum(decklist)
        for t in range(len(decklist)):
            pro*=decklist[t]
            s=s-decklist[t]
            if s==pro:
                maxscore.append(s)
    if not(bool(maxscore)):
        print('Case '+'#'+str(k+1)+':',0)
        continue
    else:
        print('Case '+'#'+str(k+1)+':',max(maxscore))

        
