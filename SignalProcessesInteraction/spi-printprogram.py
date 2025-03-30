# Использование сигналов для взаимодействия процессов, №1 - программа бесконечно выводит свой pid и заданную строку
# с перерывом в секунду. После получения сигналов, вывод меняется. Поддерживается завершение работы программы через
# SIGINT
import signal
import os
from time import sleep

pid = os.getpid()
output_str = "pid: {}, Стандартный вывод - не было получено сигналов".format(pid)
exit_flag = False

def signal_processor(incoming_signal, frame):
    global output_str, exit_flag
    if incoming_signal == signal.SIGUSR1:
        output_str = "pid: {}, Получен SIGUSR1!".format(pid)
    elif incoming_signal == signal.SIGUSR2:
        output_str = "pid: {}, Получен SIGUSR2!".format(pid)
    elif incoming_signal == signal.SIGINT:
        output_str = "pid: {}, Получен SIGINT, завершение работы программы...".format(pid)
        exit_flag = True


if __name__ == "__main__":
    signal.signal(signal.SIGUSR1, signal_processor)
    signal.signal(signal.SIGUSR2, signal_processor)
    signal.signal(signal.SIGINT, signal_processor)
    while True:
        print(output_str, "\n")
        if exit_flag:
            exit(0)
        sleep(1)
