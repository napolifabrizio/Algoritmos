
### Recursão
num = 70

def fat(num):
    if num <= 1:
        return num
    else:
        return fat(num - 1) * num

def fat_loop(num):
    total = 1
    for i in range(1, num+1):
        total *= i
    return total

print(fat_loop(num) == fat(num))