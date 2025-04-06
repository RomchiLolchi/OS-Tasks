# Взаимодействие процессов (очередь сообщений), №2 (Вар. 1) - программа, решающая задания на вычисление, полученные от
# первой программы посредством именованного канала. Запускается этот и второй файл. Обработка пользовательских ошибок
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
        with open(os.path.dirname(os.path.realpath(__file__)) + "/calculator_pipe", "r") as pipe:
            task = pipe.read()
            print("\nПолучено: ", task, ". Результат: ", eval(task))
