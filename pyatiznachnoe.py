def solve (number):
    hundreds = number//100
    tens_thousands = (number // 1000)*10
    thousands = number // 1000
    tens = number%100
    units = tens%10
    tens //= 10
    result = tens**units
    result *= hundreds
    result //= tens_thousands - thousands
    return result


print(solve(12345))
