# n=int(input())
# for i in range(n):
#     print(' '*i)
#     for k in range(i):
#         print(" ",end='')
#     for j in range(n-i):
#         print(n-j-i,end=' ')
#     print()
for x in range(5,0,-1):
    for y in range(x,5):
        print(" ",end=" ")
    for z in range(x,0,-1):
        print(z,end=" ")
    print()
