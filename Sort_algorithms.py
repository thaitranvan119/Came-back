import math
import numpy as np
import random as rd
import time

# Sort algorithms
def bubble_sort(list_a):
    n = len(list_a)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if list_a[j] < list_a[j - 1]:
                t = list_a[j]
                list_a[j] = list_a[j - 1]
                list_a[j - 1] = t
    return list_a

def insertion_sort(list_a):
    n = len(list_a)
    for i in range(1, n):
        tmp = i
        curr_value = list_a[i]
        while tmp > 0 and list_a[tmp - 1] > curr_value:
            list_a[tmp] = list_a[tmp - 1]
            tmp -= 1
        list_a[tmp] = curr_value   
    return list_a

def quick_sort(list_a):

    return list_a


# Reverse list
def reverse(list_a):
    n = len(list_a)
    for i in range(n//2):
        t = list_a[i]
        list_a[i] = list_a[n - 1 - i]
        list_a[n - 1 - i] = t
    return list_a


if __name__ == "__main__":
    np.random.seed(11)
    test = list(np.random.permutation(10000))
    test_2 = list(range(10000))

    a = reverse(test_2)

    s_time = time.time()
    print(a[:10])
    s_1 = insertion_sort(a)
    print(s_1[:10])
    print(time.time() - s_time)
    print('-----------------------------')

    s_time = time.time()
    print(a[:10])
    s_2 = bubble_sort(a)
    print(s_2[:10])
    print(time.time() - s_time)
    print('-----------------------------')
    