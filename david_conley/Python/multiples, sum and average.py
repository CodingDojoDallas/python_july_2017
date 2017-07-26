for x in range (1,1001):
    if x % 2 == 1:
        print x

for x in range (5, 1000005):
    if x % 5 == 0:
        print x

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum

my_numbers = [1, 2, 5, 10, 255, 3]
print sum(my_numbers)/len(my_numbers)
