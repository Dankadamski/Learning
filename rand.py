numbers = [10, 11, 12, 13, 14, 15]
all_result = all(x % 2 == 0 for x in numbers)
print("Are all the numbers even: ", all_result)
any_result = any(x % 2 == 0 for x in numbers)
print("Are any of the numbers even: ", any_result)

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
odd_numbers = [x for x in numbers if x % 2 == 1]
print(odd_numbers)
