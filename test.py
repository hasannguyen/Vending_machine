
item_cost = 50
amount_paid = 32


test_str = f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is'

test = {
# '$10 bill': 1,
# '$1 bill': 2,
# 'quarter': 1,
'dime': 1,
# 'pennie': 2
   }


count = len(test)

#find way to implement commas. 

print(count)


#implementing if there's one denomination left, and if that denomination is  more than 1 or if it is a penny
if count == 1:
    for key in test:
        if key == 'pennie' and test[key] == 1:
            test_str += f' {test[key]} penny'
        elif test[key]>1:
            test_str += f' {test[key]} {key}s'
        else:
            test_str += f' {test[key]} {key}'

while count>1:

    if count>1:
        for key in test:
            count -= 1

            if count != len(test) -1:
                test_str += ','

            if count == 0:
                test_str += ' and'

            if key == 'pennie' and test[key] == 1:
                test_str += f' {test[key]} penny'
            elif test[key] > 1:
                test_str += f' {test[key]} {key}s'
            else:
                test_str += f' {test[key]} {key}'

print(test_str)