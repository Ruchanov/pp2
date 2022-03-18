with open('copy.txt','r') as first,open('pp.txt','a') as second:
    for i in first:
        second.write(i)