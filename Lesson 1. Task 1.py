# https://drive.google.com/file/d/1yS-thd1FTY8AUm_kdyE5IK6pE8BgHXRT/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь
n = int(input("Введите трехзначное число: "))
a1 = n % 10
a2 = n % 100 // 10
a3 = n // 100

print("Сумма цифр числа:", a1 + a2 + a3)
print("Произведение цифр числа:", a1 * a2 * a3)