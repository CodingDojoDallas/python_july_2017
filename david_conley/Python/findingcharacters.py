wordList = ["hello","people","paul","is","silly"]
char = "p"
newList = []
for item in wordList:
  if char in item:
    newList.append(item)
print newList    
