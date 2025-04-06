cmake_minimum_required(VERSION 3.30)
project(OS_tasks C)

set(CMAKE_C_STANDARD 11)

add_executable(MemoryEatingCalloc
        eatingmemory_calloc.c)

add_executable(MemoryEatingMalloc
        eatingmemory_malloc.c)