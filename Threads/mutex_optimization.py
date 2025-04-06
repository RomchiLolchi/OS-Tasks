# Оптимизация использования мьютексов - программа принимает количество потоков на создание и создаёт их;
# потоки в цикле увеличивают значение глобальной переменной на 1 за каждую итерацию. Отличие от sync_common_memory_usage.py -
# оптимизированная синхронизация
import threading

global_variable = 0


def thread_task(thread_number):
    global global_variable
    for j in range(0, 1000000):
        global_variable += 1
    print(f"Поток {thread_number} завершил работу, global_variable={global_variable}")


if __name__ == "__main__":
    thread_amount = int(input("Введите количество потоков для создания: "))
    for i in range(0, thread_amount):
        thread = threading.Thread(target=thread_task, args=(i + 1,))
        thread.start()
        thread.join()
