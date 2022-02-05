x=int(input())
while x>0:
    y=int(input())
    if y<=10:
        print("Go to work!")
    if y>10 and y<=25:
        print("You are weak")
    if y>25 and y<=45:
        print("Okay, fine")
    if y>45:
        print(" Burn! Burn! Burn Young!")
    x-=1