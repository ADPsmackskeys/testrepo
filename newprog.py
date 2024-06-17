og,n=input().split()
og=int(og)
n=int(n)
win={}

for i in range(n):
    st,gain=input().split()
    st=int(st)
    gain=int(gain)
    win[st]=gain
l=list(win.items())
l.sort()
win=dict(l)
    
for i in range(len(win.items())-1):
    if og>list(win.keys())[i]:
        og+=list(win.values())[i]

if og>list(win.keys())[-1]:
    print('YES')
else:
    print('NO')