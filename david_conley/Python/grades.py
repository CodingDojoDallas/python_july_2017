import random
number = random.randint(1,100)
score = str(number)

if score in range(60, 70):
    print "Score: " + score + "; Your grade is a D"

elif score in range(70, 80):
    print "Score: " + score + "; Your grade is a C"

elif score in range(80, 90):
    print "Score: " + score  + "; Your grade is a D"

else:
    print "Score: " + score + "; Your grade is a D"

    print "End of the program. Bye!"
