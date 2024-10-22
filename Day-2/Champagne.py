def champagne(row, poured, glass):
    glasses=[[0]* (i+1) for i in range(101)]
    glasses[0][0]=poured
    for i in range(100):
        for j in range(i+1):
            if glasses[i][j]>1:
                overflow=glasses[i][j]-1
                glasses[i][j]=1
                glasses[i+1][j]+overflow/2
                glasses[i+1][j+1]+=overflow/2
    return min(1, glasses[row][glass])
print(champagne(1,1,1))
print(champagne(1,2,1))
print(champagne(1,3,1))
print(champagne(2,4,0))
