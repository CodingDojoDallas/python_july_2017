import random

print "Starting the program..."

count = 1
tails = 0
heads = 0

for toss in range(1, 5001):
    flip = random.randint(1,2)
    if flip == 1:
        heads = heads + 1
        print "Attempt #" + str(count) + ": Throwing a coin... It's a head! ...Got " + str(heads) + " heads so far and " + str(tails) + " tail(s) so far"


    else:
        tails = tails + 1
        print "Attempt #" + str(count) + ": Throwing a coin... It's a tail! ...Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"

    count = count + 1
