# Создание процессов, №2 - программа создаёт копию самой себя и выводит идентификатор родительского и дочернего процесса
# (+ не завершается без ввода пользователя для удобства проверки)
import os


def print_processes_ids(print_prefix=""):
    print(print_prefix, "\nИдентификатор текущего процесса: ", os.getpid(), "\nИдентификатор родительского процесса: ", os.getppid())
    try:
        input("Ожидание любого ввода для завершения\n")
    except EOFError:
        print("")


if __name__ == '__main__':
    forkPid = os.fork()
    if forkPid == 0:
        print_processes_ids("Дочерний процесс:")
    elif forkPid > 0:
        print_processes_ids("Родительский процесс:")
    else:
        print("Ошибка fork")
