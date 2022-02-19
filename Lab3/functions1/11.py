def palindrome(s):
    res=True
    if s[::-1]==s:
        return res
    else:
        res=False
        return res
print(palindrome(input()))