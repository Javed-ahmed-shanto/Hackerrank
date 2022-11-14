N, M = map(int, input().split())

j= 0
n =[]

for i in range(1, N+1, 1):
    if(i<((N/2)+0.5)):
        print((".|."*(i+j)).center(M, "-")) # to print
        n.append((".|."*(i+j)).center(M, "-")) # to append in the list so that it can be poped out
        j=j+1
    elif(i==((N/2)+0.5)): # in the middle part when it become half
        print("WELCOME".center(M, "-"))
    else:
        print(n.pop()) # to pop out the last half from appended a
