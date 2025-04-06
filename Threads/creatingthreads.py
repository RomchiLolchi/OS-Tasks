# Создание потоков - программа принимает количество потоков на создание и создаёт их (также принимает сколько каждый
# поток должен напечатать строк)
import threading
import os


def thread_task(thread_number, print_amount):
    for j in range(0, print_amount):
        print(f"Это поток {thread_number} с pid {os.getpid()}, вывод № {j + 1}")


if __name__ == "__main__":
    thread_amount = int(input("Введите количество потоков для создания: "))
    user_print_amount = int(input("Введите количество строк, которое выведет каждый из потоков: "))
    for i in range(0, thread_amount):
        thread = threading.Thread(target=thread_task, args=(i + 1, user_print_amount))
        thread.start()
        thread.join()
    print("Все потоки завершили работу, завершение программы...")
    exit(0)