def find_sum_and_difference(numbers, M, N):
    sorted_numbers = sorted(numbers) 
    nth_min = sorted_numbers[N-1]
    mth_max = sorted_numbers[-M]
    sum_value = mth_max + nth_min
    difference_value = mth_max - nth_min
    return sum_value, difference_value

numbers = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3

sum_value, difference_value = find_sum_and_difference(numbers, M, N)
print("Sum:", sum_value)
print("Difference:", difference_value)
