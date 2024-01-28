# дано трех значное число 123 найти сумму чисел.Задача 2.

# a=int(input("Введите первое число:"))
# b=int(input("Введите второе число:"))
# c=int(input("Введите третие число:"))
# print(a,"+",b,'+',c,'=',a+b+c)

# num=int(input("Введите трех значное число: "))
# digit1=num//100
# digit2=(num%100)//10
# digit3=num%10

# sum_of_digits=digit1+digit2+digit3
# print(f"Сумма цифр числа {num} равна {sum_of_digits}")

# num = int(input("Введите трехзначное число: "))
# digit_sum = 0
# while num != 0:
#     digit = num % 10
#     digit_sum += digit
#     num //= 10
# print("Сумма цифр:", digit_sum) 

# задача 4

s = int(input("Введите число: "))
sergey = s / 6
petr = sergey
ekaterina = (sergey + petr) * 2
print(int(sergey), int(ekaterina), int(petr))
#---------------------------------------------------

s = int(input("Введите число:")) // 3
print(s // 2, s * 2, s // 2)
#------------------------------------------------

print((a := int(input("Введите число:"))) // 6, a // 6 * 4, a // 6)