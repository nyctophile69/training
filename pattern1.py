n=int(input())
for i in range (0,n):
    for j in range(0,n):
        print("*",end=" ")
    print()

print("2")
for k in range(n,0,-1):
    for t in range(k,0,-1):
        print(t,end=" ")
    print()