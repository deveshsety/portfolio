primary_diagonal = 0
secondary_diagonal = 0
R = C = int(input())
mat = [[int(input()) for x in range(C)] for y in range(R)]
for i in range(0,R):
    primary_diagonal += mat[i][i]
    secondary_diagonal += mat[i][R-i-1]
if primary_diagonal == secondary_diagonal :
    print(1)
else :
    print(0)