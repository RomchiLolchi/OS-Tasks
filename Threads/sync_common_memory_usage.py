# Синхронизация обращения к общей памяти - программа принимает количество потоков на создание и создаёт их;
# потоки в цикле увеличивают значение глобальной переменной на 1 за каждую итерацию. Отличие от creatingthreadsformath.py -
# наличие синхронизации
import threading

global_variable = 0
thread_lock = threading.Lock()


def thread_task(thread_number):
    global global_variable, thread_lock
    thread_lock.acquire()
    for j in range(0, 1000000):
        global_variable += 1
    print(f"Поток {thread_number} завершил работу, global_variable={global_variable}")
    thread_lock.release()


if __name__ == "__main__":
    thread_amount = int(input("Введите количество потоков для создания: "))
    for i in range(0, thread_amount):
        thread = threading.Thread(target=thread_task, args=(i + 1,))
        thread.start()
