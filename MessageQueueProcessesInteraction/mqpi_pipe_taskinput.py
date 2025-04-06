# Взаимодействие процессов (очередь сообщений), №1 (Вар. 1) - программа, принимающая задания на вычисление и передающая их
# второй программе посредством именованного канала. Запускается этот и второй файл. Обработка пользовательских ошибок
# не предусмотрена!! Работа нескольких инстансов программы невозможна
import os
import signal


def close_on_exit(sig, frame):
    if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/calculator_pipe"):
        os.remove(os.path.dirname(os.path.realpath(__file__)) + "/calculator_pipe")
    exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, close_on_exit)
    if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/calculator_pipe"):
        os.mkfifo(os.path.dirname(os.path.realpath(__file__)) + "/calculator_pipe")
    print("Готов к работе")
    while True:
        with open(os.path.dirname(os.path.realpath(__file__)) + "/calculator_pipe", "w") as pipe:
            pipe.write(input("\nВведите пример для решения (например: 2 + 3 / 3, 7 * 5 - 8, 2 * 4): "))
            print("\nПолучено, передача...")
