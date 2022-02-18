# Module 3 - File 1
# Cori Miller 

# Calculating the maximum value
def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

max_number_set = [12,36,27]

print('In the following set of numbers, what is the maximum?', max_number_set)

print(maximum(12,36,27))

## Calculating the minimum value

def minimum(value1, value2, value3, value4):
    """Return the min of 4 values."""
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    if value4 < min_value:
        min_value = value4
    return min_value

min_number_set = [15, 9, 27, 14]

print('In the following set of numbers, what is the minimum?', min_number_set)

print(minimum(15, 9, 27, 14))

