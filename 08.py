def bubbleSort(it):
    n = len(it)
    # Traverse through all iterable elements
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(n - i - 1):
            if it[j] > it[j+1]:
                it[j], it[j+1] = it[j+1], it[j]
    return it
def quickSort(it):
    n = len(it)
    if n <= 1:
        return it
    pivot = it[n // 2]
    left = [x for x in it if x < pivot]
    right = [x for x in it if x > pivot]
    middle = [x for x in it if x == pivot]
    return quickSort(left) + middle + quickSort(right)

# lst1 = [5, 0, 0, -3, -9]
# lst2 = [5, 0, 0, -3, -9]
# bubbleSort(lst1)
# print(lst1)
# print(quickSort(lst2))

import random
import time
lst = []
for _ in range(10_0):
    lst.append(random.randint(1, 10_000))
print(lst)
# lst2 = lst.copy()
# lst3 = lst.copy()
# start = time.perf_counter_ns()
# bubbleSort(lst)
# print(time.perf_counter_ns() - start)
#
# start = time.perf_counter_ns()
# quickSort(lst2)
# print(time.perf_counter_ns() - start)
#
