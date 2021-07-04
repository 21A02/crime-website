n=4
m=20

while(n<m):
    i=2
    
    while(i<n):
        
        if n%i==0:
            break
        
        i=i+1
    
    if n==i:
        print(n)
    
    n=n+1
    #print("test",n,m)
        