num=int(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        if i*j==num and i != 1:
            d=0
            for k in range(2,i):
                if i%k==0:
                    d=d+1
            if d==0:
                print(i,end=" ")
