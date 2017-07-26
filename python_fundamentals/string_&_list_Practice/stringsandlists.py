
#Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')

#Replace the first instance of a word from a string
words = "It's thanksgiving day. It's my birthday,too!"
print words.replace('day', 'month', 1)

#Find and print the min and max values from a list
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#print the first and the last values in a list and append them to another list

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]

#New list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
x2 = x[:len(x)/2]
x3 = x[len(x)/2:]
print x2
print x3
x3.insert(0, x2)
print x3
