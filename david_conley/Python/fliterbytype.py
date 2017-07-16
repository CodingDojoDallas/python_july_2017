sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

currentt_test = lL

typ_tester = type(current_test)
if typ_tester is int:
    if typ_tester >= 100:
        print "Thats a big number"
    else:
        print "thats a small number"
elif typ_tester is str:
    if len(typ_tester) >= 50:
        print "Long sentence"
    else:
        print "Short sentence"
elif isinstance(current_test, list):
    if len(current_test) >= 10:
        print "big list"
    else:
        print "Short list"
