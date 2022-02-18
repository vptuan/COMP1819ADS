import time as time


def linear_search(array, n, x):
    for i in range(0, n):
        if array[i] == x:
            return i
    return -1


def binary_search(array, l, r, x):

    if r >= 1:
        mid = l + (r - l) // 2

        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search(array, l, mid - 1, x)
        else:
            return binary_search(array, mid + 1, r, x)

    else:
        return -1


def time_linear(array, x):
    start = time.time()
    result = linear_search(array, len(array), x)
    if result == -1:
        print("Element is not present in the array")
    else:
        print("Element is present at index ", result)
    end = time.time()
    print("This search took " + str(end - start) + " seconds")


def time_binary(array, x):
    start = time.time()
    result = binary_search(array, 0, len(array) - 1, x)
    if result == -1:
        print("Element is not present in the array")
    else:
        print("Element is present at index ", result)
    end = time.time()
    print("This search took " + str(end - start) + " seconds")


def main():
    time_linear([2, 3, 4, 10, 40], 10)  # 0 seconds
    time_binary([2, 3, 4, 10, 40], 10)  # 0 seconds

    time_linear([1, 3, 5, 6, 5, 23, 36, 45, 56, 63, 85, 93, 95], 63)    # 0 seconds
    time_binary([1, 3, 5, 6, 5, 23, 36, 45, 56, 63, 85, 93, 95], 63)    # 0 seconds

    import random as random
    random_list = list()
    for i in range(100000000):
        random_list.append(i)
    time_linear(random_list, 48439546)  # 4.623 seconds
    time_binary(random_list, 48439546)  # 0 seconds


if __name__ == '__main__':
    main()
    