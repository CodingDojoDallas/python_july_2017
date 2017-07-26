words = "It's thanksgiving day. It's my birthday,too!"
words = words.find('day')
print words
18

words = "It's thanksgiving day. It's my birthday,too!"
words = words.replace("day", "month")
print words

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[7]
"hello" "world"
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[7]
new_x = [x[0], x[7]]
print new_x
['hello', 'world']

 x = [19,2,54,-2,7,12,98,32,10,-3,6]
 x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[:len(x)/2] # optional first parameter of slice defaults to zero
second_list = x[len(x)/2:] # optional second parameter of slice defaults to the list's length
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list
