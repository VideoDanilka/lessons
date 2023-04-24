import sys

# проверяем, что передан аргумент с именем файла
filename = ''
if len(sys.argv) <= 0:
    print("ERROR")
    sys.exit()
else:
    for arg in sys.argv[1:]:
        if '.txt' in arg:
            filename = arg

# проверяем, что файл существует
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("ERROR")
    sys.exit()

# обработка дополнительных аргументов
sort_lines = False
numbered_lines = False
count_lines = False

for arg in sys.argv[1:]:
    if arg == '--sort':
        sort_lines = True
    elif arg == '--num':
        numbered_lines = True
    elif arg == '--count':
        count_lines = True

# сортировка строк
if sort_lines:
    lines.sort()

# вывод строк
if numbered_lines:
    for i, line in enumerate(lines):
        line = str.strip(line)
        print(f"{i} {line}")
else:
    for line in lines:
        line = str.strip(line)
        print(line)

# вывод кол-ва строк
if count_lines:
    print(f"rows count: {len(lines)}")
