# ЗАДАЧА 15
# доно число арбузов найти из этого числа самое большое исамое маленькое.

#input 5->5 1 6 5 9
#output 1 9

n=int(input())
max= -1
min= 30001
for i in range(n):
    x=int(input())
    if x > max:
        max=x
    if x<min:
        min=x
print(max, min)            