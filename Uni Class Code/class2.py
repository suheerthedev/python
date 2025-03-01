result = 0
for i in range(0,10):
    for j in range (0, i):
        result = i * 2
    print(result)
    

for i in range(0, 32):
    fact = 1
    num = i
    while(num > 0):
        fact = num * fact
        num = num - 1
    print(fact)
    
