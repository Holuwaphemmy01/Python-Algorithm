# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
#
# Examples:
# Input: 42145 Output: 54421
#
# Input: 145263 Output: 654321
#
# Input: 123456789 Output: 987654321
#




def descending(numbers):
    value = []
    numbers = str(numbers)
    for x in range(len(numbers)):
        number = int(numbers[x])
        value.append(number)

    for x in range(len(value)):
        for y in range(len(value)):
            # if x == y:
            #     continue
            if value[x] > value[y]:
                value[x], value[y] = value[y], value[x]

    result = ''
    for x in range(len(value)):
        result += str(value[x])
    return int(result)



