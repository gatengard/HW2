first = int(input(f'введите первое число: '))
second = int(input(f'введите второго число: '))
third = int(input(f'введите третье число: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)