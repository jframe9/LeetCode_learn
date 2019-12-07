
def intersection(num1, num2):
    result = []
    num1 = list(set(num1))
    num2 = list(set(num2))
    for num in num1:
        if num in num2:
            result.append(num)

    return result

result = intersection([1,2,2,1], [2,2])
print(result)