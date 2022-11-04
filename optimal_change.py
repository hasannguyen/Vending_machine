import math

def optimal_change(item_cost,amount_paid):
    
    amount_change = round(amount_paid - item_cost,2)

    if amount_paid < item_cost:
        return 'Must provide more money.'
    elif amount_paid == item_cost:
        return 'Exact amount was paid, no change is needed.'

    change_output = f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is'

    change_map = {}

    denominations_map = {
    '$100 bill': 100,
    '$50 bill': 50,
    '$20 bill': 20,
    '$10 bill': 10,
    '$5 bill': 5,
    '$1 bill': 1,
    'quarter': 0.25,
    'dime': 0.1,
    'nickel': 0.05,
    'pennie':0.01
    }
    
    for key in denominations_map:
        if math.floor(round(amount_change,2)/denominations_map[key])>0:
            count = math.floor(round(amount_change,2)/denominations_map[key])
            change_map[key]= count
            amount_change = round(amount_change,2)%denominations_map[key]

    map_length = len(change_map)

    if map_length == 1:
        for key in change_map:
            if key == 'pennie' and change_map[key] == 1:
                change_output += f' {change_map[key]} penny'
            elif change_map[key]>1:
                change_output += f' {change_map[key]} {key}s'
            else:
                change_output += f' {change_map[key]} {key}'

    while map_length>1:
        for key in change_map:
            map_length -= 1
            if map_length != len(change_map) -1:
                change_output += ','
            if map_length == 0:
                change_output += ' and'
            if key == 'pennie' and change_map[key] == 1:
                change_output += f' {change_map[key]} penny'
            elif change_map[key] > 1:
                change_output += f' {change_map[key]} {key}s'
            else:
                change_output += f' {change_map[key]} {key}'

    return change_output + '.'

