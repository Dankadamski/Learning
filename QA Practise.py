user = int(input("Add a maximum number: "))
x = 1
while x <= user:
    print(x, x * x)
    x += 1
    if x > user:
        break
