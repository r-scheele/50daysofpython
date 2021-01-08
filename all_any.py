import sys
arr = ['Kunle', 'Tayo', 'Tola']
array = [2, 4, 6, 8, 10, 21]


opt1 = (char for char in range(10000))
opt3 = [char for char in range(10000)]
print(sys.getsizeof(opt1))
print(sys.getsizeof(opt3))


def all_even(arr):
    for num in arr:
        if (num%2 == 1):
            return False
    return True

opt2 = all_even(array)

