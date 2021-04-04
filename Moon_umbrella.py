import re
t=int(input())
for k in range(t):
    tcl=[int(x) if x.isdigit() else x for x in input().split()]
    mural=tcl[2]
    mural=mural.replace('?','x')
    cost=mural.count('CJ')*tcl[0]+mural.count('JC')*tcl[1]+mural.count('CxJ')*tcl[0]+mural.count('JxC')*tcl[1]+len(re.findall("Cxx+J", mural))*tcl[0]+len(re.findall("Jxx+C", mural))*tcl[1]
    print('Case '+'#'+str(k+1)+':',cost)
        