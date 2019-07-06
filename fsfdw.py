k,n=map(int,input().split())
for s in range(k+1,n):
    sum=0
    num=s
    while num>0:
        dig=num%10
        sum+=dig**3
        num//=10
        if(s==sum):
            print(s,end=" ")
