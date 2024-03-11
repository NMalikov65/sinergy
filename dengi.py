def investors_can_invest(x, a, b):
    if a >= x and b >= x:
        return 2
    elif a >= x:
        return 'Mike'
    elif b >= x:
        return 'Ivan'
    elif a + b >= x:
        return 1
    else:
        return 0


print(investors_can_invest(100, 150, 200))  # Выводит 2
print(investors_can_invest(100, 50, 200))  # Выводит 'Mike'
print(investors_can_invest(100, 150, 50))  # Выводит 'Ivan'
print(investors_can_invest(100, 50, 50))  # Выводит 1
print(investors_can_invest(100, 50, 40)) # Выводит 0