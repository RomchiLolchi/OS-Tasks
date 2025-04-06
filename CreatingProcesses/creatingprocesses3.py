# Создание процессов, №3 - программа выводит идентификатор родительского и дочернего процесса, с помощью exec запускает
# файл creatingprocesses1.py (внутри этого же процесса), который так же выводит идентификатор родительского и дочернего процесса
# как следствие - PID и PPID не меняются (+ не завершается без ввода пользователя для удобства проверки)
import os
import sys


def print_processes_ids(print_prefix=""):
    print(print_prefix, "\nИдентификатор текущего процесса: ", os.getpid(), "\nИдентификатор родительского процесса: ",
          os.getppid())
    try:
        input("Ожидание любого ввода для завершения\n")
    except EOFError:
        print("")


if __name__ == '__main__':
    print_processes_ids("Начальный процесс, следующий вывод - новый процесс")
    os.execl(sys.executable, "python", os.path.dirname(os.path.realpath(__file__)) + "/creatingprocesses1.py", "")
