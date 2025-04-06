// Поедание памяти (Вар. calloc()) - пользователь выбирает количество выделяемой памяти за блок. Процесс выделения
// памяти документируется в консоль
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int chosenMemory, allMemory = 0;
    printf("Введите количество памяти за блок в МБ: \n");
    scanf("%d", &chosenMemory);
    chosenMemory *= 1048576;
    printf("\nНачало выделения памяти...");
    while (true)
    {
        int *mem = (int *) calloc(1, chosenMemory);
        if (mem == NULL)
        {
            printf("\nОшибка выделения памяти");
            exit(0);
        }
        allMemory += chosenMemory;
        printf("\nВыделено %d МБ памяти, всего на текущий момент: %d МБ", chosenMemory / 1048576, allMemory / 1048576);
    }
}
