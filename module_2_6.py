a = int(input(f'что за цифра в первой каменной вставке: '))
parol = ''
for i in range(1, 20):
    for k in range(i + 1, 20):
        if i >= k:
            continue
        elif a % (i + k) == 0:
            parol += f'{i}{k}'
print(f'если в первой каменной вставке цифра {a}, значит во вторую каменную вставку вводи {parol}')