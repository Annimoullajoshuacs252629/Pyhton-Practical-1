def swap_elements(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

swap_elements(numbers, 1, 3)

print("Updated List:", numbers)
