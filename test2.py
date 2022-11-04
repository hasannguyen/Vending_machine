testdict = {
    'shoe': 5,
    'apple': 5,
    'nike' :2
}

del testdict['shoe']

for key in testdict.copy():

    if len(testdict) == 2:
        print(testdict)
        testdict.pop(key)
        print(testdict)
print(testdict)