prices = [7,1,5,3,6,4]
min = 1000000000
index = 0
max = 0 
for i in range(len(prices)):
    if prices[i]<min:
        min = prices[i]
        index = i
for i in range(index+1,len(prices)):
    if prices[i]>max:
        max = prices[i] 
print(max,min)