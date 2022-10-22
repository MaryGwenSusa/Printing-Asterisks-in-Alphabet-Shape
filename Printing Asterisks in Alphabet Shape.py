printK = [[" " for colNum in range(5)] for rowNum in  range(7)] 
firstCol=0
lastCol=4
for row in range(7):
    for col in range(5):
        if col==0 or (row==col+2 and col>1):
            printK[row][col] = "*" 
        elif ((row==firstCol and col==lastCol) and col>0):
            printK[row][col] = "*" 
            firstCol=+1
            lastCol=-1  

printA = [[" " for colNum in range(5)] for rowNum in  range(7)]
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            printA[row][col] = "*"


printT = [[" " for colNum in range(5)] for rowNum in  range(7)]
for row in range(7):
    for col in range(5):
        if col==2 or (row==0 and col!=2):
            printT[row][col] = "*"

for rowPattern in range(7):
    for colPattern in range(5):
        print(printK[rowPattern][colPattern], end = " ")
    print(end=" ")
    for colPattern in range(5):
        print(printA[rowPattern][colPattern], end = " ")
    print(end=" ")
    for colPattern in range(5):
        print(printT[rowPattern][colPattern], end = " ")
    print(end=" ")
    for colPattern in range(5):
        print(printA[rowPattern][colPattern], end = " ")
    print()