def longestCommonPrefix(strs):
        test = strs[0]
        b= True
        res = ''
        answer = ''
        for i in test:
            res += i 
            print(res)
            for j in range(len(strs)):
                if res not in strs[j]:
                    b = False
                    return answer
            if res == True:
                res = answer

print(longestCommonPrefix(["flower","flow","flight"]))