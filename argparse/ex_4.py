import argparse

parser = argparse.ArgumentParser()
parser.add_argument("source_file", help="имя файла-источника")
parser.add_argument("destination_file", help="имя файла-приемника")
parser.add_argument("--upper", action="store_true", help="привести текст к верхнему регистру")
parser.add_argument("--lines", type=int, help="скопировать только первые N строк")
args = parser.parse_args()

with open(args.source_file, "r") as source:
    if args.lines:  # если указано количество строк для копирования
        lines = source.readlines()[:args.lines]  # читаем только нужное количество строк
    else:
        lines = source.readlines()  # читаем все строки файла
    if args.upper:  # если нужно привести текст к верхнему регистру
        lines = [line.upper() for line in lines]

with open(args.destination_file, "w") as destination:
    destination.writelines(lines)  # записываем строки в файл-приемник
