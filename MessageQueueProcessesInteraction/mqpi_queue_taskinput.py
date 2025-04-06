# Взаимодействие процессов (очередь сообщений), №1 (Вар. 2) - программа, запускающая "сервер" (т.е. вторую программу) и
# принимающая задания на вычисление и передающая их второй программе посредством очереди сообщений.
# Обработка пользовательских ошибок не предусмотрена!! Запускается только этот файл, второй запускается в автоматическом
# режиме. Работа нескольких инстансов поддерживается
import signal
from multiprocessing import Process, Queue
import os

process: Process


def end_second_on_exit(sig, frame):
    print("\nВыход и завершение второй программы...")
    process.kill()
    exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, end_second_on_exit)
    queue = Queue()
    print("\nЗапуск второй программы...")
    process = Process(
        target=lambda: exec(open(os.path.dirname(os.path.realpath(__file__)) + "/mqpi_queue_taskprocessing.py").read(),
                            {"queue": queue}))
    process.start()
    print("\nГотов к работе, pid приёмника: ", os.getpid())
    while True:
        queue.put(input("\nВведите пример для решения (например: 2 + 3 / 3, 7 * 5 - 8, 2 * 4): "))
        print("\nПолучено, передача...")
