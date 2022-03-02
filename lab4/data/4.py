from datetime import datetime
y,m,d,h,mi,s=map(int,input().split())
g,me,de,ch,min,sec=map(int,input().split())
d=datetime(y,m,d,h,mi,s)
d2=datetime(g,me,de,ch,min,sec)
print((d-d2).total_seconds())