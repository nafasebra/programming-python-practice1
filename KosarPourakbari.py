import random

def generate_array(n):
    array = []
    for _ in range(n):
        array.append(random.randint(0, 100))
    return array

def print_min_max(array):
    min_value = min(array)
    max_value = max(array)
    print("kuchek tarin onsor: ", min_value)
    print("bozorg tarin onsor: ", max_value)

def print_second_min_max(array):
    sorted_array = sorted(array)
    second_min_value = sorted_array[1]
    second_max_value = sorted_array[-2]
    print("dovomin kuchek tarin onsor: ", second_min_value)
    print("dovomin bozorg tarin onsor: ", second_max_value)

def reverse_array(array):
    reversed_array = array[::-1]
    print("maakoose araye: ", reversed_array)

def print_average(array):
    average = sum(array) / len(array)
    print("miangin: ", average)

n = int(input("enter number: "))
array = generate_array(n)

print("Array: ", array)
print_min_max(array)
print_second_min_max(array)
reverse_array(array)
print_average(array)
