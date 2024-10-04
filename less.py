num1 = int(input("Enter your first number: ")) #Ожидаю первое число от пользователя

while True:
    num2 = int(input("Enter your second number: "))
    if num2 == 0:
        print("You can't divide by 0! Try again.")
    else: break
#В этом действие число "0" не будет в решение, програма выдаст ошибку и попросит пользователя ввести число еще раз
result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2
#Решение num1 и num2, придавая им переменную
print(f"{num1} + {num2} = {result1}")
print(f"{num1} - {num2} = {result2}")
print(f"{num1} * {num2} = {result3}")
print(f"{num1} / {num2} = {result4}")
#Выписывает целый пример с ответом
