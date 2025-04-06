# Создание процессов, №1 - программа выводит идентификатор текущего и родительского процесса (+ не завершается без ввода
# пользователя для удобства проверки)
import os


def print_processes_ids(print_prefix=""):
    print(print_prefix, "\nИдентификатор текущего процесса: ", os.getpid(), "\nИдентификатор родительского процесса: ",
          os.getppid())
    try:
        input("Ожидание любого ввода для завершения\n")
    except EOFError:
        print("")


if __name__ == '__main__':
    print_processes_ids()
