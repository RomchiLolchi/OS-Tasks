# Использование сигналов для взаимодействия процессов, №2 - программа, отправляющая заданный сигнал на заданный pid.
# Компаньон первой программы, выводящей строки на экран; используется для изменения вывода первой программы. Принимает
# только ввод с клавиатуры. Обработка пользовательских ошибок не предусмотрена!!
import signal
import os

def send_signal_flow():
    signal_to_send: signal
    signal_input = input(
        "╔Введите номер сигнала для отправки:\n"
        "╠[1] SIGUSR1\n"
        "╠[2] SIGUSR2\n"
        "╚[3] SIGINT (+ завершает работу и этой программы)\n"
    )
    if signal_input == "1":
        signal_to_send = signal.SIGUSR1
    elif signal_input == "2":
        signal_to_send = signal.SIGUSR2
    else:
        signal_to_send = signal.SIGINT
    pid = int(input("Введите pid процесса, которому нужно отправить сигнал:\n"))
    os.kill(pid, signal_to_send)

    if signal_to_send == signal.SIGINT:
        print("Отправлен SIGINT, Завершение процессов...")
        exit(0)


if __name__ == "__main__":
    while True:
        send_signal_flow()