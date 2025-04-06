# Взаимодействие процессов (очередь сообщений), №2 (Вар. 2) - программа, решающая задания на вычисление, полученные от
# первой программы посредством переданного объекта очереди. Обработка пользовательских ошибок не предусмотрена!!
# Этот файл запускается в автоматическом режиме!! Работа нескольких инстансов поддерживается
import os
import signal
from multiprocessing import Queue


def notify_on_exit(sig, frame):
    print("\nПроизошло завершение второй программы")
    exit(0)


signal.signal(signal.SIGINT, notify_on_exit)
queue: Queue = globals()["queue"]
print("\nВторая программа запущена и готова к работе, pid: ", os.getpid())
while True:
    task = queue.get(block=True)
    print("\nПолучено: ", task, ". Результат: ", eval(task))
