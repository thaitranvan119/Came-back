import math
import numpy as np
import random as rd

def bubble_sort(list_a):
    n = len(list_a)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if list_a[j] < list_a[j - 1]:
                t = list_a[j]
                list_a[j] = list_a[j - 1]
                list_a[j - 1] = t
    return list_a




if __name__ == "__main__":
    test = [0, 1, 6, 7, 4, 2, 3 , 9, 8, 5]
    print(bubble_sort(test))