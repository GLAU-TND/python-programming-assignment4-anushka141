a=input()
b=list(map(str,input().split()))
c=[]
for i in b:
    if i.startswith(a):
        c.append(i)
print(c)

        
    
