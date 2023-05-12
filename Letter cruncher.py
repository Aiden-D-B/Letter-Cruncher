word = input("Please enter your first word:")
word2 = input("Please enter your second word:")
wordLen = len(word)
word2Len = len(word2)
firstLetter = word[0]
firstLetter2 = word2[0]
lastLetter = word[-1]
lastLetter2 = word2[-1]
print("The total number of letters is",wordLen+word2Len)
print("The first letters are",firstLetter,"and",firstLetter2)
print("The last letters are",lastLetter,"and",lastLetter2)
