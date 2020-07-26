percent = float(input("Interest %: "))
Interest = float((percent + 100) / 100)
money = float(input("How much did you originally have in the bank?"))
num_years = float(input("How many years do you want it in the bank?"))
Total_money = float((Interest ** num_years) * money)
dream = float(input("Money Goal: "))
while Total_money < dream:
    print([Total_money, num_years])
    num_years += 1
    Total_money *= Interest
    if Total_money >= 1000000:
        break
    print([Total_money, num_years])















