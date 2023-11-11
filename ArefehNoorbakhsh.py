import random

def generate_array(n):
    array = []
    for _ in range(n):
        array.append(random.randint(0, 100))
    return array

def print_min_max(array):
    min_value = min(array)
    max_value = max(array)
    print("کوچک ترين عنصر آرايه ", min_value)
    print("بزرگترين عنصر آرايه ", max_value)

def print_second_min_max(array):
    sorted_array = sorted(array)
    second_min_value = sorted_array[1]
    second_max_value = sorted_array[-2]
    print("دومين کوچک ترين مقدار آرايه: ", second_min_value)
    print("دومين بزرگترين مقدار آرايه: ", second_max_value)

def reverse_array(array):
    reversed_array = array[::-1]
    print("برعکس آرايه: ", reversed_array)

def print_average(array):
    average = sum(array) / len(array)
    print("ميانگين آرايه: ", average)

n = int(input("عدد دلخواه را جهت ساخت آرايه وارد کنيد :"))
array = generate_array(n)

print("آرايه: ", array)
print_min_max(array)
print_second_min_max(array)
reverse_array(array)
print_average(array)
