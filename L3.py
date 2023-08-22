# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов

def pluralize_percent(number):
    if 11 <= number <= 14:
        return "процентов"
    last_digit = number % 10
    if last_digit == 1:
        return "процент"
    elif 2 <= last_digit <= 4:
        return "процента"
    else:
        return "процентов"

for number in range(1, 101):
    print(f"{number} {pluralize_percent(number)}")
