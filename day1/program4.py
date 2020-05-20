cost = int(input("Enter the cost price "))
sell = int(input("Enter the selling price "))

#profit
profit = sell -cost
print(profit)
new_sell = profit*1.05 + cost
print(int(new_sell))
