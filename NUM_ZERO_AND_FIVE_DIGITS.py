def num_zero_and_five_digits(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 and digit == 5:
            count = count + 1
        n = n // 10
