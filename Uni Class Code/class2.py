import math
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
    
str = "suheer"
countA = 0
countE = 0
countI = 0
countO = 0
countU = 0
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0, len(str)-1):
    count[int(ord(str[i]))-97] += 1
    
for i in range(0, len(str)):
    print(count[int(ord(str[i]))-97])


