class String():
    def __init__(self,s):
        self.s=s
    def st(self):
        return self.s
    def upper(self):
        return self.s.upper()
s=input()
s=String(s)
print(s.st())
print(s.upper())
