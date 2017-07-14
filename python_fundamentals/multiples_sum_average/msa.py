
#using a for loop to print all of the odd numbers from 1-1000
oddNum = (i for i in range (1, 1000) if i%2 !=0)
for i in oddNum:
    print i

#using a for loop print all of the multiples of 5 from 5 to 1,000,000
mult5 = (i for i in range (5, 1000000) if i%5==0)
for i in mult5:
    print i

#create a program that prints the sum of all the values from a list
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b

#create program that prints the average of the values in a list
a = [1, 2, 5, 10, 255, 3]
b =sum(a)
print b/len(a)
