from optimal_change import optimal_change

#Normal test cases
print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
print("3:", optimal_change(0.30, 500) == "The optimal change for an item that costs $0.3 with an amount paid of $500 is 4 $100 bills, 1 $50 bill, 2 $20 bills, 1 $5 bill, 4 $1 bills, 2 quarters, and 2 dimes.")
print("4:", optimal_change(29.41, 41) == "The optimal change for an item that costs $29.41 with an amount paid of $41 is 1 $10 bill, 1 $1 bill, 2 quarters, 1 nickel, and 4 pennies.")
print("5:", optimal_change(87.21, 94.32) == "The optimal change for an item that costs $87.21 with an amount paid of $94.32 is 1 $5 bill, 2 $1 bills, 1 dime, and 1 penny.")
print("6:", optimal_change(4.31, 94.13) == "The optimal change for an item that costs $4.31 with an amount paid of $94.13 is 1 $50 bill, 1 $20 bill, 1 $10 bill, 1 $5 bill, 4 $1 bills, 3 quarters, 1 nickel, and 2 pennies.")
print("7:", optimal_change(0.59, 4.32) == "The optimal change for an item that costs $0.59 with an amount paid of $4.32 is 3 $1 bills, 2 quarters, 2 dimes, and 3 pennies.")
#Edge/special cases including exact amount, not enough, and single denominations
print("8:", optimal_change(13.41, 10) == "Must provide more money.")
print("9:", optimal_change(32, 32) == "Exact amount was paid, no change is needed.")
print("11:", optimal_change(42, 43) == "The optimal change for an item that costs $42 with an amount paid of $43 is 1 $1 bill.")
print("12:", optimal_change(21.12, 31.12) == "The optimal change for an item that costs $21.12 with an amount paid of $31.12 is 1 $10 bill.")
print("13:", optimal_change(11.12, 11.13) == "The optimal change for an item that costs $11.12 with an amount paid of $11.13 is 1 penny.")
print("14:", optimal_change(0.05, 0.08) == "The optimal change for an item that costs $0.05 with an amount paid of $0.08 is 3 pennies.")
