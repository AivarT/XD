row='--------\n'
col = '  |  |  \n'

xo2 = (
    col +
    row +
    col +
    row +
    col
)

#p=3600 * 24 * 365
n=3


for i in range(n + 1):
    t = 1000
    if i % 2 == 1:
        t = -i
    else:
        t = i / 2
        
    print(i) 
    
n=215496
for i in range(n-1, n+1):
    print(i)
   
print(xo2)

row ='--------'
col = '  |  |  '

n=8
for p in range(n+1):
    o=row
    l=col
#     print('--- ', p)
    if p%2==1 :
        print(o)
    else:
        print(l)
