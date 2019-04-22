a = 4736
b = 9245
odd_sum = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        odd_sum += i
print(odd_sum)
