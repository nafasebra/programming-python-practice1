import random

def generate_array(n):
    array = []
    for _ in range(n):
        array.append(random.randint(0, 100))
    return array

def print_min_max(array):
    min_value = min(array)
    max_value = max(array)
    print("The smallest array element: ", min_value)
    print("the biggest array element ", max_value)

def print_second_min_max(array):
    sorted_array = sorted(array)
    second_min_value = sorted_array[1]
    second_max_value = sorted_array[-2]
    print("2nd the smallest array element: ", second_min_value)
    print("2nd the biggest array element: ", second_max_value)

def reverse_array(array):
    reversed_array = array[::-1]
    print("rversed array: ", reversed_array)

def print_average(array):
    average = sum(array) / len(array)
    print("avarage of array: ", average)

n = int(input("Enter you number: "))
array = generate_array(n)

print("the array: ", array)
print_min_max(array)
print_second_min_max(array)
reverse_array(array)
print_average(array)
