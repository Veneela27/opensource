x,y,z=map(int,input().split())
time=z*24*60
tneed=x*y
if tneed<=time:
    print("YES")
else:
    print("NO")
