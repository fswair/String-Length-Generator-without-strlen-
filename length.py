myString = "GITHUB.COM/FSWAIR | @FLUSWAIR"
myList = []
myNumList = []

for i in myString:
  myList.append(i)
for j in myList:
    
    myNumList.append(myList.index(j))
    

getResult = max(myNumList)
print((getResult + 1))
