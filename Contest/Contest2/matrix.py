size=int(input())
arr=[]
c=[]
for i in range(size):
    arr.append(list(map(int,input().split())))
result_matrix = [[0 for i in range(size)] for i in range(size)]
for i in range(size):
  for j in range(size):
    for k in range(size):
       result_matrix[i][j] += arr[i][k] * arr[k][j]
if result_matrix == arr:
    print('Good matrix')
else:
    print('Bad matrix')